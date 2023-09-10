from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
numbers = {}

# Create a new number
@app.route('/number', methods=['POST'])
def add_number():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')

    if key in numbers:
        return jsonify({"error": "Key already exists"}), 400

    numbers[key] = value
    return jsonify({"success": True, "key": key, "value": value}), 201

# Retrieve a number by key
@app.route('/number/<key>', methods=['GET'])
def get_number(key):
    value = numbers.get(key)
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    
    return jsonify({"key": key, "value": value})

# Update a number by key
@app.route('/number/<key>', methods=['PUT'])
def update_number(key):
    if key not in numbers:
        return jsonify({"error": "Key not found"}), 404

    data = request.get_json()
    new_value = data.get('value')

    numbers[key] = new_value
    return jsonify({"success": True, "key": key, "updated_value": new_value})

# Delete a number by key
@app.route('/number/<key>', methods=['DELETE'])
def delete_number(key):
    if key not in numbers:
        return jsonify({"error": "Key not found"}), 404

    del numbers[key]
    return jsonify({"success": True, "message": "Number deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
