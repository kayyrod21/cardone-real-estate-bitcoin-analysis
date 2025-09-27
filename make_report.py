# make_report.py

import os
from cardone_analysis import run_hybrid_model
from btc_scenarios import plot_btc_regression
from cap_breakdown import plot_cap_breakdown
from capital_breakdown import plot_capital_breakdown
from overall import plot_overall
from portfolio_comp import plot_portfolio_comp
from portfolio_pie import plot_portfolio_pie

# Ensure outputs directory exists
os.makedirs("outputs", exist_ok=True)

print("\n▶ Running analysis and regenerating charts...")

# Call plotting functions directly (no subprocess)
print("  - Generating BTC Regression (zoomed bands)")
plot_btc_regression(save_path="outputs/btc_regression.png")

print("  - Running hybrid model...")
df, summary = run_hybrid_model()

# Add derived metrics to summary
summary["property_appreciation"] = summary["Final_Property_Value"] - summary["Equity_Investment"]
summary["btc_gains"] = summary["Final_BTC_Value"]
summary["cash_distributions"] = summary["Total_Cash_Distributions"]

print("  - Generating Capital Gains Breakdown (proportional)")
plot_cap_breakdown(summary, save_path="outputs/cap_breakdown.png")

print("  - Generating Capital Gains Breakdown (at exit)")
plot_capital_breakdown(summary, save_path="outputs/capital_breakdown.png")

print("  - Generating Total Portfolio Value chart")
plot_overall(df, save_path="outputs/overall.png")   # <-- pass df

print("  - Generating Portfolio Composition chart")
plot_portfolio_comp(df, save_path="outputs/portfolio_comp.png")  # <-- pass df

print("  - Generating Portfolio Pie chart")
plot_portfolio_pie(df, save_path="outputs/portfolio_pie.png")  # <-- pass df

# Verify all charts were generated
import os
required_charts = [
    "outputs/overall.png",
    "outputs/btc_regression.png", 
    "outputs/portfolio_comp.png",
    "outputs/portfolio_comp_alt.png",
    "outputs/portfolio_pie.png",
    "outputs/cap_breakdown.png",
    "outputs/capital_breakdown.png"
]

missing_charts = [chart for chart in required_charts if not os.path.exists(chart)]
if missing_charts:
    print(f"⚠️  Warning: Missing charts: {missing_charts}")
else:
    print("✅ All charts generated successfully")

# Build README.md (repo homepage)
with open("README.md", "w") as f:
    f.write("# Real Estate + Bitcoin Portfolio Analysis\n\n")
    f.write("This project explores Grant Cardone's strategy of using rental "
            "cash flow to accumulate Bitcoin. It compares real estate-only returns "
            "versus a hybrid allocation into BTC, modeled under different halving scenarios.\n\n")

    # --- Section 1 ---
    f.write("## 1. Overall Strategy Comparison\n")
    f.write("This heatmap provides a high-level comparison of the three strategies across "
            "**Liquidity**, **Capital Lockup**, **Human Effort**, and **Return Potential**.\n\n")
    f.write("![Overall Portfolio](outputs/overall.png)\n\n")

    # --- Section 2 ---
    f.write("## 2. Portfolio Composition Over Time\n")
    f.write("Even small BTC allocations compound over time.\n\n")
    f.write("![Portfolio Composition](outputs/portfolio_comp.png)\n")
    f.write("*Line chart showing Bitcoin vs Real Estate allocation over time*\n\n")
    f.write("![Portfolio Composition (Stacked)](outputs/portfolio_comp_alt.png)\n")
    f.write("*Alternative stacked area chart view of portfolio composition*\n\n")

    # --- Section 3 ---
    f.write("## 3. Portfolio Allocation: Start vs End\n")
    f.write("By Year 10, Bitcoin grows to ~7–10% under base case assumptions.\n\n")
    f.write("![Portfolio Pie](outputs/portfolio_pie.png)\n\n")

    # --- Section 4 ---
    f.write("## 4. Base Case Summary Metrics\n")
    f.write(f"- **Equity Investment**: ${summary['Equity_Investment']:,.0f}\n")
    f.write(f"- **Final Property Value**: ${summary['Final_Property_Value']:,.0f}\n")
    f.write(f"- **Final BTC Value**: ${summary['Final_BTC_Value']:,.0f}\n")
    f.write(f"- **Sale Proceeds**: ${summary['Sale_Proceeds']:,.0f}\n")
    f.write(f"- **IRR**: {summary['IRR']*100:.2f}%\n")
    f.write(f"- **NPV**: ${summary['NPV']:,.0f}\n\n")

    # --- Section 5 ---
    f.write("## 5. Capital Gains Breakdown\n")
    f.write("Proportional contribution of Property, BTC, and Cash:\n\n")
    f.write("![Capital Breakdown](outputs/cap_breakdown.png)\n\n")
    f.write("Absolute dollar terms (at exit):\n\n")
    f.write("![Capital Breakdown at Exit](outputs/capital_breakdown.png)\n\n")

    # --- Section 6 ---
    f.write("## 6. Bitcoin Halving Regression Context\n")
    f.write("The HPR (Halving Price Regression) model smooths out hype cycles "
            "and shows a conservative long-term Bitcoin price trajectory.\n\n")
    f.write("![BTC Regression](outputs/btc_regression.png)\n\n")

    # --- Section 7 ---
    f.write("## 7. Key Findings\n")
    f.write("- Real estate provides stable appreciation and steady cash flow.\n")
    f.write("- Bitcoin adds asymmetric upside, with convexity tied to the halving cycles.\n")
    f.write("- BTC gains exceeded cash distributions — showing how liquidity in USD terms "
            "underperforms vs appreciating assets.\n")
    f.write("- Even conservative BTC assumptions improve IRR and NPV.\n\n")

    f.write("➡️ **Overall Takeaway**: This hybrid model balances the **security of property** "
            "with the **convexity of Bitcoin**, making it a stable bet with asymmetric upside.\n\n")
    
    f.write("---\n\n")
    f.write("📖 **For detailed analysis and methodology, see [ANALYSIS.md](ANALYSIS.md)**\n")

print("\n✅ README.md (homepage) regenerated with updated charts and metrics")
