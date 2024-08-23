from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microshop.core.models.base import Base

if TYPE_CHECKING:
    pass


class Order(Base):
    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        server_default=func.now(),
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_association",
        back_populates="orders",
        # lazy="noload",
    )
    products_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="order",
    )
