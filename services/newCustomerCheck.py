from utils.database import dBConnection

def newCustomerCheck(customer_name, phone_number):
    db,client,collection=dBConnection()
    existingCustomer= collection.find_one({"customerName": customer_name, "phoneNumber": phone_number})
    return existingCustomer is not None