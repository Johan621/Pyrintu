"""add opportunity uniqueness constraint

Revision ID: 0005_opportunity_unique_constraint
Revises: 0004_create_opportunities
"""

from alembic import op

revision = "0005_opportunity_unique_constraint"
down_revision = "0004_create_opportunities"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        "uq_opportunity_scope_candidate",
        "opportunities",
        ["user_id", "intent_id", "candidate_type", "candidate_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("uq_opportunity_scope_candidate", "opportunities")
