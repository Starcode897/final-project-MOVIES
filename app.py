# Flask application to access our model for our web browser

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

@app.route("/model")
def dataModel():
    
if __name__ == "__main__":
    app.run(debug=True)