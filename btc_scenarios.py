# btc_scenarios.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def plot_btc_regression(save_path="outputs/btc_regression.png"):
    # Download BTC price history
    btc = yf.download("BTC-USD", start="2010-01-01")[["Close"]].dropna()
    btc["Days"] = (btc.index - btc.index.min()).days

    # Regression on log-log
    x = np.log(np.arange(1, len(btc) + 1)).flatten()
    y = np.log(btc["Close"].values).flatten()
    coeffs = np.polyfit(x, y, 1)
    poly = np.poly1d(coeffs)

    # Generate extended future timeline (to 2035)
    future_dates = pd.date_range(start=btc.index.min(), end="2035-01-01", freq="D")
    future_x = np.log(np.arange(1, len(future_dates) + 1))

    # Base regression
    base = np.exp(poly(future_x))

    # Apply vertical offsets (log-space shifts)
    curves = {
        "HPR Base": base,
        "HPR +1yr": np.exp(np.log(base) + 0.5*np.log(2)),  # smaller offset
        "HPR +2yr": np.exp(np.log(base) + 1*np.log(2)),
        "HPR +3yr": np.exp(np.log(base) + 1.5*np.log(2)),
        "HPR +4yr": np.exp(np.log(base) + 2*np.log(2)),
    }

    # Plot
    plt.figure(figsize=(12, 7))
    plt.plot(btc.index, btc["Close"], color="black", label="BTC Price", linewidth=1.8)

    colors = ["blue", "green", "yellow", "orange", "red"]
    for (label, series), c in zip(curves.items(), colors):
        plt.plot(future_dates, series, color=c, label=label, linewidth=1.5)

    # Halving events
    halvings = ["2020-05-11", "2024-04-20", "2028-04-10", "2032-04-01"]
    for h in halvings:
        plt.axvline(pd.to_datetime(h), linestyle="--", color="cyan", alpha=0.7)

    plt.xlim(pd.to_datetime("2020-01-01"), pd.to_datetime("2035-01-01"))
    plt.yscale("log")

     # Y-axis zoom (cut empty log space)
    ymin = float(btc["Close"].loc["2020-01-01":].min()) * 0.8
    ymax = float(max(curves["HPR +4yr"])) * 1.2
    plt.ylim(ymin, ymax)


    plt.title("Bitcoin Regression Model with Extended Rainbow (2020–2035)")
    plt.ylabel("BTC Price (Log Scale)")
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)

    plt.savefig(save_path, dpi=200)
    plt.close()
