menu = {
    "DOSA": 95,
    "IDLY": 50,
    "PONGAL": 80,
    "POORI": 60,
    "VADA" : 30
}

total_bill = 0

print("--- WELCOME TO THE ROYAL'S HOTEL ---")
print("DOSA: 95 | IDLY: 50 | PONGAL: 80 | POORI: 60 | VADA: 30")

while True:
    print("-" * 30)
    item = input("Enter item name (or type 'exit' to finish): ")

    if item.lower() == "exit":
        break
    
    item = item.upper()

    if item in menu:
        qty = input("Enter quantity for '" + item + "': ")
        qty = int(qty)
              
        price = menu[item]
        cost = price * qty
        
        total_bill = total_bill + cost
        print("Added to bill. Current Total: " + str(total_bill))
    else:
        print("Invalid item! Please check the spelling.")

print("-" * 30)
print("FINAL BILL AMOUNT: " + str(total_bill))
print("Thank you for visiting ROYAL’S HOTEL!")
print("Be Royal and Feel Royal ")
print("-" * 30)
