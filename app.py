from flask import request, render_template
from flask import Flask
from .model import Product
from .calculate import *

app = Flask('__name__')

# add product route
@app.route('/add-product', methods=["GET","POST"])
def addProdcut():

    product = {
        'name': '',
        'sellingPrice': 0,
        'purchasePrice': 0,
        'unitsPurchased': 0,
        'unitsSold':0
    }
    if request.method=="POST":
        
        if request.form['pname'] != '':
            product['name'] = request.form['pname']
        
        if request.form['sp'] != '':
            product['sellingPrice'] = request.form['sp']
        
        if request.form['price'] != '':
            product['purchasePrice'] = request.form['price']

        if request.form['purchase'] != '':
            product['unitsPurchased'] = request.form['purchase']

        if request.form['sold'] != '':
            product['unitsSold'] = request.form['sold']

        p = Product(
            product['name'],
            product['sellingPrice'],
            product['purchasePrice'],
            product['unitsPurchased'],
            product['unitsSold']
        )

        product_list.append(p)

    return render_template('add_product_form.html')

@app.route('/update-commission', methods=["GET","POST"])
def updateCommissionPercentage():

    if request.method == "POST":
        position = request.form.get("positions")
        employeeCommissionPercent[position] = request.form["commission"]

    return render_template('change_commission_value.html')

@app.route('/sales-profit-report', methods=["GET"])
def renderSalesProfitReport():

    commission_values = dict()

    profit_per_sale = dict()

    if len(product_list) != 0:

        for pos in positions:
            commission_values[pos] = list()
            for item in product_list:
                commission_values[pos].append(commissionToEachSale(employeeCommissionPercent[pos], item))


        for product in product_list:
            profit_per_sale[product.name] = (product.sellingPrice*product.unitsSold) - (product.unitsPurchased*product.purchasePrice)

    total_commission=totalCommissionPercent()

    net_profit = calculateNetProfit()

    return (
                "sales_and_commission_report.html", 
                {
                    'commission_values': commission_values, 
                    'profit_per_sale': profit_per_sale, 
                    'total_commission': total_commission,
                    'employeeCommissionPercent': employeeCommissionPercent,
                    'product_list': product_list,
                    'positions': positions,
                    'net_profit': net_profit 
                }
            )

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=true)