from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, Flask!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
