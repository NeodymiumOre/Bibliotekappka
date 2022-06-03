# This file is supposed to be executed ONCE!!!

from sqlalchemy import literal_column
from database import *
from sqlalchemy.sql import func
from sqlalchemy import text

db = Database()
db.connect("root", "maciej")

# # add user librarian
# librarian = text("create user librarian identified by 'librarian';")
# results = db.engine.execute(librarian)

# # grant privileges to librarian
# librarianPriv = text("GRANT ALL PRIVILEGES ON *.* TO librarian IDENTIFIED BY 'librarian';")
# results = db.engine.execute(librarianPriv)
# db.engine.execute("FLUSH PRIVILEGES;")

# # create user reader
# reader = text("create user reader identified by 'reader';")
# results = db.engine.execute(reader)

# grant privileges to reader
readerPriv = text("GRANT SELECT ON *.* TO reader IDENTIFIED BY 'reader';")
results = db.engine.execute(readerPriv)
db.engine.execute("FLUSH PRIVILEGES;")

