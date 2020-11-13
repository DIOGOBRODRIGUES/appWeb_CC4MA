from flask import Flask
from vogais3 import search4letters
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'Hello World from Flask! '

@app.route('/search4')
def do_search() ->str:
    return str(search4letters('Maria Luiza Moura!', 'MLyiz,!'))
app.run()