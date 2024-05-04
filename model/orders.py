from datetime import datetime
from typing import List, NamedTuple

class Order(NamedTuple):
    customerName: str
    newCustomer:bool
    price: float
    currency: str
    productCategories: List[str]
    salesType: str
    phoneNumber: str
    quantity: int
    orderName: str
    customerCity: str
    customerCountry: str
    cityLatitude: float
    cityLongitude: float
    countryLatitude: float
    countryLongitude: float
    entryTime: datetime

    def to_dict(self) -> dict:
        return {
            'customerName': self.customerName,
            'newCustomer':self.newCustomer,
            'price': self.price,
            'currency': self.currency,
            'productCategories': self.productCategories,
            'salesType': self.salesType,
            'phoneNumber': self.phoneNumber,
            'quantity': self.quantity,
            'orderName': self.orderName,
            'customerCity': self.customerCity,
            'customerCountry': self.customerCountry,
            'cityLatitude': self.cityLatitude,
            'cityLongitude': self.cityLongitude,
            'countryLatitude': self.countryLatitude,
            'countryLongitude': self.countryLongitude,
            'entryTime': self.entryTime.isoformat(), 
        }
