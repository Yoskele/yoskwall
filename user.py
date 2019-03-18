import sqlite3


class User():
  def __init__(self):
    self.connection = sqlite3.connect('thenewwall.db')
    self.cursor = self.connection.cursor()


  def save(self, email, password):
    query = "INSERT INTO users (email, password)VALUES (?, ?)"
    self.cursor.execute(query, (email, password))
    self.connection.commit()