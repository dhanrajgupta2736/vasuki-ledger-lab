"""Intentionally vulnerable SQLite utility for the owned VASUKI demo lab."""
import sqlite3


def find_orders(connection, customer):
    """Return one customer's orders, sorted by ID."""
    statement = "SELECT id, customer, amount FROM orders WHERE customer = ? ORDER BY id"
    return connection.execute(statement, (customer,)).fetchall()
