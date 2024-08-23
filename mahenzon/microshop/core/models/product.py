from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from microshop.core.models.base import Base

if TYPE_CHECKING:
    pass


class Product(Base):

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]

    orders: Mapped[list["Order"]] = relationship(
        secondary="order_product_association",
        back_populates="products",
    )
    order_details: Mapped["OrderProductAssociation"] = relationship(
        back_populates="product",
    )
