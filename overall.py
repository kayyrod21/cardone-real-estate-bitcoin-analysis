# overall.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_overall(df=None, save_path="outputs/overall.png"):
    # Define qualitative comparison
    data = {
        "Real Estate": {
            "Liquidity": 1,        # Low
            "Capital Lockup": 1,   # High lockup (bad)
            "Human Effort": 1,     # High (bad)
            "Return Potential": 4  # Strong returns
        },
        "Bitcoin": {
            "Liquidity": 5,        # High
            "Capital Lockup": 5,   # None (good)
            "Human Effort": 5,     # None (good)
            "Return Potential": 3  # Convex but volatile
        },
        "Hybrid": {
            "Liquidity": 3,        # Medium
            "Capital Lockup": 3,   # Medium
            "Human Effort": 3,     # Balanced
            "Return Potential": 5  # Best balance
        }
    }

    # Convert to DataFrame for heatmap
    df = pd.DataFrame(data).T

    plt.figure(figsize=(8, 5))
    sns.heatmap(df, annot=True, cmap="RdYlGn", cbar=True, linewidths=0.5,
                linecolor="gray", fmt="d", vmin=1, vmax=5)

    plt.title("Overall Comparison: Real Estate vs Bitcoin vs Hybrid", fontsize=14, pad=12)
    plt.ylabel("Portfolio Type")
    plt.xlabel("Evaluation Criteria")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200)
    plt.close()
