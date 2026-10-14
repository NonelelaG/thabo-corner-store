"""
visualize.py
-------------
Task 5: Turn your analysis into charts.

This module covers KM-04 KT07: Visualising Data with AI-assisted tools.
We use matplotlib here, one of the most common Python charting
libraries (conceptually similar to the ggplot2 example from the
KM-04 slides).

You must produce AT LEAST TWO charts:
  1. A bar chart of total revenue per product (or per category)
  2. A line chart of the monthly sales trend

Save both charts as .png files — you will include them as evidence
in your submission.
"""

import matplotlib.pyplot as plt


def bar_chart_revenue_per_product(product_names: list, revenues: list, save_path: str = "revenue_per_product.png"):
    """
    Create and save a bar chart of revenue per product.

    Args:
        product_names: list of product name strings (x-axis labels)
        revenues: list of revenue numbers, same length and order as
            product_names
        save_path: where to save the .png file

    TODO:
        plt.figure(figsize=(10, 6))
        plt.bar(product_names, revenues)
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Revenue (R)")
        plt.title("Total Revenue per Product — Thabo's Corner Store")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
    """
    raise NotImplementedError


def line_chart_monthly_trend(monthly_trend: dict, save_path: str = "monthly_trend.png"):
    """
    Create and save a line chart of total quantity sold per month.

    Args:
        monthly_trend: a dict like {"2026-01": 143, "2026-02": 97}
            (this is exactly what analysis.monthly_sales_trend() returns)
        save_path: where to save the .png file

    TODO:
        months = list(monthly_trend.keys())
        totals = list(monthly_trend.values())
        plt.figure(figsize=(8, 5))
        plt.plot(months, totals, marker="o")
        plt.ylabel("Units Sold")
        plt.title("Monthly Sales Trend — Thabo's Corner Store")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
    """
    raise NotImplementedError
