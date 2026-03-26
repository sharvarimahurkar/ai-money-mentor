from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    advice = ""

    if request.method == 'POST':
        age = int(request.form['age'])
        income = int(request.form['income'])
        expenses = int(request.form['expenses'])
        goal = request.form['goal']

        savings = income - expenses

        if savings > 10000:
            advice = f"You can save ₹{savings}. Start SIP of ₹5000 and keep emergency fund."
        elif savings > 5000:
            advice = f"You can save ₹{savings}. Start small SIP of ₹3000."
        else:
            advice = "Reduce expenses before investing."

    return render_template('index.html', advice=advice)

if __name__ == '__main__':
    app.run(debug=True)