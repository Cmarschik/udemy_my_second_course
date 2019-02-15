from user import User
from database import Database

Database.initialise(database='learning', host='localhost', user='postgres', password='CpSQLM')

user = User('cmarschik@gmail.com','Colton', 'Marschik', None)

user.save_to_db()

user_from_db = user.load_from_db_by_email('cmarschik@gmail.com')

print(user_from_db)