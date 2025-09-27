import matplotlib.pyplot as plt
from cardone_analysis import run_hybrid_model
from btc_scenarios import generate_hpr_paths

# Run base case
df, summary = run_hybrid_model()
hpr_df = generate_hpr_paths(10)  # 10 years

scenarios = ["Blue", "Green", "Yellow", "Red"]

plt.figure(figsize=(10,6))
for s in scenarios:
    btc_projection = hpr_df[s].values[:len(df)]
    btc_value = df["BTC_Units"].values * btc_projection
    portfolio_value = df["Property_Value"].values + btc_value
    plt.plot(df["Month"], portfolio_value, label=f"{s} Scenario")

plt.title("Total Portfolio Value Under Halving Scenarios")
plt.xlabel("Month")
plt.ylabel("USD")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/overall.png", dpi=300)
plt.close()
