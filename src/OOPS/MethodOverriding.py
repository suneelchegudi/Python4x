class Mobile:
    def __init__(self, price, modelNo):
        self.price = price
        self.modeNo = modelNo
    def discountPrice(self):
        return self.price-self.price*(1/10)

class Iphone(Mobile):
    def __init__(self,price,modelNo):
        Mobile.__init__(self, price, modelNo)
    def discountPrice(self, discount):
        return self.price-self.price*(1/discount)

class Samsung(Mobile):
    def __init__(self,price,modelNo):
        Mobile.__init__(self, price, modelNo)
    # def discountPrice(self):
    #     return self.price-self.price*(1/discount)


Iphone_Object = Iphone(10000,101)
print(Iphone_Object.discountPrice(15))

samsung_objject = Samsung(10000,102)
print(samsung_objject.discountPrice())