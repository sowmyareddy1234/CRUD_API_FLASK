from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def index():
    return render_template('task_1.html')  # Replace 'your_html_file.html' with the actual file name


# In-memory data store (replace with a database in a real-world scenario)
data_store = {
    1: {'name': 'ram', 'description': 'student'},
    2: {'name': 'sita', 'description': 'student'},
    4: {'name': 'raju', 'description': 'teacher'},
    5: {'name': 'ramya', 'description': 'Dean'},
    6: {'name': 'sowmya', 'description': 'student'},
    # Add more items as needed
}

# Endpoint to get all items
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(data_store)

# Endpoint to get a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

# Endpoint to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    try:
        data = request.get_json()
        item_id = max(data_store.keys()) + 1
        data_store[item_id] = {'name': data['name'], 'description': data['description']}
        return jsonify({'message': 'Item created successfully', 'item_id': item_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = data_store.get(item_id)
    if item:
        try:
            data = request.get_json()
            item['name'] = data['name']
            item['description'] = data['description']
            return jsonify({'message': 'Item updated successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Item not found'}), 404

# Endpoint to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = data_store.pop(item_id, None)
    if item:
        return jsonify({'message': 'Item deleted successfully'})
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
