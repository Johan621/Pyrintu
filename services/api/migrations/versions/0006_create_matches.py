"""create matches table

Revision ID: 0006_create_matches
Revises: 0005_opportunity_unique_constraint
Create Date: 2026-08-15
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0006_create_matches"
down_revision = "0005_opportunity_unique_constraint"
branch_labels = None
depends_on = None


def upgrade() -> None:
    uuid_type = sa.Uuid(as_uuid=True)
    
    op.create_table(
        "matches",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("opportunity_id", uuid_type, nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["opportunity_id"], ["opportunities.id"]),
    )
    op.create_index("ix_matches_opportunity_id", "matches", ["opportunity_id"])
    op.create_index("ix_matches_status", "matches", ["status"])
    op.create_index("ix_matches_expires_at", "matches", ["expires_at"])


def downgrade() -> None:
    op.drop_index("ix_matches_expires_at", table_name="matches")
    op.drop_index("ix_matches_status", table_name="matches")
    op.drop_index("ix_matches_opportunity_id", table_name="matches")
    op.drop_table("matches")
