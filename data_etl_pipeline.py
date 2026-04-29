# Optimized loading with specific dtypes
df = pd.read_csv('ecommerce_data.csv', dtype={ 'event_type': 'category', 'brand': 'category', 'product_id': 'int32', 'user_id': 'int32' })

# Feature Engineering: Extracting Time-of-Day Insights
df['event_time'] = pd.to_datetime(df['event_time']) df['hour'] = df['event_time'].dt.hour df['day_name'] = df['event_time'].dt.day_name()

# Calculating Conversion Rate (Purchases / Total Sessions)
total_sessions = df['user_session'].nunique() total_purchases = df[df['event_type'] == 'purchase']['user_session'].nunique() conversion_rate = (total_purchases / total_sessions) * 100

# Key Technical Challenges Solved

Big Data Handling: Managed 12M+ records using Pandas optimization techniques to stay within RAM limits.

Data Consistency: Cleaned and imputed missing values for the brand column based on category patterns.

Event Funneling: Aggregated individual events into unique sessions to map the user journey (View -> Cart -> Purchase).
