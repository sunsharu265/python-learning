from seller import Seller
from customer import Customer

sellerObj = Seller()

# List seller data
print(sellerObj.showSellerList())
print("customer list")

# Add SellerData
sellerObj.getSeller()
sellerObj.showSellerList()

print(sellerObj.showSellerList())
print(Customer.customer.showlist())