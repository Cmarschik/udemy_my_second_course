from psycopg2 import pool



class Database:
    __connection_pool = None #adding two underscores hides the properpty '__connection_pool' so it is not misused in other parts of the program

    @classmethod
    def initialise(cls, **kwargs): #must be initialized to use this pool E.G. Database.initialise() / refers to the currently bound class(Database)
        cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                          10,
                                                          **kwargs)  # creates 1 connection instantly, with a max of 10 connections allows
                                                                   # this saves time bc connections are already made and don't have to be made every
                                                                   # ...time we reference postgreSQ:
                                                                   #**kwargs allows us to enter any number of named parameters when we call the function
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn() #adding two underscores at beginning makes getconn a private variable


    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall() #'closeall()' closes all connections

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None #when a new connection is made, it is simply None bc we have not 'getconn' yet
        self.cursor = None

    def __enter__(self): #required to use the 'with' clause in main code
        self.connection = Database.get_connection() #gets us a connection from the pool
        self.cursor = self.connection.cursor() #creates a cursor that will be accessed when we use this class
        return self.cursor #returns it so it is usable

    def __exit__(self, exception_type, exception_value, exception_traceback): #required to use the 'with' clause in main code / 'exception' give us error information if an error ocurs inside the 'with' clause
        if exception_value is not None: #if we receive an exception value/error E.G. TypeError, ValueError, AttributeError
            self.connection.rollback() #rolls back connection/goes back to just before the connection went through and brought up an error
        else:
            self.cursor.close() #closes the cursor
            self.connection.commit() #must commit before we return a connection back to pool
        Database.return_connection(self.connection) #returns a connection to the pool

