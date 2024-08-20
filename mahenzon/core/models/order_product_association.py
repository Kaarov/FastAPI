from typing import TYPE_CHECKING

from sqlalchemy import Table, ForeignKey, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .order import Order
    from .product import Product


class OrderProductAssociation(Base):
    __tablename__ = "order_product_association"
    __table_args__ = (
        UniqueConstraint(
            "order_id",
            "product_id",
            name="idx_unique_order_association",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    count: Mapped[int] = mapped_column(default=1, server_default="1")
    unit_price: Mapped[int] = mapped_column(default=0, server_default="0")

    # association between Assocation -> Order
    order: Mapped["Order"] = relationship(
        back_populates="products_details",
    )

    # association between Assocation -> Product
    product: Mapped["Product"] = relationship(
        back_populates="order_details",
    )
