import requests
import pandas as pd
from tabulate import tabulate

# JITO-SOL ISOLATED MARKET
# 1. Fetch Data (Last 365 Days)
print("Fetching JitoSOL data...")
jito_url = 'https://api.kamino.finance/kamino-market/H6rHXmXoCQvq8Ue81MqNh7ow5ysPa1dSozwW3PU1dDH6/reserves/F9HdecRG8GPs9LEn4S5VfeJVEZVqrDJFR6bvmQTi22na/borrow-and-staking-apys/history/median?env=mainnet-beta&start=2024-12-17&end=2025-12-18'
jito_resp = requests.get(jito_url).json()

print("Fetching SOL data...")
sol_url = "https://api.kamino.finance/kamino-market/H6rHXmXoCQvq8Ue81MqNh7ow5ysPa1dSozwW3PU1dDH6/reserves/6gTJfuPHEg6uRAijRkMqNc9kan4sVZejKMxmvx2grT1p/metrics/history?env=mainnet-beta&start=2024-12-17&end=2025-12-18&frequency=hour"
sol_resp = requests.get(sol_url).json()

# 2. Process DataFrames
jito_data = [{'timestamp': i['createdOn'], 'staking_apy': float(i['stakingApy'])} for i in jito_resp]
df_jito = pd.DataFrame(jito_data)
df_jito['timestamp'] = pd.to_datetime(df_jito['timestamp'])
df_jito = df_jito.set_index('timestamp').sort_index()

sol_data = [{'timestamp': i['timestamp'], 'borrow_apy': float(i['metrics']['borrowInterestAPY'])} for i in sol_resp['history']]
df_sol = pd.DataFrame(sol_data)
df_sol['timestamp'] = pd.to_datetime(df_sol['timestamp'])
df_sol = df_sol.set_index('timestamp').sort_index()

# 3. Merge & Align
df = df_sol.join(df_jito, how='left')
df['staking_apy'] = df['staking_apy'].ffill()
df = df.dropna()

print(f"Total Data Points: {len(df)} hours")
print(f"Date Range: {df.index.min()} to {df.index.max()}")

# 4. Simulation Function
def run_simulation(data, title):
    print(f"\n================ {title} ================")
    print(f"Period: {data.index.min()} -> {data.index.max()}")
    print(f"Duration: {(data.index.max() - data.index.min()).days} days")
    
    # Rate Analysis
    mean_staking = data['staking_apy'].mean()
    mean_borrow = data['borrow_apy'].mean()
    mean_spread = mean_staking - mean_borrow
    
    print(f"Avg Staking APY: {mean_staking*100:.2f}%")
    print(f"Avg Borrow APY:  {mean_borrow*100:.2f}%")
    print(f"Avg Spread:      {mean_spread*100:.2f}%")
    print("---")
    
    leverages = [2, 3, 4, 5, 8, 10]
    initial_investment = 1000
    results = []
    
    # We need a copy to avoid SettingWithCopy warnings on the slice
    sim_df = data.copy()
    
    for lev in leverages:
        col_net_apy = f'net_apy_{lev}x'
        col_port = f'portfolio_{lev}x'
        
        # Net APY Calculation
        sim_df[col_net_apy] = (sim_df['staking_apy'] * lev) - (sim_df['borrow_apy'] * (lev - 1))
        
        # Hourly Rate & Compounding
        hourly_rate = (1 + sim_df[col_net_apy]) ** (1 / (365 * 24)) - 1
        sim_df[col_port] = initial_investment * (1 + hourly_rate).cumprod()
        
        final_val = sim_df[col_port].iloc[-1]
        profit = final_val - initial_investment
        return_pct = (profit / initial_investment) * 100
        
        # # Max Drawdown
        # rolling_max = sim_df[col_port].cummax()
        # drawdown = (sim_df[col_port] - rolling_max) / rolling_max
        # max_dd = drawdown.min() * 100
        
        results.append({
            'Lev': f"{lev}x",
            'Avg Net APY': f"{sim_df[col_net_apy].mean()*100:.2f}%",
            'Return %': f"{return_pct:.2f}%",
            'Profit ($)': f"${profit:.2f}",
            'Final Value': f"${final_val:.2f}",
            # 'Max DD': f"{max_dd:.2f}%"
        })
        
    df_results = pd.DataFrame(results)
    print(tabulate(df_results, headers="keys", tablefmt="github", showindex=False))

# 5. Define Time Windows
end_date = df.index.max()

# 12 Months (Full Data)
run_simulation(df, "Last 12 Months")

# 6 Months
start_6m = end_date - pd.DateOffset(months=6)
df_6m = df[df.index >= start_6m]
run_simulation(df_6m, "Last 6 Months")

# 3 Months
start_3m = end_date - pd.DateOffset(months=3)
df_3m = df[df.index >= start_3m]
run_simulation(df_3m, "Last 3 Months")
