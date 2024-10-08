"""add unit_price column to order product association table

Revision ID: a649eb208a63
Revises: 0e07ff36ebb5
Create Date: 2024-08-20 22:32:41.056510

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a649eb208a63"
down_revision: Union[str, None] = "0e07ff36ebb5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_product_association",
        sa.Column("unit_price", sa.Integer(), server_default="0", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_product_association", "unit_price")
    # ### end Alembic commands ###
