from abc import ABC, abstractmethod

# Interface for Budget Tracker (Abstract Base Class)
class BudgetTrackerInterface(ABC):
    
    @abstractmethod
    def add_expense(self, category, amount):
        pass

    @abstractmethod
    def remove_expense(self, category, amount):
        pass

    @abstractmethod
    def view_expenses(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def check_category_limit(self, category):
        pass


# Budget Tracker Implementation
class BudgetTracker(BudgetTrackerInterface):
    
    def __init__(self, initial_budget):
        self.total_budget = initial_budget
        self.expenses = {
            'shopping': 0,
            'food': 0,
            'academic': 0,
            'medical' : 0,
        }
        # Set category limits
        self.limits = {
            'shopping': 500,  # Limit for shopping
            'food': 300,      # Limit for food
            'academic': 400,  # Limit for academic expenses
            'medical' : 200,  # Limit for medical expenses
        }

    def add_expense(self, category, amount):
        """Add an expense to a specific category, ensuring it does not exceed the limit"""
        if category not in self.expenses:
            print(f"Invalid category: {category}")
            return

        if amount < 0:
            print("Expense amount cannot be negative.")
            return
        
        if self.expenses[category] + amount > self.limits[category]:
            print(f"Error: Adding {amount} exceeds the limit for {category} which is {self.limits[category]}.")
        else:
            self.expenses[category] += amount
            print(f"Added {amount} to {category}. Total {category} expenses: {self.expenses[category]}")

    def remove_expense(self, category, amount):
        """Remove an expense from a specific category"""
        if category in self.expenses and self.expenses[category] >= amount:
            self.expenses[category] -= amount
            print(f"Removed {amount} from {category}. Total {category} expenses: {self.expenses[category]}")
        else:
            print("Invalid amount or category.")

    def view_expenses(self):
        """View all expenses in each category"""
        if not any(self.expenses.values()):
            print("No expenses yet.")
        else:
            print("Expenses by Category:")
            for category, amount in self.expenses.items():
                print(f"{category.capitalize()}: ${amount} (Limit: ${self.limits[category]})")

    def check_balance(self):
        """Check remaining budget"""
        total_expenses = sum(self.expenses.values())
        balance = self.total_budget - total_expenses
        print(f"Total Budget: ${self.total_budget}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Remaining Balance: ${balance}")

    def check_category_limit(self, category):
        """Check if a specific category has exceeded its limit"""
        if category in self.expenses:
            remaining_limit = self.limits[category] - self.expenses[category]
            print(f"Remaining limit for {category}: ${remaining_limit}")
        else:
            print("Invalid category.")


# Example of using the BudgetTracker class
def main():
    print("Welcome to Budget Tracker with Interface!")

    # Create a budget tracker with an initial budget
    my_budget = BudgetTracker(1000)  # starting budget of $1000

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Check Balance")
        print("5. Check Category Limit")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter the expense category (shopping, food, academic): ").lower()
            amount = float(input("Enter the amount spent: "))
            my_budget.add_expense(category, amount)
        elif choice == '2':
            category = input("Enter the expense category (shopping, food, academic): ").lower()
            amount = float(input("Enter the amount to remove: "))
            my_budget.remove_expense(category, amount)
        elif choice == '3':
            my_budget.view_expenses()
        elif choice == '4':
            my_budget.check_balance()
        elif choice == '5':
            category = input("Enter the category to check limit (shopping, food, academic): ").lower()
            my_budget.check_category_limit(category)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
