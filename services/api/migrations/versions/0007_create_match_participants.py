"""create match_participants table

Revision ID: 0007_create_match_participants
Revises: 0006_create_matches
Create Date: 2026-08-15
"""

from alembic import op
import sqlalchemy as sa

revision = "0007_create_match_participants"
down_revision = "0006_create_matches"
branch_labels = None
depends_on = None


def upgrade() -> None:
    uuid_type = sa.Uuid(as_uuid=True)
    
    op.create_table(
        "match_participants",
        sa.Column("match_id", uuid_type, primary_key=True, nullable=False),
        sa.Column("user_id", uuid_type, primary_key=True, nullable=False),
        sa.Column("decision", sa.String(length=32), nullable=False),
        sa.Column("decided_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("mutuality_reveal_state", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["match_id"], ["matches.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index("ix_match_participants_user_id", "match_participants", ["user_id"])
    op.create_index("ix_match_participants_decision", "match_participants", ["decision"])


def downgrade() -> None:
    op.drop_index("ix_match_participants_decision", table_name="match_participants")
    op.drop_index("ix_match_participants_user_id", table_name="match_participants")
    op.drop_table("match_participants")
