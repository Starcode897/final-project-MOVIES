from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model_pickle', 'rb'))

app = Flask(__name__)

############################################## REPO Files ########################################

#Homepage route when app first runs
@app.route('/')
def home():
    return render_template('index.html')

#Homepage route when navigating from another page
@app.route('/home')
def homepage():
    #Go to webpage
    return render_template('index.html')

#Route for learning page
@app.route("/learning")
def learning():
    #Go to webpage
    return render_template('learning.html')

#Route for about page
@app.route("/about")
def about():
    #Go to webpage
    return render_template('about.html')



############################################## REPO TEMPLATE ########################################




############################################## Tutorial ########################################

#Input templates
@app.route('/input')
def form():
    return render_template('input.html')


@app.route('/predict', methods=['POST'])
#!!! THIS 'calc' used to be 'home' in tutorial!!!!!!
def calc():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    # return pred
    return render_template('predict.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)



##############################################Tutorial########################################











