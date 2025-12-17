# Kamino Multiply Strategy Analysis (JitoSOL/SOL Loop)

This repository analyzes the historical performance of the **JitoSOL/SOL Multiply** strategy on Kamino JitoSOL isolated market over the last 12 months (Dec 2024 - Dec 2025).

## 1. Strategy Overview
The strategy involves a recursive loop:
1.  **Deposit JitoSOL** (Earns Staking APY).
2.  **Borrow SOL** (Pays Borrow APY).
3.  **Convert SOL to JitoSOL** and repeat.

**Goal:** Leverage the spread between JitoSOL staking rewards and SOL borrowing costs.
**Risk:** If Borrow APY > Staking APY (Negative Carry), the position loses value.

## 2. Methodology
*   **Data Sources:**
    *   **JitoSOL Staking APY:** Daily Median (Historical).
    *   **SOL Borrow APY:** Hourly Average (Historical).
*   **Timeframe:** Dec 17, 2024 to Dec 17, 2025.
*   **Simulation Logic:**
    *   Data is aligned to **hourly buckets**.
    *   Staking APY is forward-filled from daily data.
    *   **Net APY** is calculated hourly: `(Staking_APY * Leverage) - (Borrow_APY * (Leverage - 1))`.
    *   **Portfolio Value** assumes auto-compounding (geometric growth) of hourly returns.

## 3. Summary
*   **Trend:** The strategy has significantly **deteriorated** in the second half of 2025.
*   **Spread Inversion:** While the **Median** spread is positive (+0.09%), the **Mean** spread is negative (-0.22%) due to high borrow rate spikes.
*   **Leverage Warning:** Currently (Last 3 Months), **leverage > 4x is losing money**.
*   **Safe Haven:** **2x Leverage** remains profitable in all timeframes because the staking yield on the principal outweighs the cost of the small borrowed portion.

---

## 4. Performance Tables (Initial Investment: $1,000)

### 📅 Last 12 Months (Dec '24 - Dec '25)
*Long-term holders are profitable, but low leverage outperformed high leverage.*

| Lev | Avg Net APY | Return % | Profit ($) | Final Value |
|---|---|---|---|---|
| **2x** | **7.38%** | **7.30%** | **$72.97** | **$1072.97** |
| 3x | 7.16% | 6.94% | $69.39 | $1069.39 |
| 4x | 6.94% | 6.62% | $66.23 | $1066.23 |
| 5x | 6.73% | 6.31% | $63.08 | $1063.08 |
| 8x | 6.07% | 5.87% | $58.72 | $1058.72 |
| 10x | 5.63% | 5.73% | $57.26 | $1057.26 |

### 📅 Last 6 Months (Jun '25 - Dec '25)
*Yields declined. High leverage (8x-10x) turned into a loss.*

| Lev | Avg Net APY | Return % | Profit ($) | Final Value |
|---|---|---|---|---|
| **2x** | **5.79%** | **2.85%** | **$28.49** | **$1028.49** |
| 3x | 4.94% | 2.40% | $24.04 | $1024.04 |
| 4x | 4.09% | 1.93% | $19.27 | $1019.27 |
| 5x | 3.24% | 1.40% | $13.96 | $1013.96 |
| 8x | 0.69% | 0.13% | $1.29 | $1001.29 |
| **10x** | **-1.01%** | **-0.47%** | **$-4.70** | **$995.30** |

### 📅 Last 3 Months (Sep '25 - Dec '25)
*Deeply negative spread. Any leverage > 4x is bleeding money.*

| Lev | Avg Net APY | Return % | Profit ($) | Final Value |
|---|---|---|---|---|
| **2x** | **4.76%** | **1.16%** | **$11.57** | **$1011.57** |
| 3x | 3.29% | 0.78% | $7.77 | $1007.77 |
| 4x | 1.81% | 0.37% | $3.67 | $1003.67 |
| **5x** | **0.34%** | **-0.10%** | **$-0.96** | **$999.04** |
| 8x | -4.08% | -1.15% | $-11.52 | $988.48 |
| 10x | -7.03% | -1.60% | $-16.02 | $983.98 |

---

## 5. Key Insights

### The "Negative Carry"
As of late 2025, the cost to borrow SOL (~7.7%) is consistently higher than the yield from staking JitoSOL (~6.2%).
*   **Formula:** `Net = (Yield * L) - (Cost * (L-1))`
*   With Yield < Cost, increasing `L` (Leverage) **mathematically guarantees** a lower (or more negative) return.


> do what you want from this information.

