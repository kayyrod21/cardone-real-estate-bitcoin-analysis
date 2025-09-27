"""
btc_scenarios.py

Generate Bitcoin Halving Price Regression (HPR) paths for scenario analysis.
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# -----------------------------
# Halving dates (for plotting)
# -----------------------------
halving_dates = [
    datetime.datetime(2012, 11, 28),
    datetime.datetime(2016, 7, 9),
    datetime.datetime(2020, 5, 11),
    datetime.datetime(2024, 4, 20),  # latest halving
]

# -----------------------------
# 1. HPR Formula
# log10(price) = 2.6521 * ln(x) - 18.163
# -----------------------------
def hpr_price(days_since_genesis):
    # Avoid log(0)
    days_since_genesis = np.where(days_since_genesis <= 0, 1, days_since_genesis)
    # Apply regression formula
    return 10 ** (2.6521 * np.log(days_since_genesis) - 18.163)
# -----------------------------
# 2. Generate Forward Projections
# -----------------------------
def generate_hpr_paths(years_ahead=10):
    start_date = datetime.datetime(2010, 1, 1)  # Bitcoin genesis
    end_date = datetime.datetime.today() + datetime.timedelta(days=365 * years_ahead)
    dates = pd.date_range(start_date, end_date, freq="ME")  # monthly end

    days = (dates - start_date).days
    days = np.where(days == 0, 1, days)  # avoid log(0) error

    base = hpr_price(days)
    blue = base
    green = base * 2   # ~1 year ahead
    yellow = base * 4  # ~2 years ahead
    orange = base * 8  # ~3 years ahead
    red = base * 16    # ~4 years ahead

    df = pd.DataFrame({
        "Date": dates,
        "Blue": blue,
        "Green": green,
        "Yellow": yellow,
        "Orange": orange,
        "Red": red
    })
    df.set_index("Date", inplace=True)
    return df

# -----------------------------
# 3. Plot Historical vs HPR
# -----------------------------
def plot_hpr():
    btc = yf.download("BTC-USD", start="2010-01-01")["Close"].to_frame("BTC_Price")
    hpr_df = generate_hpr_paths(15)

    plt.figure(figsize=(10,6))
    plt.plot(btc.index, btc["BTC_Price"], label="BTC Price", color="black")
    plt.plot(hpr_df.index, hpr_df["Blue"], label="HPR Base (Blue)", color="blue")
    plt.plot(hpr_df.index, hpr_df["Green"], label="Green (1 yr ahead)", color="green")
    plt.plot(hpr_df.index, hpr_df["Yellow"], label="Yellow (2 yr ahead)", color="gold")
    plt.plot(hpr_df.index, hpr_df["Orange"], label="Orange (3 yr ahead)", color="orange")
    plt.plot(hpr_df.index, hpr_df["Red"], label="Red (4 yr ahead)", color="red")
    for h in halving_dates:
        plt.axvline(h, color="cyan", linestyle="--", alpha=0.6)

    plt.yscale("log")
    plt.title("Bitcoin Historical Price vs Halving Price Regression")
    plt.xlabel("Date")
    plt.ylabel("BTC Price (Log Scale)")
    plt.legend()
    plt.tight_layout()

    # ✅ Save, no show
    plt.savefig("outputs/btc_regression.png")
    plt.close()


if __name__ == "__main__":
    btc = yf.download("BTC-USD", start="2010-01-01")["Close"]

    hpr_df = generate_hpr_paths(15)

    plt.figure(figsize=(10,6))
    plt.plot(btc.index, btc, label="BTC Price", color="black")
    plt.plot(hpr_df.index, hpr_df["Blue"], label="HPR Base (Blue)", color="blue")
    plt.plot(hpr_df.index, hpr_df["Green"], label="Green (1 yr ahead)", color="green")
    plt.plot(hpr_df.index, hpr_df["Yellow"], label="Yellow (2 yr ahead)", color="gold")
    plt.plot(hpr_df.index, hpr_df["Orange"], label="Orange (3 yr ahead)", color="orange")
    plt.plot(hpr_df.index, hpr_df["Red"], label="Red (4 yr ahead)", color="red")

    anchors = {
        "2012-11-28": 12.33,
        "2016-07-09": 651.94,
        "2020-05-11": 8591.65,
    }
    for date, price in anchors.items():
        plt.scatter(pd.to_datetime(date), price, color="red", zorder=5)

    plt.yscale("log")
    plt.title("Bitcoin Historical Price vs HPR Model")
    plt.xlabel("Date")
    plt.ylabel("BTC Price (Log Scale)")
    plt.legend()
    plt.tight_layout()

    # ✅ Save, no show
    plt.savefig("outputs/btc_regression.png")
    plt.close()
