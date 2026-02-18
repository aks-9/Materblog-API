# In this step, you’ll create an API endpoint to update an existing blog post.
# This endpoint will be a PUT request at the path /api/posts/<id>, where <id> is the id of the post that the client wants to update.
# Here’s what this endpoint should do:
# Input
# This endpoint should expect a JSON object in the body of the request with the following structure:
# {
#     "title": "<new title>",
#     "content": "<new content>"
# }
# Both title and content are optional. If the client does not provide them, your endpoint should keep the current values.
# Output
# If the post with the given id exists and the client provides valid input, your endpoint should update the post and return a JSON object with the following structure:
# {
#     "id": "<id of the updated post>",
#     "title": "<new title or old title if not provided>",
#     "content": "<new content or old content if not provided>"
# }
# The status code of the response should be 200 OK.
# Error Handling
# Your endpoint should handle possible errors. If there is no post with the given id, your endpoint should return a response with the status code 404 Not Found and a message indicating that the post was not found.
# 🧪 Testing Your API
# After you’ve implemented the “update” endpoint, it’s time to test it with Postman.
# Start your Flask app if it’s not already running.
# Open Postman and create a new PUT request to http://localhost:5002/api/posts/<id>, replacing <id> with the id of a post you want to update.
# In the “Body” tab, select “raw” and then “JSON” from the dropdown menu.
# Enter a JSON object with ‘title’ and/or ‘content’ for the updated post.
# Send the request.
# You should receive a response with status code 200 and the updated post. If you send a GET request to /api/posts, the updated post should have the new title and/or content.
# Try also sending a PUT request with an id that does not exist, and check if your endpoint returns the correct error response.
# Testing The Frontend
# You probably noticed that the frontend does not support the update command. We didn’t implement these features in the frontend for the sake of simplicity, but the website should work properly with the previous features. Starting from this step, the frontend will not support future command.
# If you want to add more functionality to the website, wait for the bonus section! ❣️
# If everything is working as expected, congratulations! 🎉 You’ve successfully implemented the “update” operation. Your RESTful API is now complete! It can list, add, delete, and update blog posts. Well done!