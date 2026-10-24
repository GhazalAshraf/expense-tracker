import csv
from pathlib import Path

import pandas as pd
import streamlit as st


FILE = Path("expenses.csv")


def load_expenses():
    if not FILE.exists():
        return []

    expenses = []
    with FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(
                {
                    "description": row["description"],
                    "amount": float(row["amount"]),
                }
            )
    return expenses


def save_expenses(expenses):
    with FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "amount"])
        writer.writeheader()
        writer.writerows(expenses)


st.set_page_config(page_title="SpendWise", page_icon="💰")
st.title("💰 SpendWise")
st.caption("End-to-End Personal Expense Tracker")
st.write("Add, view, total, and delete your everyday expenses.")

expenses = load_expenses()

with st.form("add_expense"):
    description = st.text_input("Expense description")
    amount = st.number_input("Amount", min_value=0.0, step=0.50, format="%.2f")
    add_button = st.form_submit_button("Add Expense")

if add_button:
    if description.strip() and amount > 0:
        expenses.append(
            {
                "description": description.strip(),
                "amount": float(amount),
            }
        )
        save_expenses(expenses)
        st.success("Expense added successfully!")
        st.rerun()
    else:
        st.warning("Please enter a description and an amount greater than 0.")

st.subheader("Saved Expenses")

if expenses:
    dataframe = pd.DataFrame(expenses)
    dataframe.index = dataframe.index + 1
    dataframe.index.name = "No."

    st.dataframe(dataframe, use_container_width=True)

    total = sum(expense["amount"] for expense in expenses)
    st.metric("Total Expenses", f"€{total:,.2f}")

    delete_number = st.selectbox(
        "Select expense to delete",
        range(1, len(expenses) + 1),
        format_func=lambda number: (
            f"{number}. {expenses[number - 1]['description']} "
            f"— €{expenses[number - 1]['amount']:.2f}"
        ),
    )

    if st.button("Delete Expense"):
        expenses.pop(delete_number - 1)
        save_expenses(expenses)
        st.success("Expense deleted!")
        st.rerun()

else:
    st.info("No expenses added yet.")
