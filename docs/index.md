# Streaming Revenue Analytics Project

This project demonstrates real-time streaming analytics using Kafka, Python, Pandas, and Matplotlib.

The project processes streaming sales transactions, enriches incoming messages with derived
 business fields, and generates analytical insights from the consumed data.

## Custom Project Overview

For Phase 5, I extended the original streaming analytics example by creating a Revenue Analytics Dashboard.

The dashboard analyzes processed Kafka sales data and produces business intelligence visualizations.

### Custom Enhancements

#### High-Value Order Detection

A new derived field called `high_value_order` was added.

Orders with a total value greater than or equal to $150 are automatically flagged for business monitoring.

#### Revenue Growth Analysis

The project calculates cumulative revenue over time and visualizes revenue growth throughout
 the streaming session.

Output:

* revenue_growth.png

#### Revenue by Course Analysis

Revenue is aggregated by product to identify top-performing courses.

Output:

* course_revenue.png

Key Finding:

* PY-STREAM-005 generated the highest revenue.

#### High-Value Order Distribution

The project analyzes the percentage of high-value transactions compared to regular transactions.

Output:

* high_value_distribution.png

### Key Results

* Total Orders Processed: 50
* High Value Orders: 7
* High Value Percentage: 14.0%
* Total Revenue: $3,835.10
* Top Revenue Course: PY-STREAM-005

### Skills Demonstrated

* Kafka Streaming Analytics
* Data Engineering
* Derived Field Calculations
* Business KPI Analysis
* Revenue Analytics
* Data Visualization with Matplotlib
* Real-Time Business Intelligence

### Generated Visualizations

#### Revenue Growth

![Revenue Growth](../data/output/revenue_growth.png)

#### Revenue by Course

![Revenue by Course](../data/output/course_revenue.png)

#### High Value Order Distribution

![High Value Order Distribution](../data/output/high_value_distribution.png)
