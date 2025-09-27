# portfolio_pie.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_portfolio_pie(df, save_path="outputs/portfolio_pie.png"):
    """
    Plots the portfolio allocation at Month 1 and Month 120 as pie charts.
    """
    # Calculate portfolio allocation percentages
    df["Total_Value"] = df["Property_Value"] + df["BTC_Value"]
    df["RE_%"] = df["Property_Value"] / df["Total_Value"]
    df["BTC_%"] = df["BTC_Value"] / df["Total_Value"]
    
    # Create allocation DataFrame for pie charts
    allocation_df = pd.DataFrame({
        "Real Estate": [df["RE_%"].iloc[0], df["RE_%"].iloc[-1]],
        "BTC": [df["BTC_%"].iloc[0], df["BTC_%"].iloc[-1]]
    }, index=["Month 1", "Month 120"])

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Month 1 pie
    axes[0].pie(allocation_df.iloc[0], labels=allocation_df.columns, autopct='%1.1f%%',
                colors=["#8c564b", "#ff7f0e"], startangle=90)
    axes[0].set_title("Month 1")

    # Month 120 pie
    axes[1].pie(allocation_df.iloc[-1], labels=allocation_df.columns, autopct='%1.1f%%',
                colors=["#8c564b", "#ff7f0e"], startangle=90)
    axes[1].set_title("Month 120")

    plt.suptitle("Portfolio Allocation: Start vs End")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
