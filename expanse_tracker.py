# ==================================
#       SIMPLE EXPENSE TRACKER
# ==================================

expenses = []


# Add Expense
def add_expense():

    name = input("Enter expense name: ")

    amount = float(input("Enter amount: ₹"))

    category = input("Enter category: ")

    date = input("Enter date (DD-MM-YYYY): ")

    expense_id = len(expenses) + 1

    expense = {
        "id": expense_id,
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print("\n✅ Expense added successfully!")


# Show Expenses
def show_expenses():

    if len(expenses) == 0:

        print("\nNo expenses added yet.")

    else:

        print("\n========== YOUR EXPENSES ==========")

        for expense in expenses:

            print("ID       :", expense["id"])
            print("Name     :", expense["name"])
            print("Amount   : ₹", expense["amount"])
            print("Category :", expense["category"])
            print("Date     :", expense["date"])
            print("-----------------------------------")


# Calculate Total
def show_total():

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    print("\n💰 Total Expense: ₹", total)
# ----------------------------------
# Search Expense by Category
# ----------------------------------

def search_expense():

    if len(expenses) == 0:

        print("\nNo expenses available.")

        return

    search_category = input(
        "\nEnter category to search: "
    ).lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for expense in expenses:

        if expense["category"].lower() == search_category:

            print("ID       :", expense["id"])
            print("Name     :", expense["name"])
            print("Amount   : ₹", expense["amount"])
            print("Category :", expense["category"])
            print("Date     :", expense["date"])
            print("-----------------------------------")

            found = True

    if found == False:

        print("❌ No expense found in this category.")

# Main Menu
while True:

    print("\n==============================")
    print("       EXPENSE TRACKER")
    print("==============================")

    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("1. Add Expense")

    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Search by Category")
    print("7. Exit")
  

    choice = input("Enter your choice: ")


    if choice == "1":

        add_expense()


    elif choice == "2":

        show_expenses()


    elif choice == "3":

        show_total()


    elif choice == "4":

        print("\nThank you for using Expense Tracker! 👋")

        break
    elif choice == "5":

     search_expense()


      elif choice == "6":

     print("\nThank you for using Expense Tracker! 👋")

     break

      else:

        print("\n❌ Invalid choice. Please try again.")