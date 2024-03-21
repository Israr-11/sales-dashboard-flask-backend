class Order:
    def __init__(self, price, currency, product_categories, sales_type,quantity, product_name,city, country, entry_time):
        self.price=price
        self.curreny=currency
        self.product_categories=product_categories
        self.sales_type=sales_type
        self.quantity=quantity
        self.product_name=product_name
        self.city=city
        self.country=country
        self.entry_time=entry_time

    
    def to_dict(self):
        return{
            'price':self.price,
            'currency':self.curreny,
            'product_categories':self.product_categories,
            'sales_type':self.sales_type,
            'quantity':self.quantity,
            'product_name':self.product_name,
            'city':self.city,
            'country':self.country,
            'entry_time':self.entry_time
        }