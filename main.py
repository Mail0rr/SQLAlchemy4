from app.routes import app
from app.db.models import base

app.run(port=30000, debug=True)