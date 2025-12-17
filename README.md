# Kamino Multiply Strategy Analysis (JitoSOL/SOL Loop)

This repository analyzes the historical performance of the **JitoSOL/SOL Multiply** strategy on Kamino JitoSOL isolated market over the last 12 months (Dec 2024 - Dec 2025).

## 1. Strategy Overview
The strategy involves a recursive loop ("Looping"):
1.  **Flash Borrow SOL** (e.g., 9x your capital).
2.  **Swap Borrowed SOL → JitoSOL**.
3.  **Deposit JitoSOL** as collateral.
4.  **Borrow SOL** against the collateral to repay the Flash Loan.

**Goal:** Leverage the yield spread between JitoSOL staking rewards and SOL borrowing costs.
**Reality:** You are betting that `Staking APY > Borrow APY`.

## 2. Methodology
*   **Data Sources:**
    *   **JitoSOL Staking APY:** Daily Median (Historical).
    *   **SOL Borrow APY:** Hourly Average (Historical).
*   **Timeframe:** Dec 17, 2024 to Dec 17, 2025.
*   **Simulation Logic:**
    *   **Net APY** calculated hourly: `(Staking_APY * Leverage) - (Borrow_APY * (Leverage - 1))`.
    *   **Portfolio Value** assumes auto-compounding of hourly returns.
    *   *Note: This simulation calculates THEORETICAL returns. Real returns are lower (see Section 6).*

## 3. Summary
*   **Trend:** The strategy has significantly **deteriorated** in the second half of 2025.
*   **Spread Inversion:** While the **Median** spread is positive (+0.09%), the **Mean** spread is negative (-0.22%) due to high borrow rate spikes.
*   **Underperformance:** In almost all recent cases, **this strategy performed WORSE than simply holding JitoSOL (1x).**

---

## 4. Benchmark Comparison (Strategy vs. Simple Staking)

The table below compares the **Strategy Return** (at various leverages) vs. **Benchmark Return** (Just holding JitoSOL with 0 debt).

### 📅 Last 12 Months (Dec '24 - Dec '25)
*Benchmark (1x JitoSOL) earned **~7.60%**. The strategy **UNDERPERFORMED** the benchmark at every leverage level.*

| Lev | Avg Net APY | Return % | vs. Benchmark (1x) |
|---|---|---|---|
| **1x (Benchmark)** | **7.60%** | **7.60%** | **--** |
| 2x | 7.38% | 7.30% | 🔻 -0.30% |
| 5x | 6.73% | 6.31% | 🔻 -1.29% |
| 10x | 5.63% | 5.73% | 🔻 -1.87% |

### 📅 Last 3 Months (Sep '25 - Dec '25)
*Benchmark earned **~1.56%** (6.2% annualized). The strategy lost money at high leverage.*

| Lev | Avg Net APY | Return % | vs. Benchmark (1x) |
|---|---|---|---|
| **1x (Benchmark)** | **6.23%** | **1.56%** | **--** |
| 2x | 4.76% | 1.16% | 🔻 -0.40% |
| 5x | 0.34% | -0.10% | 🔻 -1.66% |
| 10x | -7.03% | -1.60% | 🔻 -3.16% |

---

## 5. Key Insights: The "Negative Carry"

As of late 2025, the cost to borrow SOL (~7.7%) is consistently higher than the yield from staking JitoSOL (~6.2%).
*   **Formula:** `Net = (Yield * L) - (Cost * (L-1))`
*   With Yield < Cost, increasing `L` (Leverage) **mathematically guarantees** a lower (or more negative) return.
*   You are effectively **paying interest** to hold a position that yields less than the interest cost.

## 6. The "Hidden" Costs (Why it's actually worse)
The simulation above is optimistic. Real-world execution includes costs that make the strategy even less attractive:

1.  **Swap Fees & Slippage:**
    *   To create a 10x position, you must Swap SOL → JitoSOL for **9x your initial capital**.
    *   Even with 0.1% slippage, you lose **0.9% of your principal instantly** upon opening.
2.  **Closing Costs:**
    *   To exit, you must Swap JitoSOL → SOL to repay the debt.
    *   You incur another **0.9% loss** (at 10x leverage) due to slippage/fees on the way out.
    *   **Total Round-Trip Cost:** ~1.8% of your principal just to enter and exit.
3.  **Borrow Fees:** Kamino often charges a small origination fee or spread on the borrow rate.

> **Conclusion:** Given the current "Negative Carry" environment (Borrow Rate > Staking Yield) + execution costs, this strategy is currently **inferior to simply staking SOL into JitoSOL.**

> do what you want from this information.
