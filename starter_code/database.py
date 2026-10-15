"""
database.py
------------
Task 3: Build a relational database from your cleaned data.

This module covers KM-04 topics: Introduction to Databases (DBMS,
components, characteristics) and Structured Query Language (SQL).

You will use Python's built-in `sqlite3` module — no extra install
needed. SQLite stores the whole database in a single file, which makes
it perfect for a student project (and easy to include as evidence).

By the end of this file you must be able to:
  1. Create a database file (store.db) with two related tables.
  2. Insert your cleaned data into those tables.
  3. Run at least FIVE meaningful SQL queries against the data,
     including at least one JOIN and one aggregation (SUM, COUNT, AVG).
"""

import sqlite3


def get_connection(db_path: str = "store.db") -> sqlite3.Connection:
    """
    Open (and create, if needed) the SQLite database file.

    Returns:
        an open sqlite3.Connection
    """
    return sqlite3.connect(db_path)


def create_tables(conn: sqlite3.Connection) -> None:
    """
    Create the `products` and `sales` tables if they don't already exist.

    Design requirements (this IS the relational-database design task —
    think about primary keys and foreign keys, covered in KM-04 KT04):

      products
        - product_id   TEXT, PRIMARY KEY
        - product_name TEXT, NOT NULL
        - category     TEXT
        - unit_price   REAL

      sales
        - sale_id        TEXT, PRIMARY KEY
        - product_id     TEXT, FOREIGN KEY references products(product_id)
        - quantity       INTEGER
        - sale_date      TEXT   (store as 'YYYY-MM-DD')
        - payment_method TEXT
        - customer_type  TEXT
        """

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id   TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category     TEXT,
         unit_price   REAL,
            in_stock     INTEGER
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id        TEXT PRIMARY KEY,
            product_id     TEXT,
            quantity       INTEGER,
            sale_date      TEXT,
            payment_method TEXT,
            customer_type  TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );
    """)

    conn.commit()


def insert_products(conn: sqlite3.Connection, products_df) -> None:
    """
    Insert every row of the cleaned products DataFrame into the
    products table.

    """

    # Clear the table first so re-running main.py doesn't duplicate rows.
    conn.execute("DELETE FROM products;")

    # pandas writes all rows in one efficient batch.
    products_df.to_sql("products", conn, if_exists="append", index=False)

    conn.commit()


def insert_sales(conn: sqlite3.Connection, sales_df) -> None:
    """
    Insert every row of the cleaned sales DataFrame into the sales table.
    """

    # Clear the table first so re-running main.py doesn't duplicate rows.
    conn.execute("DELETE FROM sales;")
    sales_df.to_sql("sales", conn, if_exists="append", index=False)
    conn.commit()


# ---------------------------------------------------------------------
# SQL QUERIES — write at least FIVE for your project.
# Three are started for you below; you must complete them and add TWO
# more of your own that answer a business question you find interesting.
# ---------------------------------------------------------------------

def query_total_revenue_per_product(conn: sqlite3.Connection):
    """
    Return each product's name and its total revenue
    (quantity * unit_price, summed across all its sales),
    highest revenue first.
    """
    sql = """
        SELECT p.product_name,
               SUM(s.quantity * p.unit_price) AS total_revenue
        FROM sales s
        JOIN products p ON p.product_id = s.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_revenue DESC
    """
    return conn.execute(sql).fetchall()


def query_best_selling_product(conn: sqlite3.Connection):
    """
    Return the single product with the highest total quantity sold.
    """
    sql = """
        SELECT p.product_name,
               SUM(s.quantity) AS total_units
        FROM sales s
        JOIN products p ON p.product_id = s.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_units DESC
        LIMIT 1
    """
    return conn.execute(sql).fetchall()


def query_sales_by_payment_method(conn: sqlite3.Connection):
    """
    Return the number of sales transactions per payment_method.
    """
    sql = """
        SELECT payment_method,
               COUNT(*) AS num_transactions
        FROM sales
        GROUP BY payment_method
        ORDER BY num_transactions DESC
    """
    return conn.execute(sql).fetchall()


def query_custom_one(conn: sqlite3.Connection):
    """
    Business question: which product category earns the most revenue?

    Joins sales to products, multiplies quantity by unit_price per
    row, groups by category, and orders categories by total revenue.
    This tells Thabo which section of his shop is actually paying
    the bills.
    """
    sql = """
        SELECT p.category,
               SUM(s.quantity * p.unit_price) AS category_revenue,
               COUNT(*) AS num_sales
        FROM sales s
        JOIN products p ON p.product_id = s.product_id
        GROUP BY p.category
        ORDER BY category_revenue DESC
    """
    return conn.execute(sql).fetchall()


def query_custom_two(conn: sqlite3.Connection):
    """
    Business question: do Regular customers buy more units per basket
    than Walk-in customers?

    Uses a WHERE filter to exclude Unknown customer types, then
    AVG() to compare the two groups. Helps Thabo decide whether a
    loyalty programme for Regulars would be worth the effort.
    """
    sql = """
        SELECT customer_type,
               COUNT(*) AS num_transactions,
               AVG(quantity) AS avg_units_per_basket
        FROM sales
        WHERE customer_type != 'Unknown'
        GROUP BY customer_type
        ORDER BY avg_units_per_basket DESC
    """
    return conn.execute(sql).fetchall()
