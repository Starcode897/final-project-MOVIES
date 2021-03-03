from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('/Users/tylerbrown/Documents/Data Science bootcamp/machine_learning_works/new.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def cal():
    return render_template('calculate.html')

@app.route('/learning')
def learn():
    return render_template('learning.html')

@app.route('/about')
def about():
    return render_template('about.html')


# The app grabs the info submitted from predict.html, and passes it into the model as an array.
# According to flask, the model doesn't exist.

@app.route('/predict', methods=['POST'])
def calc():
    data1 = request.form['gender']
    data2 = request.form['retired']
    data3 = request.form['partner']
    data4 = request.form['dependents']
    data5 = request.form['tenure']
    data6 = request.form['telephone']
    data7 = request.form['DSL']
    data8 = request.form['Fiber']
    data9 = request.form['security']
    data10 = request.form['backup']
    data11 = request.form['protection']
    data12 = request.form['techsupport']
    data13 = request.form['streamtv']
    data14 = request.form['streammovie']
    data15 = request.form['billing']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7,
    data8, data9, data10, data11, data12, data13, data14, data15]])
    pred = model.predict(arr)
    return render_template('outcome.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















