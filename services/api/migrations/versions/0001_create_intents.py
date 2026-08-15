"""create intents table

Revision ID: 0001_create_intents
Revises:
Create Date: 2026-08-15
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001_create_intents"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    uuid_type = sa.Uuid(as_uuid=True)
    json_type = postgresql.JSONB().with_variant(sa.JSON(), "sqlite")

    op.create_table(
        "intents",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("owner_user_id", uuid_type, nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("goal_type", sa.String(length=64), nullable=False),
        sa.Column("raw_input", sa.Text(), nullable=True),
        sa.Column("normalized_goal_json", json_type, nullable=False),
        sa.Column("constraints_json", json_type, nullable=False),
        sa.Column("availability_json", json_type, nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("closed_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_intents_owner_user_id", "intents", ["owner_user_id"])
    op.create_index("ix_intents_status", "intents", ["status"])


def downgrade() -> None:
    op.drop_index("ix_intents_status", table_name="intents")
    op.drop_index("ix_intents_owner_user_id", table_name="intents")
    op.drop_table("intents")
