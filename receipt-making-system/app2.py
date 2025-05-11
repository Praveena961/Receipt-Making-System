from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_receipt', methods=['POST'])
def generate_receipt():
    customer_name = request.form['customer_name']
    items = request.form.getlist('item[]')
    prices = request.form.getlist('price[]')
    quantities = request.form.getlist('quantity[]')

    receipt_items = []
    total = 0
    for item, price, quantity in zip(items, prices, quantities):
        price = float(price)
        quantity = int(quantity)
        item_total = price * quantity
        total += item_total
        receipt_items.append((item, price, quantity, item_total))

    return render_template('receipt.html', customer_name=customer_name, receipt_items=receipt_items, total=total)

if __name__ == '__main__':
    app.run(debug=True)
