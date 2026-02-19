# to search for posts by their title or content. This feature can be useful for users who want to quickly find relevant posts.
# This endpoint will be a GET request at the path /api/posts/search, and it will take query parameters for the search terms.

# The input to this endpoint will be provided as query parameters in the URL.
# You should support at least two parameters: title and content.
# If the client provides these parameters, your endpoint should return posts where the title or content contain the given search terms.

# For example, a request to /api/posts/search?title=flask
# should return all posts where the title includes the word "flask".
# The output should be a list of posts that match the search criteria, in the same format as the “list” endpoint.
# If no posts match the search criteria, your endpoint should return an empty list.


# After you’ve implemented the “search” endpoint, it’s time to test it with Postman.
# Start your Flask app if it’s not already running.
# Open Postman and create a new GET request to http://localhost:5002/api/posts/search, adding query parameters for your search terms.
# Send the request.