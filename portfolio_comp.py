import matplotlib.pyplot as plt
from cardone_analysis import run_hybrid_model

# Run base case
df, summary = run_hybrid_model()

# Compute portfolio % composition
df["Portfolio_Value"] = df["Property_Value"] + df["BTC_Value"]
df["RE_%"] = df["Property_Value"] / df["Portfolio_Value"]
df["BTC_%"] = df["BTC_Value"] / df["Portfolio_Value"]

# Plot stacked area
plt.figure(figsize=(10,6))
plt.stackplot(
    df["Month"],
    df["RE_%"],
    df["BTC_%"],
    labels=["Real Estate %", "Bitcoin %"]
)
plt.title("Portfolio Composition Over Time")
plt.xlabel("Month")
plt.ylabel("Share of Portfolio Value")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("outputs/portfolio_comp.png", dpi=300)
plt.close()
