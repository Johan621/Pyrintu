"""Idempotent seed entrypoint for the MVP activity catalog."""

from __future__ import annotations

import asyncio

from pyrintu_api.db import SessionLocal
from pyrintu_api.seeds.mvp_activities import seed_mvp_activities


async def main() -> None:
    async with SessionLocal() as session:
        inserted = await seed_mvp_activities(session)
    print(f"Seeded {inserted} MVP activity catalog row(s).")


if __name__ == "__main__":
    asyncio.run(main())
