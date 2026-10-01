from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True
    )

    category: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )
    priority: Mapped[int] = mapped_column(
        default=3,
        nullable=False
    )