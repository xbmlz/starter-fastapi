"""init

Revision ID: ad1af593565b
Revises: 
Create Date: 2022-12-06 17:27:35.799403

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "ad1af593565b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # sys_user
    op.create_table(
        "sys_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("account", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    pass


def downgrade() -> None:
    # sys_user
    op.drop_table("sys_user")
    pass
