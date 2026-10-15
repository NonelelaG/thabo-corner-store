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
    products_df = pd.read_csv(products_path)
    sales_df = pd.read_csv(sales_path)
    return products_df, sales_df


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
        # ---- 1. Make a copy so we don't mutate the caller's DataFrame ----
    df = products_df.copy()

    # ---- 2. Drop exact duplicate rows ----
    # keep='first' keeps the first occurrence and removes later copies.
    df = df.drop_duplicates(keep="first")

    # ---- 3. Strip whitespace from text columns ----
    # Leading/trailing spaces make 'Beverages ' look different from 'Beverages'.
    for col in ["product_name", "category"]:
        df[col] = df[col].astype(str).str.strip()

    # ---- 4. Standardise category to Title Case ----
    # 'beverages', 'BEVERAGES' and 'Beverages' all become 'Beverages'.
    df["category"] = df["category"].str.title()

    # ---- 5. Drop rows where product_name is missing ----
    # A product with no name cannot be reported on or displayed in a chart.
    df = df[df["product_name"].notna()]
    df = df[df["product_name"] != ""]
    df = df[df["product_name"].str.lower() != "nan"]

    # ---- 6. Drop rows where unit_price is missing ----
    # Revenue is quantity * unit_price. Without a price we cannot
    # compute revenue, so this row is unusable for our analysis.
    df = df[df["unit_price"].notna()]

    # ---- 7. Reset the index so row numbers look clean ----
    df = df.reset_index(drop=True)

    return df


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
        # ---- 1. Copy so we don't modify the caller's DataFrame ----
    df = sales_df.copy()

    # ---- 2. Drop exact duplicate rows ----
    df = df.drop_duplicates(keep="first")

    # ---- 3. Strip whitespace from text columns ----
    for col in ["sale_id", "product_id", "payment_method", "customer_type"]:
        df[col] = df[col].astype(str).str.strip()

    # ---- 4. Drop sales that reference a product that doesn't exist ----
    # These "orphan" product_ids can't be joined to the products table,
    # so they would break every revenue query. Better to remove them.
    df = df[df["product_id"].isin(valid_product_ids)]

    # ---- 5. Drop rows where quantity is missing ----
    # Revenue = quantity * unit_price. Without a quantity the sale is
    # unanalysable, so we drop the row.
    df = df[df["quantity"].notna()]

    # ---- 6. Standardise sale_date to YYYY-MM-DD ----
    # The raw data has several different formats. We try each known
    # format one at a time (in order) and keep the first one that
    # succeeds. Anything that can't be parsed becomes NaT and is
    # dropped in step 7.
    #
    # We do NOT use pandas' automatic date parsing, because a value
    # like 02/01/2026 is ambiguous — pandas might read it as Feb 1
    # when we mean 2 January. Being explicit avoids silent errors.
    known_formats = [
        "%Y-%m-%d",   # 2026-01-01
        "%d/%m/%Y",   # 02/01/2026  (DD/MM/YYYY)
        "%Y/%m/%d",   # 2026/01/03
        "%d-%m-%Y",   # 05-01-2026
        "%d %B %Y",   # 15 January 2026
    ]

    def parse_date(value):
        """Try each known format; return a Timestamp or NaT."""
        if pd.isna(value):
            return pd.NaT
        text = str(value).strip()
        for fmt in known_formats:
            try:
                return pd.to_datetime(text, format=fmt)
            except (ValueError, TypeError):
                continue
        return pd.NaT

    df["sale_date"] = df["sale_date"].apply(parse_date)

    # ---- 7. Drop rows with an unparseable or missing date ----
    df = df[df["sale_date"].notna()]

    # ---- 8. Convert the date column to YYYY-MM-DD strings ----
    # Storing as text in SQLite is simple and sorts correctly.
    df["sale_date"] = df["sale_date"].dt.strftime("%Y-%m-%d")

    # ---- 9. Fill missing payment_method with "Unknown" ----
    # We do NOT guess a method — pretending a sale was cash when we
    # don't know is worse than admitting we don't know.
    df["payment_method"] = df["payment_method"].replace("nan", pd.NA)
    df["payment_method"] = df["payment_method"].fillna("Unknown")

    # ---- 10. Fill missing customer_type with "Unknown" ----
    # This is an optional field, so "Unknown" is honest.
    df["customer_type"] = df["customer_type"].replace("nan", pd.NA)
    df["customer_type"] = df["customer_type"].fillna("Unknown")

    # ---- 11. Tidy up: integer quantity, fresh index ----
    df["quantity"] = df["quantity"].astype(int)
    df = df.reset_index(drop=True)

    return df


def cleaning_summary(raw_df: "pd.DataFrame", clean_df: "pd.DataFrame", name: str) -> str:
    """
    Build a short, human-readable string summarising how many rows were
    removed or changed during cleaning. You will paste this into your
    README findings section.

    Example output:
        "products: 16 raw rows -> 14 clean rows (2 removed)"
    """
    raw_count = len(raw_df)
    clean_count = len(clean_df)
    removed = raw_count - clean_count
    pct = (removed / raw_count * 100) if raw_count else 0

    return (
        f"{name}: {raw_count} raw rows -> {clean_count} clean rows "
        f"({removed} removed, {pct:.1f}%)"
    )
