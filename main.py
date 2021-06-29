from app import create_app, db
from flask_migrate import Migrate
from app.models import Address_State, Address_City, Buyer

app = create_app("development")

Migrate(app, db)

@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
        Address_City=Address_City,
        Address_State=Address_State,
        Buyer=Buyer
    )

