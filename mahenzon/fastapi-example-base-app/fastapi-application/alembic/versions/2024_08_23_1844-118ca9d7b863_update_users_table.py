"""update users table

Revision ID: 118ca9d7b863
Revises: 4a1d034c05b0
Create Date: 2024-08-23 18:44:08.682154

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "118ca9d7b863"
down_revision: Union[str, None] = "4a1d034c05b0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f("uq_users_foo_bar"), "users", ["foo", "bar"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
