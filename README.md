# 🏠💰 Real Estate + Bitcoin Portfolio Analysis

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Analysis](https://img.shields.io/badge/Analysis-Complete-brightgreen.svg)](ANALYSIS.md)

> **Grant Cardone's Strategy**: Using rental cash flow to accumulate Bitcoin over time

This project explores three investment strategies through quantitative modeling and visual analysis:

- 🏢 **Real Estate Only** — capital-intensive, labor-heavy, but stable
- ₿ **Bitcoin Only** — highly liquid, minimal effort, but volatile  
- 🔄 **Hybrid (RE + BTC)** — combines both for optimal risk-adjusted returns

---

## 📊 Quick Overview

| Strategy | Liquidity | Capital Lockup | Human Effort | Return Potential |
|----------|-----------|----------------|--------------|------------------|
| Real Estate | ⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐⭐ |
| Bitcoin | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Hybrid** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🎯 Key Visualizations

### 1. Overall Strategy Comparison
![Overall Portfolio](outputs/overall.png)
*Heatmap showing strategy trade-offs across key metrics (1-5 scale)*

### 2. Bitcoin Regression & Halving Context
![BTC Regression](outputs/btc_regression.png)
*Logarithmic regression bands with halving cycles through 2035*

### 3. Portfolio Composition Evolution
![Portfolio Composition](outputs/portfolio_comp.png)
*Line chart showing Bitcoin vs Real Estate allocation over time*

![Portfolio Composition (Stacked)](outputs/portfolio_comp_alt.png)
*Alternative stacked area chart view of portfolio composition*

> **💡 Visualization Options**: The portfolio composition can be viewed as either a clean line chart (default) or a normalized stacked area chart. Both show the same data but offer different perspectives on allocation changes over time.

### 4. Capital Gains Breakdown
![Capital Breakdown](outputs/cap_breakdown.png)
*Proportional contributions: Property Appreciation vs BTC Gains vs Cash*

![Capital Breakdown at Exit](outputs/capital_breakdown.png)
*Absolute dollar contributions at portfolio exit*

### 5. Portfolio Allocation: Start vs End
![Portfolio Pie](outputs/portfolio_pie.png)
*Month 1 vs Month 120 allocation percentages*

---

## 📈 Base Case Results (10-Year Hold)

| Metric | Value |
|--------|-------|
| **Equity Investment** | $94,000,000 |
| **Final Property Value** | $315,820,349 |
| **Final BTC Value** | $24,877,999 |
| **Total Sale Proceeds** | $174,820,349 |
| **IRR** | 8.68% |
| **NPV** | $38,891,861 |

### Capital Gains Breakdown
- **Property Appreciation**: $221,820,349 (68.4%)
- **BTC Gains**: $24,877,999 (7.7%)
- **Cash Distributions**: $14,818,800 (4.6%)
- **Net Gain**: $120,517,148

---

## 🔍 Key Findings

### ✅ **Hybrid Strategy Wins**
- **Best Risk-Adjusted Returns**: Combines stability of real estate with Bitcoin's convexity
- **Enhanced IRR & NPV**: Even conservative BTC assumptions improve overall performance
- **Balanced Effort**: Moderate human effort vs pure real estate's high overhead

### 📊 **Bitcoin's Asymmetric Upside**
- **Liquidity Advantage**: High liquidity vs real estate's capital lockup
- **Minimal Effort**: Passive investment vs active property management
- **Convex Returns**: Volatile but explosive growth potential

### 🏠 **Real Estate Foundation**
- **Stable Appreciation**: Linear, predictable growth
- **Cash Flow Generation**: Steady rental income for BTC accumulation
- **Capital Preservation**: Tangible asset backing

### 💡 **Critical Insight**
> **BTC gains exceeded cash distributions** — showing liquidity in USD terms underperforms vs appreciating assets

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib seaborn yfinance numpy
```

### Run Analysis
```bash
python3 make_report.py
```

This generates all visualizations and updates the analysis documents.

### Generate Alternative Visualizations
```python
# Generate both portfolio composition styles
from portfolio_comp import plot_portfolio_comp
from cardone_analysis import run_hybrid_model

df, _ = run_hybrid_model()

# Line chart (default)
plot_portfolio_comp(df, "outputs/portfolio_comp.png", mode="line")

# Stacked area chart
plot_portfolio_comp(df, "outputs/portfolio_comp_alt.png", mode="stacked")
```

---

## 📁 Project Structure

```
├── 📊 Analysis Files
│   ├── cardone_analysis.py      # Core hybrid model
│   ├── btc_scenarios.py         # Bitcoin regression analysis
│   └── make_report.py           # Main execution script
├── 📈 Visualization Scripts
│   ├── overall.py               # Strategy comparison heatmap
│   ├── portfolio_comp.py        # Composition over time (2 styles)
│   ├── portfolio_pie.py         # Allocation pie charts
│   ├── cap_breakdown.py         # Proportional gains
│   └── capital_breakdown.py     # Absolute gains
├── 📋 Documentation
│   ├── README.md                # This file
│   ├── ANALYSIS.md              # Detailed analysis
│   └── REPORT.md                # Comprehensive report
└── 📊 outputs/                  # Generated visualizations
    ├── overall.png
    ├── btc_regression.png
    ├── portfolio_comp.png       # Line chart
    ├── portfolio_comp_alt.png   # Stacked area chart
    ├── portfolio_pie.png
    ├── cap_breakdown.png
    └── capital_breakdown.png
```

---

## 🎯 Investment Thesis

### The Cardone Strategy
1. **Acquire Cash-Flowing Real Estate** → Generate steady rental income
2. **Accumulate Bitcoin** → Use cash flow to DCA into BTC
3. **Compound Over Time** → Let both assets appreciate and compound

### Why This Works
- **Real Estate** provides stable foundation and cash flow
- **Bitcoin** adds asymmetric upside and liquidity
- **Hybrid** balances risk while maximizing return potential

---

## 📚 Additional Resources

- 📖 [Detailed Analysis](ANALYSIS.md) - Comprehensive strategy breakdown
- 📊 [Full Report](REPORT.md) - Complete technical analysis
- 🔗 [Grant Cardone's Strategy](https://grantcardone.com) - Original inspiration

---

## 🤝 Contributing

This analysis is open-source and welcomes contributions! Areas for improvement:

- Additional Bitcoin halving scenarios
- Different real estate market assumptions  
- Risk-adjusted return calculations
- Tax optimization strategies

---

## ⚠️ Disclaimer

This is educational analysis only. Not financial advice. Past performance doesn't guarantee future results. Always do your own research and consult financial professionals.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**➡️ Bottom Line**: The hybrid model balances the **security of property** with the **convexity of Bitcoin**, producing stable returns with asymmetric upside potential.

*Built with ❤️ for the Bitcoin and Real Estate communities*