# In this step, you’ll be enhancing your “list” endpoint (/api/posts) to allow sorting of blog posts.
# This functionality provides flexibility to users to organize the posts as per their needs.
# these new parameters are optional. If the user does not provide them, the endpoint should behave exactly as it did before, listing posts in their original order.
# This endpoint will accept two new query parameters for sorting: sort and direction.

# sort: Specifies the field by which posts should be sorted. It should accept the values title or content.
# direction: Specifies the sort order. It should accept asc for ascending order and desc for descending order.

# For instance, a request to /api/posts?sort=title&direction=desc
# would return all posts sorted by their title in descending order.

# Remember, these parameters are not mandatory. If a user doesn’t provide them, your endpoint should simply return posts in their original order.
# The output of this endpoint should be a list of posts sorted based on the provided parameters.
# f the parameters are not provided, the list should retain the original order of posts.
# In the event of invalid sort fields or directions, your endpoint should return a status code of 400 Bad Request along with an error message indicating the issue.

#
# Testing Your API
# Once you’ve added sorting functionality, it’s time to test it using Postman.
# Make sure your Flask application is running.
# Open Postman and make a new GET request to http://localhost:5002/api/posts, adding your sort field and direction as query parameters.
# Send the request.
# The returned list of posts should be sorted according to your parameters. Try changing these parameters and observe the change in results.