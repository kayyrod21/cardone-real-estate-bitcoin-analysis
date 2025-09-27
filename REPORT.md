# Real Estate + Bitcoin Portfolio Analysis

This project explores Grant Cardone's strategy of using rental cash flow to accumulate Bitcoin. It compares real estate-only returns versus a hybrid allocation into BTC, modeled under different halving scenarios.

## 1. Total Portfolio Value Under Halving Scenarios
This chart shows how the portfolio grows over 10 years, depending on which Bitcoin halving band (Blue, Green, Yellow, Red) it follows.

![Overall Portfolio](outputs/overall.png)

## 2. Portfolio Composition Over Time
The stack plot illustrates how the share of Bitcoin vs Real Estate evolves. Even small BTC allocations compound over time.

![Portfolio Composition](outputs/portfolio_comp.png)

## 3. Portfolio Allocation: Start vs End
Comparing Year 0 and Year 10. Initially, the portfolio is nearly 100% real estate. By Year 10, Bitcoin has grown to ~7–10% under base case assumptions.

![Portfolio Pie](outputs/portfolio_pie.png)

## 4. Base Case Summary Metrics
These are the outputs from the base case (10% BTC growth, 10-year hold period):

- **Equity Investment**: $94,000,000
- **Final Property Value**: $315,820,349
- **Final BTC Value**: $24,877,999
- **Sale Proceeds**: $174,820,349
- **IRR**: 8.68%
- **NPV**: $38,891,861

## 4b. Capital Gains Breakdown (Base Case)
- **Property Appreciation**: $221,820,349
- **BTC Gains**: $24,877,999
- **Cash Distributions**: $14,818,800
- **Total Value at Exit**: $214,517,148
- **Net Gain (Total – Equity Investment)**: $120,517,148

## 4c. Visual Breakdown of Capital Gains
This stacked bar chart shows the relative contributions of Property Appreciation, BTC Gains, and Cash Distributions.

![Capital Breakdown](outputs/cap_breakdown.png)

## 5. Halving Scenario Metrics
Here we compare outcomes under the HPR (Halving Price Regression) model:

| Scenario | IRR | NPV | Final BTC Value |
|----------|-----|-----|-----------------|
| Blue | 8.18% | $32,784,307 | $3,904 |
| Green | 8.18% | $32,784,307 | $7,808 |
| Yellow | 8.18% | $32,784,307 | $15,617 |
| Red | 8.18% | $32,784,307 | $62,467 |

## 6. Bitcoin Halving Regression Context
The HPR (Halving Price Regression) model smooths out hype cycles and shows a conservative long-term Bitcoin price trajectory. This chart overlays historical BTC prices with the regression bands.

![BTC Regression](outputs/btc_regression.png)

## 7. Key Findings
- Real estate provides stable appreciation and steady cash flow.
- Bitcoin adds asymmetric upside, with convexity tied to the halving cycles.
- Even conservative BTC growth assumptions improve the overall IRR and NPV.
- In optimistic halving scenarios, Bitcoin could eclipse real estate’s contribution.

## 8. Glossary of Financial Metrics
**IRR (Internal Rate of Return):** The annualized rate of return at which the net present value (NPV) of all future cash flows equals zero. In other words, it’s the effective yearly return considering both the size *and* timing of cash flows. Useful for comparing projects.

**NPV (Net Present Value):** The dollar value today of all expected future cash flows (rents, distributions, property sale, Bitcoin liquidation), discounted back at a chosen rate (e.g., loan interest or required return). A positive NPV means the project creates value above its cost of capital.

👉 *Quick takeaway:* IRR tells you the % return. NPV tells you the $ value created today. Both help investors judge if the Real Estate + Bitcoin strategy is attractive.
➡️ **Overall Takeaway**: This hybrid model balances the **security of property** with the **convexity of Bitcoin**, making it a stable bet with asymmetric upside.
