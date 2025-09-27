import matplotlib.pyplot as plt

def plot_cap_breakdown(summary, save_path="outputs/cap_breakdown.png"):
    # Extract raw values from summary
    initial_equity = summary["Equity_Investment"]
    final_property_value = summary["Final_Property_Value"]
    final_btc_value = summary["Final_BTC_Value"]
    sale_proceeds = summary["Sale_Proceeds"]
    total_distributions = summary["Total_Cash_Distributions"]

    # Calculate breakdowns
    property_appreciation = final_property_value - initial_equity
    btc_gains = final_btc_value
    cash_distributions = total_distributions

    values = [property_appreciation, btc_gains, cash_distributions]
    labels = ["Property Appreciation", "BTC Gains", "Cash Distributions"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

    # Plot stacked horizontal bar
    fig, ax = plt.subplots(figsize=(8, 2.5))
    left = 0
    for v, c, lbl in zip(values, colors, labels):
        ax.barh(["Capital Breakdown"], v, left=left, color=c, label=f"{lbl}: ${v:,.0f}")
        left += v

    ax.set_title("Capital Gains Breakdown (Base Case)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.25), ncol=3)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
