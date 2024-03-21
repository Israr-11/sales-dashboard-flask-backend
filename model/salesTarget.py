class SalesTarget:
    def __init__(self, month, year,sales_target):
        self.month=month
        self.year=year
        self.sales_target=sales_target


    
    def to_dict(self):
        return{
            'month':self.month,
            'year':self.year,
            'sales_target':self.sales_target
        }


    