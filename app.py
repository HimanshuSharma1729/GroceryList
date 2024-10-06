from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from grocery_list import groceries  # Import the grocery list from grocery_list.py

app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the GroceryItem model
class GroceryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Item {self.name}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display grocery items
@app.route('/')
def index():
    all_items = GroceryItem.query.all()  # Fetch all items from the database
    return render_template('index.html', all_items=all_items, groceries=groceries)

# Route to add items
@app.route('/add_items', methods=['POST'])
def add_items():
    item_name = request.form.get('select_items')
    if item_name:
        # Check if the item already exists in the database
        existing_item = GroceryItem.query.filter_by(name=item_name).first()
        if not existing_item:  # Only add if it does not exist
            new_item = GroceryItem(name=item_name)
            db.session.add(new_item)
            db.session.commit()
    return redirect(url_for('index'))

# Route to remove items
@app.route('/remove_items', methods=['POST'])
def remove_items():
    checked_items = request.form.getlist('check')
    for item_name in checked_items:
        item_to_delete = GroceryItem.query.filter_by(name=item_name).first()
        if item_to_delete:
            db.session.delete(item_to_delete)
            db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
