# portfolio_comp_alt.py
import matplotlib.pyplot as plt

def plot_portfolio_comp_alt(summary, save_path="outputs/portfolio_comp_alt.png"):
    """
    Stacked bar chart comparing starting vs ending portfolio composition.
    Uses summary dict values for consistency with other charts.
    """

    # Extract values safely from summary
    start_real_estate = summary.get("Equity_Investment", 0)
    start_btc = summary.get("Initial_BTC_Value", 0)

    end_real_estate = summary.get("Final_Property_Value", 0)
    end_btc = summary.get("Final_BTC_Value", 0)

    categories = ["Start", "End"]
    real_estate_vals = [start_real_estate, end_real_estate]
    btc_vals = [start_btc, end_btc]

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(categories, real_estate_vals, label="Real Estate", color="#4682B4")
    ax.bar(categories, btc_vals, bottom=real_estate_vals, label="Bitcoin", color="#FF9900")

    ax.set_ylabel("Portfolio Value (USD)")
    ax.set_title("Portfolio Composition: Start vs End")
    ax.legend()

    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.close()
