import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('static/model_ml/model_knn.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        battery = int(request.form['battery'])
        cam = int(request.form['cam'])
        memory = int(request.form['memory'])
        mwt = int(request.form['mwt'])
        prh = int(request.form['prh'])
        prw = int(request.form['prw'])
        ram = int(request.form['ram'])
        sh = int(request.form['sh'])
        sw = int(request.form['sw'])
        tt = int(request.form['tt'])
        features = [[battery, cam, memory, mwt, prh, prw, ram, sh, sw, tt]]
        prediction = model.predict(features)

        return render_template('index.html', prediction_text = f'Price Score is {prediction}')
    
    return render_template('index.html')   

if __name__ == "__main__":
    app.run(debug=True)