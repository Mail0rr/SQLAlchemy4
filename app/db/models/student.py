from __future__ import annotations

from typing import(
    List,
    Optional
)

from sqlalchemy import (
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from . import(
    Base
)
from .group import Group

from .associates import student_group_assoc_table

class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[Optional[str]]
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int] = mapped_column()
    adress: Mapped[str] = mapped_column(String(200))

    groups: Mapped[List[Group]] = relationship(secondary=student_group_assoc_table)

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, surname={self.surname}, age={self.age}, address={self.address})"