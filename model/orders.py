from datetime import datetime
from typing import List, NamedTuple

class Order(NamedTuple):
    price: float
    currency: str
    product_categories: List[str]
    sales_type: str
    quantity: int
    product_name: str
    city: str
    country: str
    phone_number: str
    entry_time: datetime

    def to_dict(self) -> dict:
        return {
            'price': self.price,
            'currency': self.currency,
            'product_categories': self.product_categories,
            'sales_type': self.sales_type,
            'quantity': self.quantity,
            'product_name': self.product_name,
            'city': self.city,
            'country': self.country,
            'phone_number': self.phone_number,
            'entry_time': self.entry_time.isoformat(),  # Use ISO 8601 format for datetime
        }
