from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#now connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Shawn/application/stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking to save resources

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    items = Item.query.all()  # Query all items from the database
    return render_template('index.html', items=items)

#def hello():
#    return ("<h>Hello</h>"
#            "let me try to write a little more stuff")

@app.route('/receivers')
def receivers():
    return "Fantasy Football receivers"

@app.route('/tight_ends')
def tight_ends():
    return "Fantasy Football tight ends"

@app.route('/running_backs')
def running_backs():
    return "Running backs"


if __name__ == '__main__':
    app.run(debug=True)