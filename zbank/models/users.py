from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from zbank import models
from zbank.database import Base


class Users(Base, models.IdMixin):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column("name", String(32))
    surname: Mapped[str] = mapped_column("surname", String(32))
    username: Mapped[str] = mapped_column("username", String(32), unique=True)
    email: Mapped[str] = mapped_column("email", String(128), unique=True)
    password: Mapped[str] = mapped_column("password", String(256))
