import pickle
from Flask import Flask, request, render_template # type: ignore

app = Flask(__name__)
model = pickle.load(open("lr.pkl", "wb"))

@app.route('/')
def input():
    return render_template('index.html')

@app.route("/prediction", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        low = float(request.form["low"]) 
        high = float(request.form["high"]) 
        volume = float(request.form["volume"]) 
        open_price = float(request.form["open"]) 
        company = int(request.form["company"]) 
        year = int(request.form["year"]) 
        month = int(request.form["month"])
        day = int(request.form["day"])

        xx = model.predict([[open_price, high, low, volume, year, month, day, company]])
        out = xx[0]

        print("Forecasted closing price on {}/{}/{} is $ {}".format(day, month, year, out))
        return render_template("index.html", prediction="Forecasted closing price on {}/{}/{} is $ {}".format(day, month, year, out))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
