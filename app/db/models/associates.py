from __future__ import annotations

from sqlalchemy import (
    Table,
    Column,
    ForeignKey
)
from . import(
    Base
)


student_group_assoc_table = Table(
    "student_group_assoc_table",
    Base.metadata,
    Column(
        "group_id",
        ForeignKey("group.id"),
        primary_key=True
    ),
    Column(
        "Student_id",
        ForeignKey("student.id"),
        primary_key=True
    ),
)