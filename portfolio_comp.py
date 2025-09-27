# portfolio_comp.py
"""
Portfolio composition chart (mountain chart style)
Shows evolution of Real Estate vs Bitcoin share over time.
"""

import matplotlib.pyplot as plt
import pandas as pd
from cardone_analysis import run_hybrid_model

def plot_portfolio_comp(df, save_path="outputs/portfolio_comp.png"):
    # Use the DataFrame passed as parameter

    # Calculate shares of portfolio
    df["Total_Value"] = df["Property_Value"] + df["BTC_Value"]
    df["RE_%"] = df["Property_Value"] / df["Total_Value"] * 100
    df["BTC_%"] = df["BTC_Value"] / df["Total_Value"] * 100

    # Mountain chart
    plt.figure(figsize=(10,6))
    plt.stackplot(
        df["Month"],
        df["RE_%"],
        df["BTC_%"],
        labels=["Real Estate", "Bitcoin"],
        colors=["#8c564b", "#ff7f0e"],
        alpha=0.8
    )

    plt.title("Portfolio Composition Over Time (Real Estate vs Bitcoin)")
    plt.xlabel("Month")
    plt.ylabel("Portfolio Share (%)")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    plot_portfolio_comp()
