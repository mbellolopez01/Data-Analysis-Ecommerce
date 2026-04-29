E-Commerce Customer Behavior Analysis (12M+ Records)

📌 1. Project Overview

This project focuses on the end-to-end processing, cleaning, and visualization of a large-scale e-commerce dataset containing over 12.1 million user events. The goal was to analyze the customer journey—from product view to purchase—and identify patterns in brand performance, peak activity hours, and conversion rates to drive data-informed marketing strategies.

🛠️ 2. Python: ETL & Technical Analysis

The core of the data processing was handled in Python, focusing on memory optimization and feature engineering to transform raw event logs into a structured analytical format.

Memory Optimization & Cleaning

To handle millions of rows without crashing the environment, we implemented data type downcasting and optimized the loading process.

import pandas as pd

# Optimized loading with specific dtypes
df = pd.read_csv('ecommerce_data.csv', dtype={
    'event_type': 'category',
    'brand': 'category',
    'product_id': 'int32',
    'user_id': 'int32'
})

# Feature Engineering: Extracting Time-of-Day Insights
df['event_time'] = pd.to_datetime(df['event_time'])
df['hour'] = df['event_time'].dt.hour
df['day_name'] = df['event_time'].dt.day_name()

# Calculating Conversion Rate (Purchases / Total Sessions)
total_sessions = df['user_session'].nunique()
total_purchases = df[df['event_type'] == 'purchase']['user_session'].nunique()
conversion_rate = (total_purchases / total_sessions) * 100


Key Technical Challenges Solved

Big Data Handling: Managed 12M+ records using Pandas optimization techniques to stay within RAM limits.

Data Consistency: Cleaned and imputed missing values for the brand column based on category patterns.

Event Funneling: Aggregated individual events into unique sessions to map the user journey (View -> Cart -> Purchase).

📊 3. Power BI: Interactive Dashboard

The processed data was exported to Power BI to create a dynamic business intelligence environment.

Dashboard Components & DAX Measures

Sales Performance: Real-time tracking of Revenue and Total Transactions using DAX measures.

Brand Leaderboard: Comparative analysis of the Top 10 brands by sales volume vs. engagement rate.

Time-Series Analysis: Heatmaps showing the hours of the day with the highest purchase probability.

Funnel Visualization: Identifying the specific stages where most users abandon their shopping carts.

Key Insights

Peak Conversion: Identified that activity peaks between 10 AM and 2 PM, while conversion rates are highest on Tuesdays.

Market Share: Top 5 brands account for more than 40% of the total revenue.

Actionable Data: Built a "Quick-Filter" system to segment performance by specific product categories instantly.

📈 Final Results

Scalability: Created a pipeline capable of processing millions of events in minutes.

Business Impact: Provided a clear view of the "Conversion Funnel," allowing the marketing team to target specific high-drop-off points.

Data Integrity: Standardized 100% of the transaction records for accurate financial reporting.
