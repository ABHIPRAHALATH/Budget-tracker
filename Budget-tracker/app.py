from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize a simple budget tracker with predefined limits
budget = 1500
expenses = {'shopping': 0, 'food': 0, 'academic': 0,'medical':0}
limits = {'shopping': 500, 'food': 300, 'academic': 400,'medical' :200}

@app.route('/')
def index():
    total_expenses = sum(expenses.values())
    remaining_balance = budget - total_expenses
    return render_template('index.html', expenses=expenses, limits=limits, budget=budget, remaining_balance=remaining_balance , notification=notification)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form['category'] 
    amount = float(request.form['amount'])

    if category in expenses and expenses[category] + amount <= limits[category]:
        expenses[category] += amount
    return redirect('/')

@app.route('/remove_expense', methods=['POST'])
def remove_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    
    if category in expenses and expenses[category] >= amount:
        expenses[category] -= amount
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize a simple budget tracker with predefined limits
budget = 1000
expenses = {'shopping': 0, 'food': 0, 'academic': 0, 'medical' :0}
limits = {'shopping': 500, 'food': 300, 'academic': 400, 'medical' :200}

@app.route('/')
def index():
    total_expenses = sum(expenses.values())
    remaining_balance = budget - total_expenses
    return render_template('index.html', expenses=expenses, limits=limits, budget=budget, remaining_balance=remaining_balance)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])

    if category in expenses and expenses[category] + amount <= limits[category]:
        expenses[category] += amount
    return redirect('/')

@app.route('/remove_expense', methods=['POST'])
def remove_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    
    if category in expenses and expenses[category] >= amount:
        expenses[category] -= amount
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
