class Item:
    def __init__(self,price,discount_strategy=None):
        self.price=price
        self.discount_strategy=discount_strategy
        
    def __str__(self):
        print("Price before discount is ",self.price)
        print("Price after discount is ",self.price_after_discount())
        return "None"
        
    def price_after_discount(self):
        if self.discount_strategy is None:
            discount =0
        elif self.discount_strategy:
            discount =self.discount_strategy(self)
            
        return self.price - discount
    
    
    
def ten_percent_discount(self):
    return self.price*0.10

def mega_discount(self):
    return self.price *0.50

if __name__=="__main__":
    print(Item(2000))
    print(Item(2000,discount_strategy=ten_percent_discount))
    print(Item(2000,discount_strategy=mega_discount))
    
 
                 