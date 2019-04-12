import datetime
class item():

    def __init__(self, _receipt__name, _receipt__price, _receipt__taxable):
        self._receipt__name = _receipt__name
        self._receipt__price = _receipt__price
        self._receipt__taxable = _receipt__taxable
    def __str__(self):
        return str(self._receipt__name)
    def getPrice(self):
        return self.__price
    def getTax(self, __tax_rate):
        return self.__price + (self.__price * receipt.__tax_rate)
class receipt():

    def __init__(self, __tax_rate = 0.07, __purchases = []):
        self.__tax_rate = __tax_rate
        self.__purchases = __purchases
    def __str__(self):
        return str(self.__purchases)
    def addItem(self, item):
        self.__purchases.append(item)
    def getItem(self, index):
        return self.__purchases[int(index)]
    def createReceipt(self, subtotal = 0, taxTotal = 0, total = 0):
        print(self.getItem(0))
        print(("-----Receipt " + str(datetime.datetime.now())+"-----"))
        print()
        for x in range(len(self.__purchases)):
            print("{:_<20}{:_>20.2f}".format(self.getItem(x).__name, self.getItem(x).__price))
            subtotal += self.getItem(x).__price
            if (self.getItem(x).__taxable):
                taxTotal += self.getItem(x).__price * self.__tax_rate
        total = subtotal + taxTotal
        print()
        print("{:_<20}{:_>20.2f}".format("Sub Total", subtotal))
        print("{:_<20}{:_>20.2f}".format("Tax", taxTotal))
        print("{:_<20}{:_>20.2f}".format("Total", total))

print('Welcome to receipt creator')
newReceipt = receipt()
end = True
while (end):
    try:
        itemName = input('Enter Item Name: ')
        itemPrice = float(input('Enter Item Price: '))
        itemTaxable = input('Is the item taxable (yes/no): ')
        stop = input('Add another item (yes/no): ')
    except:
        print('Enter a valid item')
        continue
    if (itemTaxable == 'yes'):
        itemTaxable = True
    else:
        itemTaxable = False
    newItem = item(itemName, itemPrice, itemTaxable)
    newReceipt.addItem(newItem)
    if (stop == 'no'):
        end = False
newReceipt.createReceipt()
