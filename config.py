import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Create a database in project and get its path.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db").replace("\\", "/")
