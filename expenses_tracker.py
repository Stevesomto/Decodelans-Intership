#First of all i need to create an empty list to store my expenses
total = []

# Then i created a while loop to keep asking the user for expenses 
# until they choose to quit
while True:
    new_expenses = input("Enter an expense (or type 'q' to quit): ")
    if new_expenses.lower() == 'q':
        break
    
# Then i use try and except to handle any errors that may occur when 
# converting the input to a float
    try:
        total = total + [float(new_expenses)]
    except ValueError:
        print("Please enter a valid number.")

# Finally, i print the total expenses in all entry made by the user. 
    print(f"Current total expenses: {sum(total)}")