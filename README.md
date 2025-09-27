# Cardone Real Estate + Bitcoin Analysis

This repository contains a financial model exploring how Cardone Capital's hybrid
real‑estate‑and‑Bitcoin funds (such as the 10X Boca Raton and 10X Miami River
funds) might perform under a range of assumptions. The model reflects the
strategy described in public sources, in which income‑generating multifamily
properties purchase BTC with monthly cash flow and use long‑term, low‑interest
debt to finance additional Bitcoin purchases.

## Project Background

Grant Cardone’s investment firm has launched several dual‑asset funds that
combine tangible multifamily real estate with a Bitcoin treasury.  For example,
the 10X Miami River Bitcoin Fund is anchored by a 346‑unit Class A property in
Miami and holds roughly \$15 million worth of BTC; it converts a portion of
monthly cash flow into Bitcoin【556331809607434†L28-L37】.  The 10X Boca Raton
Bitcoin Fund involves a 366‑unit property and adds \$100 million (about
1 000 BTC) to the fund’s Bitcoin treasury, reinvesting rental income into BTC【140341013969425†L23-L45】.
By August 2025 Cardone Capital had already purchased 1 000 BTC and planned to
expand its holdings to 4 000 BTC through refinancing and additional fund
raises【300627256761090†L90-L96】.  These funds advertise an 8 % preferred return
and target capital raises between \$150 million and \$200 million【386761112370758†L15-L47】.

The core thesis is that real estate provides stable cash flow, collateral for
long‑term debt and tax advantages, while Bitcoin offers high‑beta upside and a
hedge against inflation.  By combining the two, investors obtain both
stability and potential exponential growth【300627256761090†L62-L88】.

## What This Project Does

The `cardone_analysis.py` script builds a simplified cash‑flow model for such a
hybrid fund.  It allows you to adjust assumptions about rents, expenses,
financing, appreciation, Bitcoin price growth and the percentage of cash flow
devoted to BTC purchases.  The model then:

* Projects monthly net operating income (NOI) from the property.
* Calculates free cash flow after paying interest on debt.
* Allocates a user‑specified share of cash flow to buy Bitcoin at a simulated
  price path and tracks BTC holdings over time.
* Computes remaining cash distributions to investors.
* Performs a sale at the end of the holding period, liquidating the property
  and Bitcoin holdings to determine final proceeds.
* Calculates the investor’s internal rate of return (IRR) and net present
  value (NPV).

You can modify the assumptions by editing the parameters in the `run_hybrid_model`
function call.  The script is written for clarity and should serve as a good
starting point for more sophisticated analyses, such as adding principal
amortization, pref returns or stochastic Bitcoin price simulations.

## Usage

Clone the repository and install the dependencies (``numpy``, ``pandas`` and
``numpy_financial``).  Then run the script directly:

```bash
python cardone_analysis.py
```

Alternatively, import the `run_hybrid_model` function into a notebook or
another script and call it with your own assumptions.  The function returns
both a pandas ``DataFrame`` with monthly results and a summary dictionary.

## Key References

The assumptions in this model are grounded in publicly available information
about Cardone Capital’s hybrid funds:

* **Miami River Fund:**  A 346‑unit multifamily property paired with \$15 million
  in Bitcoin; the fund reinvests part of its monthly cash flow into BTC【556331809607434†L28-L37】.
* **Boca Raton Fund:**  A 366‑unit deal that adds \$100 million (≈1 000 BTC) to the
  Bitcoin treasury and advertises an 8 % preferred return【140341013969425†L23-L68】.
* **BTC Purchase:**  In June 2025 Cardone Capital purchased 1 000 BTC and plans
  to expand to 4 000 BTC by the end of the year【300627256761090†L90-L96】.  They use
  low‑interest refinancing to finance these acquisitions【300627256761090†L90-L96】.
* **Converting Rent to Bitcoin:**  Grant Cardone has noted that converting 12 years
  of rent checks into BTC could have transformed \$160 million into nearly
  \$3 billion【140341013969425†L93-L98】, underpinning the strategy of reinvesting
  rental income into Bitcoin.
