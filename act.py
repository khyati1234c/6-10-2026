def greet_customer():
    print("welcome to the lemonade stand")
    print("fresh lemonade made just for you")

greet_customer()

price_per_cup=float(input("enter the price of cup in dollars"))
cups_sold=int(input("enter the number of cups sold"))

def calculate_total(price,cups):
    total=price*cups
    return total

total_cost=calculate_total(price_per_cup,cups_sold)

rounded_total=round(total_cost,2)
print("total cost:",rounded_total)

amount_payed=float(input("enter the amount payed by the customer"))

def calculate_change(paid,total):
    change=paid-total
    return change

change_due=calculate_change(amount_payed,rounded_total)
rounded_change=round(change_due,2)

def thankyou_message(cups):
    if cups >=5:
        print("wow such a big order   thankyou for your support")
    else:
        return "thanks for stoping by"

closing_message=thankyou_message(cups_sold)

# PART 12: Print the final lemonade stand receipt

print("")

print("===== LEMONADE STAND RECEIPT =====")

print("Price Per Cup:", price_per_cup)

print("Cups Sold:", cups_sold)

print("Total Cost:", rounded_total)

print("Amount Paid:", amount_paid)

print("Change Due:", rounded_change)

print(closing_message)

print("===================================")