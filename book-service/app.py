from flask import Flask, jsonify
import mysql.connector
import requests

db = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='root',
  database='books'
)

app = Flask('book-service')

@app.route('/', methods=['GET'])
def index():
  cursor = db.cursor(dictionary=True)
  cursor.execute('SELECT * FROM books')
  books = cursor.fetchall()
  tmp = []
  for book in books:
    book['author'] = requests.get('http://localhost:8000/'+str(book['author_id'])).json()
    del book['author_id']
    tmp.append(book)
  return jsonify(tmp)

if __name == "__main__":
  app.run(port=8001)
