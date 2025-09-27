# make_report.py

import os
import subprocess
from cardone_analysis import run_hybrid_model
from btc_scenarios import generate_hpr_paths

# Ensure outputs directory exists
os.makedirs("outputs", exist_ok=True)

# Run the analysis scripts to regenerate data & charts
scripts = ["portfolio_comp.py", "portfolio_pie.py", "overall.py", "cardone_analysis.py", "cap_breakdown.py"]

print("\n▶ Running analysis scripts...")
for script in scripts:
    if os.path.exists(script):
        print(f"  - {script}")
        subprocess.run(["python3", script])
    else:
        print(f"  ! Skipping {script}, not found")

# ✅ Run base case model to grab summary metrics
_, summary = run_hybrid_model()

# ✅ Run halving scenario models
scenarios = ["Blue", "Green", "Yellow", "Red"]
hpr_df = generate_hpr_paths(10)  # 10 years ahead
scenario_summaries = {}

for scenario in scenarios:
    btc_projection = hpr_df[scenario].values[:120]  # 10 years monthly
    df, scen_summary = run_hybrid_model(btc_growth_rate=0,  # override with projection
                                        hold_period_years=10)
    scen_summary["Final_BTC_Value"] = btc_projection[-1]  # use projection endpoint
    scenario_summaries[scenario] = scen_summary

# Build REPORT.md
with open("outputs/report.md", "w") as f:
    f.write("# Real Estate + Bitcoin Portfolio Analysis\n\n")
    f.write("This project explores Grant Cardone's strategy of using rental "
            "cash flow to accumulate Bitcoin. It compares real estate-only returns "
            "versus a hybrid allocation into BTC, modeled under different halving scenarios.\n\n")

    # --- Section 1: Total Portfolio Value ---
    f.write("## 1. Total Portfolio Value Under Halving Scenarios\n")
    f.write("This chart shows how the portfolio grows over 10 years, depending on "
            "which Bitcoin halving band (Blue, Green, Yellow, Red) it follows.\n\n")
    f.write("![Overall Portfolio](outputs/overall.png)\n\n")

    # --- Section 2: Portfolio Composition ---
    f.write("## 2. Portfolio Composition Over Time\n")
    f.write("The stack plot illustrates how the share of Bitcoin vs Real Estate "
            "evolves. Even small BTC allocations compound over time.\n\n")
    f.write("![Portfolio Composition](outputs/portfolio_comp.png)\n\n")

    # --- Section 3: Portfolio Allocation (Pie) ---
    f.write("## 3. Portfolio Allocation: Start vs End\n")
    f.write("Comparing Year 0 and Year 10. Initially, the portfolio is nearly "
            "100% real estate. By Year 10, Bitcoin has grown to ~7–10% under "
            "base case assumptions.\n\n")
    f.write("![Portfolio Pie](outputs/portfolio_pie.png)\n\n")

    # --- Section 4: Base Case Metrics ---
    f.write("## 4. Base Case Summary Metrics\n")
    f.write("These are the outputs from the base case (10% BTC growth, 10-year hold period):\n\n")
    f.write(f"- **Equity Investment**: ${summary['Equity_Investment']:,.0f}\n")
    f.write(f"- **Final Property Value**: ${summary['Final_Property_Value']:,.0f}\n")
    f.write(f"- **Final BTC Value**: ${summary['Final_BTC_Value']:,.0f}\n")
    f.write(f"- **Sale Proceeds**: ${summary['Sale_Proceeds']:,.0f}\n")
    f.write(f"- **IRR**: {summary['IRR']*100:.2f}%\n")
    f.write(f"- **NPV**: ${summary['NPV']:,.0f}\n\n")

        # --- Section 4b: Capital Gains Breakdown ---
    f.write("## 4b. Capital Gains Breakdown (Base Case)\n")

    initial_equity = summary["Equity_Investment"]
    final_property_value = summary["Final_Property_Value"]
    final_btc_value = summary["Final_BTC_Value"]
    sale_proceeds = summary["Sale_Proceeds"]
    total_distributions = summary["Total_Cash_Distributions"]

    # Property appreciation (approximate: final value minus equity invested)
    property_appreciation = final_property_value - initial_equity
    btc_gains = final_btc_value
    total_value = sale_proceeds + final_btc_value + total_distributions
    total_gain = total_value - initial_equity

    f.write(f"- **Property Appreciation**: ${property_appreciation:,.0f}\n")
    f.write(f"- **BTC Gains**: ${btc_gains:,.0f}\n")
    f.write(f"- **Cash Distributions**: ${total_distributions:,.0f}\n")
    f.write(f"- **Total Value at Exit**: ${total_value:,.0f}\n")
    f.write(f"- **Net Gain (Total – Equity Investment)**: ${total_gain:,.0f}\n\n")
    # --- Section 4c: Visual Breakdown ---
    f.write("## 4c. Visual Breakdown of Capital Gains\n")
    f.write("This stacked bar chart shows the relative contributions of "
            "Property Appreciation, BTC Gains, and Cash Distributions.\n\n")
    f.write("![Capital Breakdown](outputs/capital_breakdown.png)\n\n")


    # --- Section 5: Halving Scenario Metrics ---
    f.write("## 5. Halving Scenario Metrics\n")
    f.write("Here we compare outcomes under the HPR (Halving Price Regression) model:\n\n")
    f.write("| Scenario | IRR | NPV | Final BTC Value |\n")
    f.write("|----------|-----|-----|-----------------|\n")
    for scen, s in scenario_summaries.items():
        f.write(f"| {scen} | {s['IRR']*100:.2f}% | ${s['NPV']:,.0f} | ${s['Final_BTC_Value']:,.0f} |\n")
    f.write("\n")

    # --- Section 6: Bitcoin Regression ---
    f.write("## 6. Bitcoin Halving Regression Context\n")
    f.write("The HPR (Halving Price Regression) model smooths out hype cycles and shows "
            "a conservative long-term Bitcoin price trajectory. This chart overlays historical "
            "BTC prices with the regression bands.\n\n")
    f.write("![BTC Regression](outputs/btc_regression.png)\n\n")

    # --- Section 7: Findings ---
    f.write("## 7. Key Findings\n")
    f.write("- Real estate provides stable appreciation and steady cash flow.\n")
    f.write("- Bitcoin adds asymmetric upside, with convexity tied to the halving cycles.\n")
    f.write("- Even conservative BTC growth assumptions improve the overall IRR and NPV.\n")
    f.write("- In optimistic halving scenarios, Bitcoin could eclipse real estate’s contribution.\n\n")

    f.write("➡️ **Overall Takeaway**: This hybrid model balances the **security of property** "
            "with the **convexity of Bitcoin**, making it a stable bet with asymmetric upside.\n")

print("\n✅ REPORT.md has been generated successfully at outputs/report.md")
