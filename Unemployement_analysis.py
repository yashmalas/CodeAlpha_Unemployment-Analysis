import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Clean column names
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Basic Statistics
print("\nStatistics:")
print(df.describe())

# Average unemployment by state
state_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by State")
print(state_unemployment.sort_values(ascending=False))

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Area",
    y="Estimated Unemployment Rate (%)"
)

plt.title("Urban vs Rural Unemployment")



plt.savefig("urban_rural.png")
plt.show()

monthly = df.groupby(
    df['Date'].dt.month
)['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))

monthly.plot(marker='o')

plt.title("Monthly Unemployment Trend")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True)

plt.savefig("monthly_trend.png")
plt.show()

plt.figure(figsize=(12,6))

state_unemployment.sort_values(
    ascending=False
).head(10).plot(kind='bar')

plt.title("Top 10 States with Highest Unemployment")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()

plt.savefig("top10_states.png")
plt.show()

