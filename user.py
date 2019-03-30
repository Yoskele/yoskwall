import sqlite3


class Users():

    def __init__(self):

        self.connection=sqlite3.connect('thenewwall.db')

        self.cursor=self.connection.cursor()


    def create_user(self, username, password):

        query = "INSERT INTO users (username, password) VALUES ('{}', '{}')".format(username,password)

        self.cursor.execute(query)

        self.connection.commit()

        self.connection.close()

    def check_user(self, username, password):
        '''If we have a user with the given user name and password, return True.
        Otherwise, return False.'''
        data = (username, password)
        
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', data)
        row = self.cursor.fetchone()
        print(row)
        if row is not None:
            return True
        return False




#yoss.create_user('gjngjg', 'löshfhfenord')
