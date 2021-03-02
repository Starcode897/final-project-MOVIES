from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model_pickle', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('predict.html')


# The app grabs the info submitted from predict.html, and passes it into the model as an array.
# According to flask, the model doesn't exist.

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['gen']
    data2 = request.form['retire']
    data3 = request.form['pard']
    data4 = request.form['depend']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    # return pred
    return render_template('after_predict.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















