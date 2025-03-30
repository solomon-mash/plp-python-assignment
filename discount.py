def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  

price = float(input("Enter price of item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percentage)

# Display the result
if final_price == price:
    print(f"No discount applied. The final price is: ${final_price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
