#CORS stands for Cross-Origin Resource Sharing.
# It’s a mechanism that allows many resources on a webpage to be requested from another domain outside the domain from which the resource originated.

from flask_cors import CORS

CORS(app)  # This will enable CORS for all routes

#By default, web browsers restrict JavaScript from making requests across domains for security reasons. This is where CORS comes into play: it allows the server to specify who can access its resources and how.

# When you use the CORS extension in Flask, you’re telling your Flask application to set specific headers in its HTTP response that instruct the browser that it’s okay to let the JavaScript code running on your computer access the data from Codio.

# Without CORS, if you tried to make requests from your frontend to your Flask app on Codio, your browser would block it. But with CORS(app), your Flask app on Codio is configured to allow these cross-origin requests, enabling your frontend to successfully communicate with your backend.