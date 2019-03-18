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


yoss = Users()

#yoss.create_user(0 'Yossi','lösenord')
