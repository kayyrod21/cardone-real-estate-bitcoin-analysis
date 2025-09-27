# capital_breakdown.py
import matplotlib.pyplot as plt

def plot_capital_breakdown(summary, save_path="outputs/capital_breakdown.png"):
    # Extract values
    values = [
        summary["Final_Property_Value"] - summary["Equity_Investment"],  # property appreciation
        summary["Final_BTC_Value"],                                      # btc gains
        summary["Total_Cash_Distributions"]                              # cash flows
    ]
    labels = ["Property Appreciation", "BTC Gains", "Cash Distributions"]
    colors = ["#4682B4", "#FF9900", "#9370DB"]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(labels, values, color=colors, alpha=0.85)

    # Add labels on top
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, val, f"${val/1e6:.1f}M",
                ha="center", va="bottom", fontsize=11, fontweight="bold")

    ax.set_title("Capital Gains Breakdown at Exit")
    ax.set_ylabel("USD Value")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.close()
