"""
analysis.py
------------
Task 4: Programming logic — functions, loops, conditionals and arrays.

This module covers KM-05 topics: Programming Basics (data types,
conditionals, loops, arrays/lists, functions) and Introduction to
Algorithms.

IMPORTANT: For this file, use plain Python (for-loops, if/else,
lists and dictionaries) even where pandas could do it in one line.
The point of this section is to demonstrate the programming
fundamentals from KM-05, not just pandas shortcuts.
"""


def total_sales_records(sales_rows: list) -> int:
    """
    Count how many sales records there are, using a loop (not len()
    directly on the list — practise the loop!).

    Args:
        sales_rows: a list of dictionaries, one per sale, e.g.
            [{"product_id": "P001", "quantity": 2, ...}, ...]

    Returns:
        the total number of records, as an integer, counted with a loop.
    """
    # TODO:
    #   count = 0
    #   for row in sales_rows:
    #       count += 1
    #   return count
    raise NotImplementedError


def low_stock_alert(products_rows: list, threshold: int = 5) -> list:
    """
    Return a list of product names where in_stock is False, OR where
    you decide a product should be flagged (use a conditional / if
    statement here — this is the KM-05 "conditionals" checkpoint).

    Args:
        products_rows: list of dictionaries, one per product
        threshold: (optional) use this if you extend the dataset with
            a stock-count column later

    Returns:
        a list of product_name strings that need re-ordering.
    """
    # TODO:
    #   alerts = []
    #   for product in products_rows:
    #       if product["in_stock"] is False:   # or == "False", check your data type
    #           alerts.append(product["product_name"])
    #   return alerts
    raise NotImplementedError


def monthly_sales_trend(sales_rows: list) -> dict:
    """
    Build a dictionary that maps each month (e.g. "2026-01") to the
    total quantity sold that month, using a loop.

    Args:
        sales_rows: list of dictionaries, one per sale, each with a
            "sale_date" key already cleaned to "YYYY-MM-DD" format
            and a "quantity" key (as an int)

    Returns:
        a dict like {"2026-01": 143, "2026-02": 97}

    TODO:
        trend = {}
        for row in sales_rows:
            month = row["sale_date"][:7]        # "YYYY-MM"
            if month in trend:
                trend[month] += row["quantity"]
            else:
                trend[month] = row["quantity"]
        return trend
    """
    raise NotImplementedError


def classify_transaction_size(quantity: int) -> str:
    """
    A small function that demonstrates if / elif / else.

    Rules:
        quantity >= 5   -> "Bulk"
        quantity >= 2   -> "Multiple"
        quantity == 1   -> "Single"
        anything else   -> "Invalid"

    TODO: implement the if / elif / else chain above.
    """
    raise NotImplementedError


def average_basket_size(sales_rows: list) -> float:
    """
    Calculate the average quantity per sale across ALL sales, using a
    loop to sum quantities and a loop (or len()) to count records.

    Returns:
        a float rounded to 2 decimal places.

    TODO:
        total = 0
        for row in sales_rows:
            total += row["quantity"]
        return round(total / len(sales_rows), 2)
    """
    raise NotImplementedError
