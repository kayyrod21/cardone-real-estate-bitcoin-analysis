"""
cardone_analysis.py

Hybrid Real Estate + Bitcoin fund model with optional Halving Price Regression (HPR) scenarios.
"""

import numpy as np
import pandas as pd
from numpy_financial import irr


def run_hybrid_model(
    property_value: float = 235_000_000.0,
    num_units: int = 366,
    monthly_rent_per_unit: float = 4000.0,
    occupancy_rate: float = 0.95,
    expense_ratio: float = 0.40,
    loan_to_value: float = 0.60,
    annual_interest_rate: float = 0.05,
    property_appreciation_rate: float = 0.03,
    btc_allocation_rate: float = 0.50,
    initial_btc_units: float = 0.0,
    btc_start_price: float = 50_000.0,
    btc_growth_rate: float = 0.10,
    hold_period_years: int = 10,
    btc_projection: list[float] | None = None,
) -> tuple[pd.DataFrame, dict]:
    """
    Simulate cash flows and Bitcoin accumulation for a hybrid real-estate-plus-BTC fund.

    If btc_projection is passed (list/array of BTC prices per month),
    it overrides btc_growth_rate and drives BTC price evolution.
    """

    months = hold_period_years * 12

    monthly_btc_growth = (1.0 + btc_growth_rate) ** (1.0 / 12.0) - 1.0
    monthly_property_appreciation = (1.0 + property_appreciation_rate) ** (1.0 / 12.0) - 1.0
    monthly_interest_rate = annual_interest_rate / 12.0

    debt_principal = property_value * loan_to_value
    equity_investment = property_value - debt_principal
    monthly_interest_payment = debt_principal * monthly_interest_rate

    property_value_current = property_value
    btc_price = btc_start_price
    btc_units = initial_btc_units

    property_values, btc_prices, btc_units_list, btc_values = [], [], [], []
    cash_distributions, free_cash_flows = [], []

    for month in range(months):
        # Property appreciation
        property_value_current *= 1.0 + monthly_property_appreciation
        property_values.append(property_value_current)

        # NOI
        gross_rent = num_units * monthly_rent_per_unit * occupancy_rate
        operating_expenses = gross_rent * expense_ratio
        noi = gross_rent - operating_expenses

        # Free cash flow after debt
        free_cash_flow = noi - monthly_interest_payment

        # BTC purchase
        btc_purchase_cash = max(free_cash_flow, 0.0) * btc_allocation_rate
        btc_units_purchased = btc_purchase_cash / btc_price if btc_price > 0.0 else 0.0
        btc_units += btc_units_purchased
        btc_units_list.append(btc_units)

        # Investor distributions
        cash_distribution = max(free_cash_flow, 0.0) * (1.0 - btc_allocation_rate)
        cash_distributions.append(cash_distribution)

        free_cash_flows.append(max(free_cash_flow, 0.0))

        # BTC price evolution
        if btc_projection is not None and month < len(btc_projection):
            btc_price = btc_projection[month]
        else:
            btc_price *= 1.0 + monthly_btc_growth
        btc_prices.append(btc_price)

        btc_values.append(btc_units * btc_price)

    # Exit
    final_property_value = property_value_current
    debt_payoff = debt_principal
    sale_proceeds = final_property_value - debt_payoff
    final_btc_value = btc_units * btc_price

    cash_flow_sequence = [-equity_investment] + cash_distributions
    cash_flow_sequence[-1] += sale_proceeds + final_btc_value

    internal_rate = irr(cash_flow_sequence)
    annual_irr = internal_rate * 12.0 if internal_rate is not None else None

    discount_rate = annual_interest_rate / 12.0
    npv = sum(cf / ((1.0 + discount_rate) ** i) for i, cf in enumerate(cash_flow_sequence))

    df = pd.DataFrame({
        "Month": np.arange(1, months + 1),
        "Property_Value": property_values,
        "BTC_Price": btc_prices,
        "BTC_Units": btc_units_list,
        "BTC_Value": btc_values,
        "Cash_Flow_to_Investors": cash_distributions,
        "Free_Cash_Flow": free_cash_flows,
    })

    summary = {
        "Equity_Investment": equity_investment,
        "Final_Property_Value": final_property_value,
        "Final_BTC_Value": final_btc_value,
        "Sale_Proceeds": sale_proceeds,
        "IRR": annual_irr,
        "NPV": npv,
        "Total_Cash_Distributions": sum(cash_distributions),
    }

    return df, summary


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from btc_scenarios import generate_hpr_paths

    # Run base case with normal growth
    df, summary = run_hybrid_model()
    print("\n=== Base Case (10% BTC Growth) ===")
    print(df.head())
    print(summary)

    # Run Halving scenarios
    hpr_df = generate_hpr_paths(10)

    for scenario in ["Blue", "Green", "Yellow", "Red"]:
        btc_projection = hpr_df[scenario].values[:120]
        df_s, summary_s = run_hybrid_model(btc_projection=btc_projection)
        print(f"\n=== {scenario} Scenario ===")
        print(summary_s)

        plt.plot(df_s["Month"], df_s["BTC_Value"], label=f"{scenario} BTC Value")

    plt.title("BTC Value Under Halving Scenarios")
    plt.xlabel("Month")
    plt.ylabel("USD")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/btc_regression.png")
    plt.close()