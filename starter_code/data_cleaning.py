"""
data_cleaning.py
-----------------
Task 2: Load the raw CSV files and clean them.

This module covers KM-04 topics: Introduction to Data (data types,
errors of omission) and Data in Spreadsheets.

The raw files in data/products.csv and data/sales.csv contain REAL
data-quality problems on purpose, so you get practice fixing them:

  products.csv issues to find and fix:
    - Some products are missing a unit_price
    - One product is missing its product_name
    - Category text is inconsistently capitalised (e.g. "beverages" vs "Beverages")
    - One exact duplicate row

  sales.csv issues to find and fix:
    - sale_date is written in at least FOUR different formats
    - Some rows have a missing sale_date (an error of omission)
    - Some rows have a missing quantity
    - Some rows have a missing payment_method
    - A few rows reference a product_id that does not exist in products.csv
    - One exact duplicate row

You must handle every one of these before the data moves on to the
database in database.py. Document the decisions you make (e.g. "rows
with a missing sale_date were dropped because we cannot analyse sales
trends without a date") in your README findings section.
"""

import pandas as pd


def load_raw_data(products_path: str, sales_path: str):
    """
    Load the two raw CSV files into pandas DataFrames.

    Args:
        products_path: file path to products.csv
        sales_path: file path to sales.csv

    Returns:
        (products_df, sales_df) tuple of pandas DataFrames, UNCLEANED.
    """
    # TODO:
    #   1. Use pd.read_csv() to load both files.
    #   2. Return them as a tuple: (products_df, sales_df)
    raise NotImplementedError


def clean_products(products_df: "pd.DataFrame") -> "pd.DataFrame":
    """
    Clean the products DataFrame.

    Must handle:
        - Missing unit_price (decide: drop the row, or fill with a sensible
          value? Justify your choice in the README.)
        - Missing product_name (a product with no name is not usable data —
          what should happen to that row?)
        - Inconsistent category capitalisation (standardise to Title Case,
          e.g. "beverages" -> "Beverages")
        - Duplicate rows (remove them)

    Returns:
        A cleaned copy of the DataFrame. Do not modify products_df in place.
    """
    # TODO: implement the cleaning steps described above.
    raise NotImplementedError


def clean_sales(sales_df: "pd.DataFrame", valid_product_ids) -> "pd.DataFrame":
    """
    Clean the sales DataFrame.

    Args:
        sales_df: the raw sales DataFrame
        valid_product_ids: a collection of product_id values that exist
            in the cleaned products table (use this to catch invalid /
            mistyped product references)

    Must handle:
        - Standardise sale_date to a single format: YYYY-MM-DD
          (hint: pandas.to_datetime() can parse several formats if you
          pass them one at a time, or try errors="coerce" and inspect
          what fails)
        - Rows with a missing or unparseable sale_date
        - Rows with a missing quantity
        - Rows with a missing payment_method (what's a sensible default?
          "Unknown" is a common, honest choice — don't guess a specific method)
        - Rows whose product_id is NOT in valid_product_ids
        - Duplicate rows

    Returns:
        A cleaned copy of the DataFrame with a standardised sale_date
        column (as a string in YYYY-MM-DD format) and no missing values
        in quantity or product_id.
    """
    # TODO: implement the cleaning steps described above.
    raise NotImplementedError


def cleaning_summary(raw_df: "pd.DataFrame", clean_df: "pd.DataFrame", name: str) -> str:
    """
    Build a short, human-readable string summarising how many rows were
    removed or changed during cleaning. You will paste this into your
    README findings section.

    Example output:
        "products: 16 raw rows -> 14 clean rows (2 removed)"
    """
    # TODO: compare len(raw_df) and len(clean_df) and format a message.
    raise NotImplementedError
