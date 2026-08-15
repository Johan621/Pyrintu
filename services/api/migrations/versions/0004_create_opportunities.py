"""create opportunities table

Revision ID: 0004_create_opportunities
Revises: 0003_create_activities
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0004_create_opportunities"
down_revision = "0003_create_activities"
branch_labels = None
depends_on = None


def upgrade() -> None:
    uuid_type = sa.Uuid(as_uuid=True)
    json_type = postgresql.JSONB().with_variant(sa.JSON(), "sqlite")

    op.create_table(
        "opportunities",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("user_id", uuid_type, nullable=False),
        sa.Column("intent_id", uuid_type, nullable=False),
        sa.Column("candidate_type", sa.String(length=64), nullable=False),
        sa.Column("candidate_id", uuid_type, nullable=False),
        sa.Column("visibility_state", sa.String(length=32), nullable=False),
        sa.Column("evidence_json", json_type, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["intent_id"], ["intents.id"]),
    )
    op.create_index("ix_opportunities_user_id_created_at", "opportunities", ["user_id", "created_at"])
    op.create_index("ix_opportunities_intent_id", "opportunities", ["intent_id"])


def downgrade() -> None:
    op.drop_index("ix_opportunities_intent_id", table_name="opportunities")
    op.drop_index("ix_opportunities_user_id_created_at", table_name="opportunities")
    op.drop_table("opportunities")
