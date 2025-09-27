# portfolio_comp.py
"""
Portfolio composition chart with two visualization styles
Shows evolution of Real Estate vs Bitcoin share over time.
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_portfolio_comp(df, save_path="outputs/portfolio_comp.png", mode="line"):
    """
    Plot portfolio composition over time with two visualization options.
    
    Args:
        df: DataFrame with portfolio data
        save_path: Path to save the chart
        mode: "line" for line chart (default) or "stacked" for stacked area chart
    """
    # Calculate shares of portfolio
    df["Total_Value"] = df["Property_Value"] + df["BTC_Value"]
    df["RE_%"] = df["Property_Value"] / df["Total_Value"] * 100
    df["BTC_%"] = df["BTC_Value"] / df["Total_Value"] * 100

    plt.figure(figsize=(10, 6))
    
    if mode == "line":
        # Line Chart (Default)
        plt.plot(df["Month"], df["BTC_%"], color="gold", label="Bitcoin", linewidth=2)
        plt.plot(df["Month"], df["RE_%"], color="brown", label="Real Estate", linewidth=2)
        plt.title("Portfolio Composition Over Time (Line Chart)")
        
    elif mode == "stacked":
        # Normalized Stacked Area Chart
        plt.stackplot(
            df["Month"],
            df["RE_%"],
            df["BTC_%"],
            labels=["Real Estate", "Bitcoin"],
            colors=["brown", "gold"],
            alpha=0.8
        )
        plt.title("Portfolio Composition Over Time (Stacked Area)")
    
    else:
        raise ValueError("Mode must be 'line' or 'stacked'")

    plt.xlabel("Month")
    plt.ylabel("Portfolio Share (%)")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.close()

if __name__ == "__main__":
    # Test both modes
    from cardone_analysis import run_hybrid_model
    df, _ = run_hybrid_model()
    
    # Generate line chart (default)
    plot_portfolio_comp(df, "outputs/portfolio_comp.png", mode="line")
    print("Generated line chart: outputs/portfolio_comp.png")
    
    # Generate stacked area chart
    plot_portfolio_comp(df, "outputs/portfolio_comp_alt.png", mode="stacked")
    print("Generated stacked area chart: outputs/portfolio_comp_alt.png")
