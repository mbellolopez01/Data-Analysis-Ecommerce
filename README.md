# E-Commerce Customer Behavior & Sales Analysis (12M+ Records)

## 📌 Project Overview

This project involved the end-to-end processing and analysis of a massive dataset containing over 12 million raw event records from a multi-category e-commerce platform. The primary goal was to architect a data pipeline capable of transforming millions of individual user interactions (views, cart additions, and purchases) into actionable business intelligence to identify conversion bottlenecks and brand performance.

## 🛠️ Tech Stack

Python (Pandas & PyArrow): Executed a high-performance ETL pipeline to process massive CSV event logs. Utilized PyArrow for efficient schema definition and data type downcasting, significantly reducing the memory footprint of the 12M+ record dataset.

Apache Parquet: Adopted as the primary storage format. By converting raw logs to Parquet, we achieved a 75% reduction in file size and enabled lightning-fast data loading into the visualization layer compared to traditional CSV files.

Power BI / Power Query: Developed a robust data model establishing relationships between events, users, and product categories. Implemented advanced data cleaning steps in Power Query to handle inconsistent brand naming and timestamp formatting.

DAX (Data Analysis Expressions): Engineered complex measures for dynamic business KPIs, including Conversion Rate (CR), Average Order Value (AOV), and User Retention patterns.

## 📊 Key Insights & Visualizations

The interactive Dashboard delivers actionable intelligence on:

Sales Dynamics: Comparative analysis of Revenue vs. Quantity sold across different product categories and brands.

Conversion Funnel: Visual tracking of the user journey from "View" to "Cart" to "Purchase," identifying specific drop-off points.

Temporal Patterns: Heatmaps highlighting peak activity times, revealing that the highest purchase volume occurs during specific midday windows.

Brand Performance: Identification of market leaders and emerging brands based on engagement-to-purchase ratios.

## 🚀 Technical Challenges & Solutions

Scalability: Addressed the challenge of processing millions of rows on standard hardware by implementing chunk-based processing and Parquet indexing.

Data Cleansing: Standardized millions of entries with missing brand information using mapping logic derived from product ID patterns.

Performance Tuning: Optimized DAX measures to ensure that filters for "Category" and "Time Frame" respond instantly, even when querying a 12M-row fact table.

## 📈 Results

Successfully analyzed the behavior of millions of unique users.

Identified key drop-off stages in the shopping cart process, leading to recommended UI/UX improvements.

Provided a scalable, automated reporting system that updates 3x faster than previous spreadsheet-based methods.
