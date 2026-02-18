# Input
# This endpoint does not require any input in the body of the request. The id of the post to be deleted is provided in the URL.

# Output
# If the post with the given id exists, your endpoint should delete the post and return a JSON object with the following structure:
{
    "message": "Post with id <id> has been deleted successfully."
}
#
# The status code of the response should be 200 OK.
#
# Error Handling
# Your endpoint should handle possible errors. If there is no post with the given id, your endpoint should return a response with the status code 404 Not Found and a message indicating that the post was not found.