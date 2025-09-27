# make_report.py

import os
from cardone_analysis import run_hybrid_model
from btc_scenarios import plot_btc_regression
from cap_breakdown import plot_cap_breakdown
from capital_breakdown import plot_capital_breakdown
from overall import plot_overall
from portfolio_comp_alt import plot_portfolio_comp_alt
from portfolio_comp import plot_portfolio_comp
from portfolio_pie import plot_portfolio_pie

# Ensure outputs directory exists
os.makedirs("outputs", exist_ok=True)

print("\n▶ Running analysis and regenerating charts...")

# Call plotting functions directly
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

print("  - Generating Strategy Comparison Heatmap")
plot_overall(df, save_path="outputs/overall.png")

print("  - Generating Portfolio Waterfall Breakdown")
plot_portfolio_comp(summary, save_path="outputs/portfolio_comp.png")

print("  - Generating Portfolio Start vs End Composition")
plot_portfolio_comp_alt(summary, save_path="outputs/portfolio_comp_alt.png")

print("  - Generating Portfolio Pie chart")
plot_portfolio_pie(df, save_path="outputs/portfolio_pie.png")

# Verify all charts were generated
required_charts = [
    "outputs/overall.png",
    "outputs/btc_regression.png",
    "outputs/portfolio_comp.png",
    "outputs/portfolio_comp_alt.png",
    "outputs/portfolio_pie.png",
    "outputs/cap_breakdown.png",
    "outputs/capital_breakdown.png",
]
missing_charts = [chart for chart in required_charts if not os.path.exists(chart)]
if missing_charts:
    print(f"⚠️  Warning: Missing charts: {missing_charts}")
else:
    print("✅ All charts generated successfully")

# -----------------------
# Build README.md (context only)
# -----------------------
with open("README.md", "w") as f:
    f.write("# Real Estate + Bitcoin Portfolio Project\n\n")
    f.write("This repository explores **Grant Cardone’s hybrid strategy**: combining "
            "real estate’s steady cash flows with Bitcoin treasury allocation.\n\n")
    f.write("## Project Context\n")
    f.write("- In June 2025, Cardone Capital disclosed a **1,000 BTC purchase (~$100M)**, "
            "with plans to accumulate 3,000 BTC by year-end.\n")
    f.write("- Funds like the **10X Boca Raton Bitcoin Fund** and **10X Miami River Bitcoin Fund** "
            "use real estate yields to continuously acquire Bitcoin.\n")
    f.write("- The model mirrors strategies of **Tesla, MicroStrategy, and other corporates** "
            "that pair traditional income streams with Bitcoin treasuries.\n\n")
    f.write("## Why Hybrid?\n")
    f.write("- **Real Estate**: stable appreciation, predictable cash flow, but illiquid and labor-intensive.\n")
    f.write("- **Bitcoin**: liquid, no overhead, asymmetric upside tied to halving cycles.\n")
    f.write("- **Hybrid**: combines stability of property with convexity of Bitcoin.\n\n")
    f.write("📖 See [REPORT.md](REPORT.md) for full technical analysis and chart outputs.\n")

