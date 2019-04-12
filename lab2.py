import datetime
class item:

    def __init__(self, __name, __price, __taxable):
        self.__name = __name
        self.__price = __price
        self.__taxable = __taxable
    def __str__(self):
        return str(self.__name)
    def getPrice(self):
        return self.__price
    def getTax(self, __tax_rate):
        return self.__price + (self.__price * receipt.__tax_rate)
class receipt:

    def __init__(self, __tax_rate = 0.07, __purchases = []):
        self.__tax_rate = __tax_rate
        self.__purchases = __purchases
    def __str__(self):
        return str(self.__purchases)
    def addItem(self, item):
        self.__purchases.append(item)
    def getItem(self, index):
        return self.__purchases[index]

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
    receipt.addItem(newItem)
    if (stop == 'no'):
        end = False

print("{:-^20}".format("Receipt", str(datetime.datetime.now())))
subtotal = 0
taxTotal = 0
for x in newReceipt.__purchases:
    print("{}{:_>20.2f}".format(receipt[x].__name, newReceipt.getItem(x).__price))
    subtotal += receipt[x].__price
    if (newReceipt.getItem(x).__taxable):
        taxTotal += newReceipt.getItem(x).__price * newReceipt.__tax_rate
total = subtotal + taxTotal
print()
print("{}{:_>20.2f}").format("Sub Total", subtotal)
print("{}{:_>20.2f}").format("Tax", taxTotal)
print("{}{:_>20.2f}").format("Total", total)
