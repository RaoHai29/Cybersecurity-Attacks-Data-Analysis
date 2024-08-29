import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('cybersecurity_attacks.csv')

# 1.1 Display the first few rows of the dataset with the column headers
print("First few rows of the dataset:")
print(df.head())

# 1.2 Handle Missing Values
# Drop rows with missing values
df_cleaned = df.dropna()

# Ensure 'Severity Level' is numeric
df_cleaned['Severity Level'] = pd.to_numeric(df_cleaned['Severity Level'], errors='coerce')

# 1.3 When most of the attacks happened (show by month and attack type)
# Convert the Timestamp to datetime
df_cleaned['Timestamp'] = pd.to_datetime(df_cleaned['Timestamp'])

# Extract month and year from the Timestamp
df_cleaned['Month'] = df_cleaned['Timestamp'].dt.month
df_cleaned['Year'] = df_cleaned['Timestamp'].dt.year

# Group by Month and Attack Type
attack_monthly = df_cleaned.groupby(['Year', 'Month', 'Attack Type']).size().unstack().fillna(0)

# Plot the data
plt.figure(figsize=(12, 6))
attack_monthly.plot(kind='bar', stacked=True)
plt.title('Monthly Distribution of Attack Types')
plt.xlabel('Year-Month')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 1.4 Show the packet length distribution for different attack types
plt.figure(figsize=(12, 6))
sns.boxplot(x='Attack Type', y='Packet Length', data=df_cleaned, palette='pastel')
plt.title('Packet Length Distribution by Attack Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Provide 5 unique insights based on the cyber data analysis

# Insight 1: Most frequent attack types
attack_trend = df_cleaned['Attack Type'].value_counts().head(5)
print("\nInsight 1: Top 5 Attack Types:")
print(attack_trend)

# Visualization for Top 5 Attack Types
plt.figure(figsize=(10, 6))
sns.barplot(x=attack_trend.index, y=attack_trend.values, palette='viridis')
plt.title('Top 5 Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insight 2: Most common geo-locations for attacks
geo_location_counts = df_cleaned['Geo-location Data'].value_counts().head(5)
print("\nInsight 2: Top 5 Geo-Locations for Attacks:")
print(geo_location_counts)

# Visualization for Top 5 Geo-Locations
plt.figure(figsize=(12, 6))
sns.barplot(x=geo_location_counts.index, y=geo_location_counts.values, palette='viridis')
plt.title('Top 5 Geo-Locations for Attacks')
plt.xlabel('Geo-location Data')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insight 3: Action taken for different attack types
action_attack = df_cleaned.groupby('Attack Type')['Action Taken'].value_counts().unstack().fillna(0)
print("\nInsight 3: Action Taken for Different Attack Types:")
print(action_attack)

# Visualization for Action Taken for Different Attack Types
plt.figure(figsize=(12, 6))
action_attack.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Action Taken for Different Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Number of Actions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insight 4: Anomaly Scores Distribution by Malware Indicators
plt.figure(figsize=(10, 6))
sns.boxplot(x='Malware Indicators', y='Anomaly Scores', data=df_cleaned, palette='pastel')
plt.title('Anomaly Scores Distribution by Malware Indicators')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insight 5: Distribution of Firewall Logs and Log Source
# Handle Missing Values
df_cleaned = df.dropna(subset=['Firewall Logs', 'Log Source'])

# Aggregate counts for Firewall Logs and Log Source
firewall_log_counts = df_cleaned['Firewall Logs'].value_counts()
log_source_counts = df_cleaned['Log Source'].value_counts()

# Combine the counts into a DataFrame
combined_df = pd.DataFrame({
    'Firewall Logs': firewall_log_counts,
    'Log Source': log_source_counts
}).fillna(0)  # Fill NaN with 0 for categories not present in both columns

# Plot the data
plt.figure(figsize=(14, 7))

# Plot Firewall Logs and Log Source as grouped bars
combined_df.plot(kind='bar', figsize=(14, 7), colormap='viridis', ax=plt.gca())

plt.title('Distribution of Firewall Logs and Log Source')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
