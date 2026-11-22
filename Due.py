def calculate_change():
    total_bill = 2.50
    amount_paid = 4.00

    change = amount_paid - total_bill
    return change

result = calculate_change()
print("Change to be returned: $", result)