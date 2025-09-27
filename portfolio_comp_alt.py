# portfolio_comp_alt.py
import matplotlib.pyplot as plt

def plot_portfolio_comp_alt(summary, save_path="outputs/portfolio_comp_alt.png"):
    # Pull values safely with .get()
    start_real_estate = summary.get("Equity_Investment", 0)
    start_btc = summary.get("Initial_BTC_Value", 0)
    end_real_estate = summary.get("Final_Property_Value", 0)
    end_btc = summary.get("Final_BTC_Value", 0)

    import matplotlib.pyplot as plt
    import numpy as np

    labels = ["Start Real Estate", "Start BTC", "End Real Estate", "End BTC"]
    values = [start_real_estate, start_btc, end_real_estate, end_btc]
    colors = ["saddlebrown", "gold", "peru", "orange"]

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(labels, values, color=colors, alpha=0.8, edgecolor="white")

    # Add value labels
    for i, v in enumerate(values):
        ax.text(i, v + max(values) * 0.02, f"${v/1e6:.1f}M", ha="center", fontsize=9)

    ax.set_title("Portfolio Start vs End Composition")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.close()
