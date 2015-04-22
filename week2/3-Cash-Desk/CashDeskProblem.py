import collections


class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount))


a = Bill(10)
b = Bill(5)
c = Bill(10)

print ("Bill test:")
print (a)
print (str(a))
print (int(a))
print (a == b)
print (a == c)

money_holder = {}
money_holder[a] = 1

print (money_holder)


class BatchBill():

    def __init__(self, bills):
        self.bills = bills

    def __int__(self):
        return self.total()

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(x) for x in self.bills])

    def __getitem__(self, index):
        return self.bills[index]


print ("BatchBill test:")
values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]
print bills
batch = BatchBill(bills)
print (len(batch))
print (batch.total())
for bill in batch:
    print (bill)


class CashDesk():

    def __init__(self):
        self.money = []

    def take_money(self, currency):
        self.money.append(currency)

    def total(self):
        result = 0
        for money in self.money:
            result += int(money)
        return result

    def inspect(self):
        pass


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total())
desk.inspect()
