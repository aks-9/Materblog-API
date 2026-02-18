from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

posts = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


def validate_post_data(data):
    if not isinstance(data, dict):
        return "Invalid data format."
    if "title" not in data or "content" not in data:
        return "Missing 'title' or 'content'."
    if not data["title"].strip() or not data["content"].strip(): #checks empty fields entered by user
        return "Title and content cannot be empty."
    return None

@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'POST':

        new_post = request.get_json()
        error_message = validate_post_data(new_post)
        if error_message:
            return jsonify({'error': error_message}), 400

        new_id = max((post['id'] for post in posts), default=0) + 1
        new_post['id'] = new_id

        posts.append(new_post)
        return jsonify(new_post), 201
    else:
        return jsonify(posts)


def get_post_by_id(post_id):
    for post in posts:
        if post['id'] == post_id:
            return post
    return None


@app.route('/api/posts/<int:post_id>', methods= ['DELETE'])
def delete_post(post_id):
    post = get_post_by_id(post_id)
    if post is None:
        return 'post not found', 404
    posts.remove(post)
    return jsonify(post), 200

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Find the post with the given
    post = get_post_by_id(post_id)

    # If the post wasn't found, return a 404 error
    if post is None:
        return jsonify({"error": "post not found"}), 404

    # Update the post with the new data
    new_data = request.get_json()
    post.update(new_data)

    # Return the updated post
    return jsonify(post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
