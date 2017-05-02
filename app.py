from flask import Flask
import json

# Create the app var to run as a webserver for local development
app = Flask(__name__)

# This defines the index page returning just a string.
# app.route bind the url typed in the browser with the method main_page

@app.route("/")
def main_page():
	return json.dumps([{"nome":"Testing","cognome":"Testing"}, {"file":"index.html"}])
	

# Run the webserver in localhost at port 5000 - default
if __name__ == "__main__":
	app.run(host="0.0.0.0")
