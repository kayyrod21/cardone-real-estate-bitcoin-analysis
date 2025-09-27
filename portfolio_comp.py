# portfolio_comp.py
import matplotlib.pyplot as plt

def plot_portfolio_comp(summary, save_path="outputs/portfolio_comp.png"):
    # Extract key values
    equity = summary["Equity_Investment"]
    prop = summary["Final_Property_Value"] - equity
    btc = summary["Final_BTC_Value"]
    cash = summary["Total_Cash_Distributions"]

    categories = ["Equity Invested", "Property Appreciation", "BTC Gains", "Cash Distributions"]
    values = [equity, prop, btc, cash]

    # Calculate cumulative values for waterfall steps
    cumulative = [0]
    for v in values[:-1]:
        cumulative.append(cumulative[-1] + v)

    # Plot waterfall bars
    plt.figure(figsize=(10, 6))
    for i, (cat, val, base) in enumerate(zip(categories, values, cumulative)):
        plt.bar(cat, val, bottom=base, label=cat if i > 0 else "", color=["grey", "steelblue", "orange", "green"][i])

        # Add labels
        plt.text(i, base + val/2, f"${val/1e6:.1f}M", ha="center", va="center", fontsize=10, fontweight="bold", color="white")

    plt.title("Portfolio Value Breakdown (Waterfall)")
    plt.ylabel("USD Value")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.close()
