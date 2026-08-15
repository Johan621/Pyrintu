import pytest

from pyrintu_intent import AIIntentInterpreter


class StubGenerator:
    def __init__(self, response: str) -> None:
        self.response = response
        self.requests: list[str] = []

    def generate(self, user_input: str) -> str:
        self.requests.append(user_input)
        return self.response


def test_ai_interpreter_validates_structured_json() -> None:
    generator = StubGenerator(
        '{"goal":"find something chill","experience":"chill","group_size":3,"budget_max":500,"time_window":"this weekend","location":"nearby"}'
    )
    interpreter = AIIntentInterpreter(generator)

    parsed = interpreter.parse("I want something chill this weekend")

    assert parsed.goal == "find something chill"
    assert parsed.group_size == 3
    assert parsed.budget_max == 500
    assert generator.requests == ["I want something chill this weekend"]


def test_ai_interpreter_rejects_invalid_json() -> None:
    interpreter = AIIntentInterpreter(StubGenerator("not-json"))

    with pytest.raises(ValueError, match="valid JSON"):
        interpreter.parse("Plan something")


def test_ai_interpreter_rejects_invalid_group_size() -> None:
    interpreter = AIIntentInterpreter(StubGenerator('{"goal":"go out","group_size":0}'))

    with pytest.raises(ValueError, match="group_size"):
        interpreter.parse("Plan something")
