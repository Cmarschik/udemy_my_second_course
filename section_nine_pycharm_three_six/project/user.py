from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def save_to_db(self): #save user to database we made in postgreSQL
        with CursorFromConnectionFromPool() as cursor: #connect to database first(create a variable called 'connection' to do so)(give it these parameters
            cursor.execute('INSERT INTO users(email, first_name, last_name) VALUES(%s, %s, %s)',
                                (self.email, self.first_name, self.last_name))


    @classmethod
    def load_from_db_by_email(cls, email): #returns/creates a new object(user) with this data from the database
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,)) #add a ',' after 'email' so python knows we made a tuple and
            user_data = cursor.fetchone() #'fetchone' retrieves the first row
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[2], id=user_data[0]) #returns the email, fname, lname, and id(using the order in which they are on the postgreSQL table
                         # ^calls the current class which is the User class for the data inserted above


