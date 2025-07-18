import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Initialize or load data
try:
    df = pd.read_csv("expenses.csv", parse_dates=["Date"])
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])

budget = 0

def add_expense():
    category = input("Enter category (e.g., Food, Rent, Travel): ")
    amount = float(input("Enter amount: ₹"))
    date = datetime.now()
    global df
    df = pd.concat([df, pd.DataFrame([[date, category, amount]], columns=df.columns)], ignore_index=True)
    print("✅ Expense added.")

def set_budget():
    global budget
    budget = float(input("Set your monthly budget: ₹"))
    print(f"✅ Budget set to ₹{budget}")

def show_summary():
    print("\n📊 Expense Summary:")
    print(df.groupby("Category")["Amount"].sum())
    print(f"\n💰 Total Spent: ₹{df['Amount'].sum():.2f}")
    if budget:
        print(f"📉 Remaining Budget: ₹{budget - df['Amount'].sum():.2f}")

def visualize():
    if df.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(10, 5))

    # Pie Chart
    plt.subplot(1, 2, 1)
    df.groupby("Category")["Amount"].sum().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Expense Distribution")

    # Bar Chart
    plt.subplot(1, 2, 2)
    df["Month"] = df["Date"].dt.to_period("M")
    monthly = df.groupby("Month")["Amount"].sum()
    monthly.plot(kind="bar", color="skyblue")
    plt.title("Monthly Expenses")
    plt.ylabel("Amount (₹)")

    plt.tight_layout()
    plt.show()

def save_data():
    df.to_csv("expenses.csv", index=False)
    print("💾 Data saved to expenses.csv")

def menu():
    while True:
        print("\n📌 Smart Expense Tracker")
        print("1. Add Expense")
        print("2. Set Budget")
        print("3. Show Summary")
        print("4. Visualize Expenses")
        print("5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            set_budget()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            visualize()
        elif choice == "5":
            save_data()
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
