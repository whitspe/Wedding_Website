from flask import Flask, render_template


# Create a flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
	return "<h1>Welcome to the Wedding Website!</h1>"