from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

posts = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/api/docs"  # (1) swagger endpoint e.g. HTTP://localhost:5002/api/docs
API_URL="/static/masterblog.json" # (2) ensure you create this dir and file

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Masterblog API' #
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


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
        sort_field = request.args.get('sort')
        direction = request.args.get('direction', 'asc')

        if not sort_field:
            return jsonify(posts)

        if sort_field not in ['title', 'content']:
            return jsonify({"error": "Invalid sort field. Must be 'title' or 'content'."}), 400

        if direction not in ['asc', 'desc']:
            return jsonify({"error": "Invalid direction. Must be 'asc' or 'desc'."}), 400

        reverse = (direction == 'desc')
        sorted_posts = sorted(posts, key=lambda x: x[sort_field].lower(), reverse=reverse) #using lamda function

        return jsonify(sorted_posts)


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


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_query = request.args.get('title', '').lower()
    content_query = request.args.get('content', '').lower()

    filtered_posts = []
    for post in posts:
        # Check if title matches (if query provided)
        title_match = title_query in post['title'].lower() if title_query else False

        # Check if content matches (if query provided)
        content_match = content_query in post['content'].lower() if content_query else False

        if (title_query or content_query) and (title_match or content_match):
            filtered_posts.append(post)
        elif not title_query and not content_query:
            # If no query provided, return all posts (or you could return empty list depending on requirement)
            # Given the loop, we could just append all, but search usually implies some filter.
            # If no filters are provided, it's returning empty list in current code (because filtered_posts is empty).
            # Let's stick to returning empty list if no query provided to avoid returning all posts on empty search.
            pass

    return jsonify(filtered_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