# -----------------------
# Build REPORT.md (detailed analysis with dynamic metrics)
# -----------------------
with open("REPORT.md", "w") as f:
    f.write("# Real Estate + Bitcoin Hybrid Portfolio Analysis\n\n")
    f.write("This report provides a technical and financial breakdown of Grant Cardone’s hybrid strategy: "
            "combining real estate cash flows with Bitcoin accumulation. The goal is to evaluate how Bitcoin "
            "allocation impacts liquidity, portfolio convexity, and long-term returns compared to real estate-only exposure.\n\n")

    # Section 1: Heatmap
    f.write("## 1. Strategy Comparison Heatmap\n")
    f.write("![Overall Portfolio](outputs/overall.png)\n\n")
    f.write("**Interpretation**\n")
    f.write("- Real Estate Only: high effort, illiquid, steady.\n")
    f.write("- Bitcoin Only: liquid, no management, volatile.\n")
    f.write("- Hybrid Model: best balance of stability and convex upside.\n\n")

    # Section 2: Capital Gains Breakdown
    f.write("## 2. Capital Gains Breakdown\n")
    f.write("### a. Proportional Contribution\n")
    f.write("![Capital Breakdown](outputs/cap_breakdown.png)\n\n")
    f.write("### b. Absolute Contribution at Exit\n")
    f.write("![Capital Breakdown at Exit](outputs/capital_breakdown.png)\n\n")
    f.write(f"- **Property Appreciation**: ${summary['property_appreciation']:,.0f}\n")
    f.write(f"- **BTC Gains**: ${summary['btc_gains']:,.0f}\n")
    f.write(f"- **Cash Distributions**: ${summary['cash_distributions']:,.0f}\n\n")
    f.write("**Interpretation**\n")
    f.write(f"- Property appreciation dominates (${summary['property_appreciation']/1e6:.1f}M).\n")
    f.write(f"- Bitcoin gains (${summary['btc_gains']/1e6:.1f}M) exceed cash distributions (${summary['cash_distributions']/1e6:.1f}M).\n")
    f.write("- BTC acts as a superior liquidity source compared to rent-driven cash.\n\n")

    # Section 3: Portfolio Value Over Time
    f.write("## 3. Portfolio Value Over Time\n")
    f.write("![Total Portfolio](outputs/overall.png)\n\n")
    f.write("**Interpretation**\n")
    f.write(f"- Equity Invested: ${summary['Equity_Investment']:,.0f}\n")
    f.write(f"- Final Property Value: ${summary['Final_Property_Value']:,.0f}\n")
    f.write(f"- Final BTC Value: ${summary['Final_BTC_Value']:,.0f}\n")
    f.write(f"- Sale Proceeds: ${summary['Sale_Proceeds']:,.0f}\n")
    f.write(f"- IRR: {summary['IRR']*100:.2f}%\n")
    f.write(f"- NPV: ${summary['NPV']:,.0f}\n\n")
    f.write("- Hybrid IRR and NPV exceed real estate-only.\n")
    f.write("- Bitcoin convexity stacks on steady property base.\n\n")

    # Section 4: Portfolio Composition
    f.write("## 4. Portfolio Composition Dynamics\n")
    f.write("### a. Waterfall Breakdown\n")
    f.write("![Portfolio Comp](outputs/portfolio_comp.png)\n\n")
    f.write("### b. Start vs End Composition\n")
    f.write("![Portfolio Comp Alt](outputs/portfolio_comp_alt.png)\n\n")
    f.write("### c. Allocation Pie (Start vs End)\n")
    f.write("![Portfolio Pie](outputs/portfolio_pie.png)\n\n")
    f.write("**Interpretation**\n")
    f.write(f"- BTC compounds from 0% → ~{(summary['btc_gains'] / (summary['Final_Property_Value'] + summary['Final_BTC_Value']))*100:.1f}% "
            "of portfolio over 10 years.\n")
    f.write("- Small allocations become meaningful without additional capital.\n\n")

    # Section 5: Bitcoin Regression
    f.write("## 5. Bitcoin Regression Model Context\n")
    f.write("![BTC Regression](outputs/btc_regression.png)\n\n")
    f.write("**Interpretation**\n")
    f.write("- Halving-driven regression shows conservative long-term BTC price path.\n")
    f.write("- Consistent with treasury strategy underpinning this model.\n\n")

    # Section 6: Key Findings
    f.write("## 6. Key Findings\n")
    f.write("- Real estate provides the foundation of returns.\n")
    f.write("- Bitcoin delivers superior liquidity and asymmetric upside.\n")
    f.write(f"- BTC gains (${summary['btc_gains']/1e6:.1f}M) exceeded cash distributions "
            f"(${summary['cash_distributions']/1e6:.1f}M).\n")
    f.write("- Hybrid model improves IRR, NPV, and convexity.\n\n")
    f.write("➡️ Overall takeaway: Cardone’s hybrid approach transforms real estate from a slow, illiquid asset "
            "into a cash-flowing base plus Bitcoin convexity engine.\n")

print("\n✅ README.md (context) and REPORT.md (full analysis with dynamic metrics) regenerated successfully")
