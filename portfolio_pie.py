import matplotlib.pyplot as plt
from cardone_analysis import run_hybrid_model

# Run base case
df, summary = run_hybrid_model()

# Initial allocation
initial_re = df.loc[0, "Property_Value"]
initial_btc = df.loc[0, "BTC_Value"]

# Final allocation
final_re = df["Property_Value"].iloc[-1]
final_btc = df["BTC_Value"].iloc[-1]

fig, axes = plt.subplots(1, 2, figsize=(10,6))

axes[0].pie([initial_re, initial_btc], labels=["Real Estate", "Bitcoin"],
            autopct='%1.1f%%', colors=["#1f77b4", "#ff7f0e"])
axes[0].set_title("Year 0 Portfolio")

axes[1].pie([final_re, final_btc], labels=["Real Estate", "Bitcoin"],
            autopct='%1.1f%%', colors=["#1f77b4", "#ff7f0e"])
axes[1].set_title("Year 10 Portfolio")

plt.suptitle("Portfolio Allocation: Start vs End")
plt.tight_layout()
plt.savefig("outputs/portfolio_pie.png", dpi=300)
plt.close()
