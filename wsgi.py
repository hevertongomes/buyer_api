from app import create_app
from os import environ

app = create_app(environ.get('ENVIRONMENT_PROJECT'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')