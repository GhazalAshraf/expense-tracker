import pytest
from project import add_expense, calculate_total, format_expenses, delete_expense


def test_add_expense():
    expenses = []
    add_expense(expenses, "Coffee", 5)
    assert expenses == [{"description": "Coffee", "amount": 5}]


def test_add_expense_invalid():
    expenses = []
    with pytest.raises(ValueError):
        add_expense(expenses, "Coffee", 0)


def test_calculate_total():
    expenses = [
        {"description": "Coffee", "amount": 5},
        {"description": "Food", "amount": 10}
    ]
    assert calculate_total(expenses) == 15


def test_format_expenses():
    expenses = [
        {"description": "Coffee", "amount": 5}
    ]
    assert format_expenses(expenses) == "1. Coffee: 5.00"
def test_delete_expense():
    expenses = [
        {"description": "Coffee", "amount": 5},
        {"description": "Food", "amount": 10}
    ]

    delete_expense(expenses, 1)

    assert expenses == [
        {"description": "Food", "amount": 10}
    ]
