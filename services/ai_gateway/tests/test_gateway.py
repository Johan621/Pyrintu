from pyrintu_ai import AIRequest, AIResultType, MockProvider, PyrintuAIGateway


def test_gateway_requires_authorized_context() -> None:
    gateway = PyrintuAIGateway(MockProvider())

    response = gateway.generate(AIRequest(user_input="What should I do?"))

    assert response.result_type == AIResultType.INSUFFICIENT_CONTEXT
    assert response.provider == "local-policy"


def test_gateway_forwards_only_authorized_context() -> None:
    provider = MockProvider("safe answer")
    gateway = PyrintuAIGateway(provider)

    response = gateway.generate(
        AIRequest(
            user_input="Suggest something quiet.",
            result_type=AIResultType.SUGGESTION,
            authorized_context="Venue A is verified and quiet.",
        )
    )

    assert response.result_type == AIResultType.SUGGESTION
    assert response.text == "safe answer"
    assert len(provider.calls) == 1
    instructions, user_input, _ = provider.calls[0]
    assert "untrusted data" in instructions
    assert "Venue A is verified and quiet." in user_input
    assert "private hidden data" not in user_input


def test_action_proposals_are_not_executed_by_gateway() -> None:
    provider = MockProvider("Propose moving the meetup to 7 PM.")
    gateway = PyrintuAIGateway(provider)

    response = gateway.generate(
        AIRequest(
            user_input="Can we move it to 7 PM?",
            result_type=AIResultType.ACTION_PROPOSAL,
            authorized_context="Current meetup time is 6 PM.",
        )
    )

    assert response.result_type == AIResultType.ACTION_PROPOSAL
    assert response.text.startswith("Propose")
