from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

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

        algoritma = request.form['algoritma']
        if algoritma == 'knn':
            model = joblib.load('static/model_ml/model_knn.pkl')
        elif algoritma == 'dt':
            model = joblib.load('static/model_ml/model_dt.pkl')
        elif algoritma == 'nb':
            model = joblib.load('static/model_ml/model_nb.pkl')
        elif algoritma == 'rf':
            model = joblib.load('static/model_ml/model_rf.pkl')

        prediction = model.predict(features)
        if prediction[0] == 0:
            result = 'Low'
        elif prediction[0] == 1:
            result = 'Medium'
        elif prediction[0] == 2:
            result = 'High'
        elif prediction[0] == 3:
            result = 'Very High'

        return render_template('index.html', prediction_text = f'Price Score is {result}')
    
    return render_template('index.html')   

if __name__ == "__main__":
    app.run(debug=True)