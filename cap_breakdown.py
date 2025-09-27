# capital_breakdown.py

import matplotlib.pyplot as plt
from cardone_analysis import run_hybrid_model

# Run the base case
_, summary = run_hybrid_model()

# Extract metrics
property_appreciation = summary["Final_Property_Value"] - summary["Equity_Investment"]
btc_gains = summary["Final_BTC_Value"]
cash_distributions = summary["Total_Cash_Distributions"]

# Data for stacked bar
categories = ["Total Returns"]
values = [property_appreciation, btc_gains, cash_distributions]
labels = ["Property Appreciation", "BTC Gains", "Cash Distributions"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

plt.figure(figsize=(8,6))
plt.bar(categories, values[0], label=labels[0], color=colors[0])
plt.bar(categories, values[1], bottom=values[0], label=labels[1], color=colors[1])
plt.bar(categories, values[2], bottom=values[0]+values[1], label=labels[2], color=colors[2])

plt.title("Capital Gains Breakdown (Base Case)")
plt.ylabel("USD")
plt.legend()
plt.tight_layout()

# Save chart
plt.savefig("outputs/cap_breakdown.png")
plt.close()
