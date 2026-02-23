from functools import reduce

def main():

    #our main dictionary
    expenses = {}

    #Ask user for initial expense type
    expense_type = input("Enter expense type (or press Enter to finish): ")

    #while loop to keep feeding answers to our dictionary
    while expense_type != "":
        expense_amount = float(input("Enter amount: "))
        expenses[expense_type] = expense_amount
        expense_type = input("Enter expense type (or press Enter to finish): ")

    #condition if no epenses where entered
    if not expenses:
        print("No expenses entered.")
        return

    #Use the lambda to add the wanted values in our dictionary
    total = reduce(lambda x, y: x + y, expenses.values())

    #Goes through and finds the highest .item/.value pair
    highest = reduce(
        lambda x, y: x if x[1] > y[1] else y,
        expenses.items()
    )

    #Goes through and finds the lowest .item/.value pair
    lowest = reduce(
        lambda x, y: x if x[1] < y[1] else y,
        expenses.items()
    )

    #Display results back to user
    print(f"\nYour Total Expense: ${total:.2f}")
    print(f"The Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"The Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()