def create_sales_calculator(percent_discount):
    def calculator(price):
        return price * (1 - (percent_discount / 100))

    return calculator

twenty_percent_off = create_sales_calculator(20)
ten_percent_off = create_sales_calculator(10)
clearance_price = create_sales_calculator(50)
thirty_five_percent_off = create_sales_calculator(35)

print(twenty_percent_off(100))
print(ten_percent_off(100))
print(clearance_price(100))
print(thirty_five_percent_off(100))