// Initialize budget and limits
let budget = 1500;
let expenses = {
    shopping: 0,
    food: 0,
    academic: 0,
    medical: 0,
};

const limits = {
    shopping: 500,
    food: 300,
    academic: 400,
    medical: 200,
};

// Function to update the expenses list and balance
function updateDisplay() {
    const expenseList = document.getElementById("expenseList");
    expenseList.innerHTML = ""; // Clear existing list

    // Update the expense categories
    for (const category in expenses) {
        const expenseItem = document.createElement("li");
        expenseItem.textContent = `${category.charAt(0).toUpperCase() + category.slice(1)}: $${expenses[category]} (Limit: $${limits[category]})`;
        expenseList.appendChild(expenseItem);
    }

    // Calculate the remaining balance
    const totalExpenses = Object.values(expenses).reduce((sum, expense) => sum + expense, 0);
    const remainingBalance = budget - totalExpenses;

    // Update remaining balance
    document.getElementById("remainingBalance").textContent = remainingBalance;

    // Check budget status
    const statusElement = document.getElementById("status");
    if (remainingBalance < 0) {
        statusElement.textContent = "Over Budget";
        statusElement.classList.add("over-budget");
        statusElement.classList.remove("good-budget");
    } else {
        statusElement.textContent = "Good";
        statusElement.classList.add("good-budget");
        statusElement.classList.remove("over-budget");
    }
}

// Handle Add Expense
document.getElementById("addExpenseForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting the traditional way

    const category = document.getElementById("category").value;
    const amount = parseFloat(document.getElementById("amount").value);

    if (amount <= 0) {
        alert("Amount must be greater than 0.");
        return;
    }

    // Check if adding the expense exceeds the category limit
    if (expenses[category] + amount <= limits[category]) {
        expenses[category] += amount;
    } else {
        alert(`Cannot add expense, limit exceeded for ${category}.`);
    }

    updateDisplay(); // Update the display
});

// Handle Remove Expense
document.getElementById("removeExpenseForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting the traditional way

    const category = document.getElementById("removeCategory").value;
    const amount = parseFloat(document.getElementById("removeAmount").value);

    if (amount <= 0) {
        alert("Amount must be greater than 0.");
        return;
    }

    // Check if the expense exists and is valid for removal
    if (expenses[category] >= amount) {
        expenses[category] -= amount;
    } else {
        alert("Cannot remove more than the current expense.");
    }

    updateDisplay(); // Update the display
});

// Initial display update
updateDisplay();
