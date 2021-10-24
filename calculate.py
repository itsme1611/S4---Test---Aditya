from .model import Product

positions = ['Sales Rep', 'Sales Manager', 'General Manager', 'VP Sales']

# Employee commission dictionary map
employeeCommissionPercent = {
    'Sales Rep': 5,
    'Sales Manager': 5,
    'General Manager': 8,
    'VP Sales': 9
}

# list of products in the grocery shop
product_list= []

# Calculate Net revenue
def getRevenue():
    
    revenue = 0

    if len(product_list) != 0:
        for product in product_list:
            revenue += product.getProductSale()
    
    return revenue

# Caluculate total expenses before the selling the products
def getTotalExpenses():
    
    expenses=0

    if len(product_list) != 0:
        for product in product_list:
            expences += product.getPurchaseCost()
    
    return expenses

# Calculate net profit to the owner
def calculateNetProfit():
    net_profit=0

    # Net Profit = (Total Revenue - Expenses)
    net_profit = getRevenue() - getTotalExpenses()

    return net_profit

# Calculate profit margin
def calculateProfitMargin():
    
    profit_margin = 0

    # net profit margin = ( net profit / total revenue ) x 100

    profit_margin = (calculateNetProfit()/getRevenue())*100

    return profit_margin

# Calculate % of commission for employee position based on net profit
def commissionToEmployee(commissionPercentage):
    employee_commission = 0

    employee_commission = (commissionPercentage*calculateNetProfit())/100
    return employee_commission

# commission to each product sale
def commissionToEachSale(commissionPercent, product):
    commissionToEmployee = 0

    commissionToEmployee = (commissionPercent*product.getProductSale())/100

    return commissionToEmployee

# Calculate total commission value
def totalCommissionValue():
    
    total_commission_value = 0

    for pos in positions:
        total_commission_value += commissionToEmployee(employeeCommissionPercent[pos]) 

    total_commission_value

# Calculate total % of commissions
def totalCommissionPercent():
    
    totalPercentOfCommission = 0

    totalPercentOfCommission = (totalCommissionValue()/calculateProfitMargin())*100

# Caluculate profit to the company
def companyProfit():

    #Profit to the Company = Net Profit – Total Commission Value  
    return (calculateNetProfit() - totalCommissionValue())
