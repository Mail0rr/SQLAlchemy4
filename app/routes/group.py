from itertools import dropwhile

from flask import request, render_template
from sqlalchemy.sql.visitors import iterate

from app import app
from app.db.models import Session, Group

from sqlalchemy import select

@app.post("/groups/")
def post_group():
    with Session() as session:
        session.add(Group(name=request.form.get("name"))) #INSERT INTO group VALUES (id, name)
        session.commit()

    return render_template("group/management.html")


@app.get("/groups/")
def get_group():
    with Session() as session:
        data = session.query(Group).all()  # SELECK id, name FROM group

    return render_template("group/management.html", iterable=data)


@app.get('/groups/<int:id>', methods=["GET"])
def group_get(id):
    with Session() as session:
        data = session.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template('main.html', content=data)
