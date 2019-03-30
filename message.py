import sqlite3


class Message():
  def __init__(self):
    self.connection = sqlite3.connect('thenewwall.db')
    self.cursor = self.connection.cursor()


  def save(self, username, text):
    query = "INSERT INTO messages (username, text) VALUES (?, ?)"
    self.cursor.execute(query, (username, text))
    self.connection.commit()


  def all(self):
    query = "SELECT * FROM messages ORDER BY id DESC"
    self.cursor.execute(query)
    messages = []
    for item in self.cursor.fetchall():
      message = {
        'username': item[1],
        'text': item[2]
      }
      messages.append(message)

    return messages


  def delete(self):
    query = 'DELETE from messages WHERE username = "admin"'
    self.cursor.execute(query)
    self.connection.commit()



#  def close(self):
#    self.connection.close()


