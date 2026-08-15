"""create users and user profiles

Revision ID: 0002_create_users_and_profiles
Revises: 0001_create_intents
"""

from alembic import op
import sqlalchemy as sa

revision = "0002_create_users_and_profiles"
down_revision = "0001_create_intents"
branch_labels = None
depends_on = None


def upgrade() -> None:
    uuid_type = sa.Uuid(as_uuid=True)

    op.create_table(
        "users",
        sa.Column("id", uuid_type, primary_key=True, nullable=False),
        sa.Column("email", sa.String(length=320), nullable=True),
        sa.Column("phone", sa.String(length=32), nullable=True),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_unique_constraint("uq_users_email", "users", ["email"])
    op.create_unique_constraint("uq_users_phone", "users", ["phone"])

    op.create_table(
        "user_profiles",
        sa.Column("user_id", uuid_type, primary_key=True, nullable=False),
        sa.Column("display_name", sa.String(length=120), nullable=False),
        sa.Column("bio", sa.Text(), nullable=True),
        sa.Column("avatar_url", sa.String(length=2048), nullable=True),
        sa.Column("profile_visibility", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )


def downgrade() -> None:
    op.drop_table("user_profiles")
    op.drop_constraint("uq_users_phone", "users", type_="unique")
    op.drop_constraint("uq_users_email", "users", type_="unique")
    op.drop_table("users")
