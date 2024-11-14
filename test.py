from typing import Optional
from flask import render_template
from app.db import engine


def great(name: Optional[str]) -> str:
    if name is not None:
        return f"Hello {name}!"
    else:
        return "Hello, guest!"

print(great(None))