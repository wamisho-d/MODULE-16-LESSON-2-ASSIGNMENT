# Flask API Code
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://sums.db' # Adjust to your database
db = SQLAlchemy(app)

# Model for Sum
class Sum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'result': self.result
        }

# Create the database
with app.app_context():
    db.create_all()

@app.route('/sum', methods=['POST'])
def add_sum():
    data = request.json
    new_sum = Sum(result=data['result'])
    db.session.add(new_sum)
    db.session.commit()
    return jsonify(new_sum.serialize()), 201

@app.route('/sum', methods=['GET'])
def get_all_sums():
    sums = Sum.query.all()
    return jsonify([sum.serialize() for sum in sums])
if __name__ == '__main__':
    app.run(debug=True)

