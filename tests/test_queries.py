"""Local dummy data proves the bug and preserves ordinary query behavior."""
import sqlite3
import pytest
from queries import find_orders


@pytest.fixture
def connection():
    db=sqlite3.connect(':memory:')
    db.execute('CREATE TABLE orders (id INTEGER, customer TEXT, amount INTEGER)')
    db.executemany('INSERT INTO orders VALUES (?, ?, ?)',[(1,'Alice',100),(2,'Bob',200),(3,'Alice',50),(4,"O'Reilly",75)])
    yield db
    db.close()


@pytest.mark.parametrize('customer,ids',[('Alice',[1,3]),('Bob',[2]),('Carol',[]),('',[]),('Ali',[]),('alice',[])])
def test_exact_customer_lookup(connection,customer,ids):
    assert [row[0] for row in find_orders(connection,customer)] == ids


def test_order_amount_and_ordering_preserved(connection):
    assert find_orders(connection,'Alice') == [(1,'Alice',100),(3,'Alice',50)]


@pytest.mark.parametrize('customer',["' OR 1=1 --", "Alice' OR '1'='1"])
def test_security_input_cannot_expand_query_scope(connection,customer):
    assert find_orders(connection,customer)==[]


def test_security_quoted_customer_is_a_literal(connection):
    assert find_orders(connection,"O'Reilly")==[(4,"O'Reilly",75)]
