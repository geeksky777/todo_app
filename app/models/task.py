from sqlalchemy import ForeignKey, String, Text, Enum
from app.db.base import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column
import enum
from sqlalchemy.orm import relationship


class Status(enum.Enum):
    compiled = "compiled"
    not_completed = "not_completed"


class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[Status] = mapped_column(
        Enum(Status, name="status_enum"),
        default=Status.not_completed,
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="tasks")
