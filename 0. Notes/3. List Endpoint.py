# A blog post will have three properties:
# 'id’: A unique identifier for each post. This will be useful when we need to reference a specific post, such as when updating or deleting a post. This ID must be an integer.
# 'title’: The title of the blog post.
# 'content’: The content of the blog post.
# We’ll start with a hardcoded list of blog posts for simplicity. Each blog post will be a dictionary in this list. The ‘id’ for each post can be an integer that we manually assign for now, but we’ll look into ways of generating this automatically in later steps


POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
    # More posts go here...
]

# Testing Your API
# Start your Flask backend app and open Postman. In Postman, you’ll want to create a new GET request to 'http://localhost:5002/api/posts’. When you send this request, you should receive a response containing your list of blog posts.
# Deploy your backend code to Codio, and run it as we showed in the demo in the previous page by running the command:
# python3 backend/backend_app.py
# And then clicking on the “Open API Application” button.

# Test The Frontend
# Don’t forget to check your API with the frontend, as shown in the previous page. Your frontend application runs on your computer, and you don’t need to run it on Codio.
# In the next step, we’ll move on to creating more complex API operations, like adding, updating, and deleting blog posts. But before we move on, make sure your list operation is working correctly!