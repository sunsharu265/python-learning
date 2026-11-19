# eCommerce Example - a small online shop

This folder shows how **all the OOPS concepts work together** in one real program,
like a tiny Amazon or Flipkart.

## How to run

From the `pythonLearning` folder:

```
python OOPS/ecommerce/main.py
```

## The files (read them in this order)

| File | Class | Real life meaning |
|------|-------|-------------------|
| `product.py` | `Product`, `Electronics`, `Clothing`, `Grocery` | The things we sell |
| `cart.py` | `Cart` | The shopping basket |
| `customer.py` | `Customer` | The person who shops |
| `payment.py` | `Payment`, `UPIPayment`, `CardPayment`, `CashOnDelivery` | Ways to pay |
| `order.py` | `Order` | One purchase, with its bill and status |
| `main.py` | - | The story: shop -> cart -> order -> delivery |

## How the classes are connected

```
Customer  --HAS-->  Cart  --HAS-->  Products
    |
    +--HAS--> Orders  --USES-->  Payment

Product  <--IS-A--  Electronics, Clothing, Grocery
Payment  <--IS-A--  UPIPayment, CardPayment, CashOnDelivery
```

## Where each OOPS concept is used

| Concept | Lesson | Where to find it here |
|---------|--------|-----------------------|
| Class and object | 1 | Every file. `phone`, `saree`, `priya` in `main.py` are objects |
| Constructor and `self` | 2 | Every `__init__` |
| Class variable | 3 | `Product.total_products`, `Order.next_order_number`, `CashOnDelivery.max_amount` |
| Encapsulation | 4 | `Product.__stock`, `Customer.__password`, `Order.__status` |
| Inheritance | 5 | `Electronics(Product)`, `UPIPayment(Payment)` |
| Polymorphism | 6 | `product.final_price()` in `cart.py`, `payment.pay()` in `order.py` |
| Abstraction | 7 | `Payment` in `payment.py` is an abstract class |
| Special methods | 8 | `Product.__str__`, `Order.__str__`, `Cart.__len__` |
| Composition | 9 | Customer has a Cart, Cart has Products, Order has a Customer |

## Questions to discuss while teaching

1. Why is `__stock` private in `Product`? What could go wrong if it was public?
2. `Grocery` has no `discount_percent()` method. Then why does `rice.final_price()` still work?
3. In `order.py`, the `place()` method never checks if the payment is UPI or card. How does it work?
4. What happens if we write `Payment()` in `main.py`? Try it.
5. Why does each customer get their own `Cart()` inside `__init__`, and not one cart as a class variable?

## Practice assignments

### Level 1 - small changes

1. Add 3 new products of your choice in `main.py` and print the product list.
2. Create a third customer with your own name. Add 2 products to the cart and place an order with UPI.
3. Change the `Clothing` discount from 20% to 30%. Run the program and see which prices change.
4. Change the free delivery limit in `Order` from Rs.500 to Rs.1000 and check the bill.

### Level 2 - new methods

5. Add a method `update_quantity(product_name, new_quantity)` to `Cart`.
6. Add a method `total_items()` to `Cart` that returns the total quantity
   (2 rice + 5 notebooks = 7).
7. Add a method `change_password(old_password, new_password)` to `Customer`.
   It should change the password only if the old password is correct.
8. Add a method `total_spent()` to `Customer` that adds the grand total of all
   orders whose status is not "Cancelled".

### Level 3 - new classes

9. Add a new product type `Book(Product)` with an `author` attribute and a 5% discount.
10. Add a new payment type `WalletPayment(Payment)` with a `balance`. Payment fails
    when the balance is too low; otherwise the balance is reduced.
11. Add a new product type `Footwear(Product)` with `shoe_size`.
12. Create a class `Coupon` with `code` and `discount_percent`. Add a method
    `apply_coupon(coupon)` to `Order` that reduces the grand total.

### Level 4 - mini project

13. Create a class `Shop` in a new file `shop.py`. It HAS a list of products and a
    list of customers. Add methods `add_product()`, `register_customer()`,
    `search_product(name)` and `show_products_below(price)`.
14. Add a `Review` class (customer, rating 1 to 5, comment). A `Product` HAS a list
    of reviews. Add `add_review()` and `average_rating()` to `Product`.
    Do not allow a rating outside 1 to 5.
15. Make `main.py` interactive using `input()`, like `hotelBillingEx.py`:
    show a menu (1. View products  2. Add to cart  3. View cart  4. Place order  5. Exit).
