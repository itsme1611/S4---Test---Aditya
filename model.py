class Product:

    def __init__(self, name='NA', sp= 0, price= 0, purchase=0,soldUnits=0):
        self.name = name
        self.sellingPrice = sp
        self.purchasePrice = price
        self.unitsPurchased = purchase
        self.unitsSold = soldUnits

    # calculate each product revenue 
    def getProductSale(self):
        # Net product sale = (number of units sold * selling price)
        return (self.unitsSold*self.sellingPrice)

    # calculate purchase cost for each product 
    def getPurchaseCost(self):
        return (self.unitsPurchased*self.purchasePrice)