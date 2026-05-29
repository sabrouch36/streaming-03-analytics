"""Revenue dashboard utilities for consumed sales analysis."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

CSV_FILE = Path("data/output/consumed_sales.csv")


def load_data() -> pd.DataFrame:
    """Load the consumed sales data.

    Returns:
    -------
    pd.DataFrame
        DataFrame with parsed datetime and cumulative revenue.
    """
    df = pd.read_csv(CSV_FILE)

    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime")
    df["cumulative_revenue"] = df["total"].cumsum()

    return df


def main():
    """Run revenue analytics and generate dashboard charts."""
    df = load_data()
    high_value_count = df["high_value_order"].sum()
    high_value_pct = (high_value_count / len(df)) * 100

    print(f"High Value Orders: {high_value_count}")
    print(f"High Value Percentage: {high_value_pct:.1f}%")

    plt.figure(figsize=(10, 5))
    plt.plot(df["datetime"], df["cumulative_revenue"])

    plt.title("Cumulative Revenue Growth")
    plt.xlabel("Time")
    plt.ylabel("Revenue ($)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("data/output/revenue_growth.png")

    print("Chart saved: data/output/revenue_growth.png")
    print("\nRows Loaded:", len(df))
    print(df[["datetime", "total", "cumulative_revenue"]].head())

    course_revenue = (
        df.groupby("product_id")["total"].sum().sort_values(ascending=False)
    )
    high_value_counts = df["high_value_order"].value_counts()

    print("\nHigh Value Distribution:")
    print(high_value_counts)
    plt.figure(figsize=(6, 6))
    plt.pie(
        high_value_counts,
        labels=["Regular Orders", "High Value Orders"],
        autopct="%1.1f%%",
    )

    plt.title("High Value Order Distribution")

    plt.tight_layout()

    plt.savefig("data/output/high_value_distribution.png")

    print("Chart saved: data/output/high_value_distribution.png")
    plt.figure(figsize=(10, 5))
    course_revenue.plot(kind="bar")

    plt.title("Revenue by Course")
    plt.xlabel("Course")
    plt.ylabel("Revenue ($)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("data/output/course_revenue.png")

    print("Chart saved: data/output/course_revenue.png")
    print("\nRevenue By Course:")
    print(course_revenue)


if __name__ == "__main__":
    main()
