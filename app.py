from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('new.pkl', 'rb'))

app = Flask(__name__)

############################################## REPO Files ########################################

#Homepage route when app first runs
@app.route('/')
def home():
    return render_template('index.html')

#Homepage route when navigating from another page

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
@app.route('/calculate')
def form():
    return render_template('calculate.html')


@app.route('/predict', methods=['POST'])
#!!! THIS 'calc' used to be 'home' in tutorial!!!!!!
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
    #data15 = request.form['currentpayment']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7,
    data8, data9, data10, data11, data12, data13, data14, data15]])
    #pred = model.predict(arr)
    pred = "${:,.2f}".format(float(model.predict(arr))) + "/month"
    # return pred
    return render_template('outcome.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)



##############################################Tutorial########################################











