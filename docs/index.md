# Streaming Revenue Analytics Project

This project demonstrates real-time streaming analytics using Kafka, Python, Pandas, and Matplotlib.

The project processes streaming sales transactions, enriches incoming messages with derived
 business fields, and generates analytical insights from the consumed data.

## Custom Project

### Dataset

The Kafka producer uses the `sales.csv` dataset.

This dataset contains simulated online course sales transactions. Each record represents a
 customer purchase and includes information about the order, customer, product, region,
  payment method, and quantity purchased.

Main fields include:

* order_id
* datetime
* region_id
* currency_code
* product_id
* unit_price
* quantity
* is_online
* customer_id
* payment_method

The original sales dataset was used as the primary source of streaming messages.

Reference datasets used for validation and enrichment include:

* products.csv
* regions.csv
* currencies.csv
* discount_codes.csv

For Phase 5, I extended the original streaming analytics example by creating a Revenue Analytics Dashboard.

The dashboard analyzes processed Kafka sales data and produces business intelligence visualizations.

### Data Contract

The project uses a data contract to ensure that incoming Kafka messages follow expected business rules.

Required fields include:

* order_id
* datetime
* region_id
* currency_code
* product_id
* unit_price
* quantity

Optional fields include:

* customer_note
* discount_code

Validation rules include:

* region_id must exist in regions.csv
* product_id must exist in products.csv
* currency_code must exist in currencies.csv
* quantity must be greater than zero
* unit_price must be greater than zero

Messages that pass all validation checks are accepted and processed. Messages that fail
validation checks are rejected or skipped.

### Kafka Messages

The Kafka producer streams sales transaction records from the `sales.csv` dataset.

Messages are published to the Kafka topic:

* `streaming-03-analytics-case`

Each message uses the `region_id` field as the Kafka message key.

The producer sends raw transaction data including:

* order_id
* datetime
* region_id
* currency_code
* product_id
* unit_price
* quantity
* customer_id
* payment_method

The original message structure was preserved. However, the consumer later enriches the
 messages with additional derived business fields.

### Consumer Validation

The Kafka consumer validates each incoming message before processing it.

Validation checks include:

* Required fields must be present.
* product_id must match a valid product in `products.csv`.
* region_id must match a valid region in `regions.csv`.
* currency_code must match a valid currency in `currencies.csv`.
* quantity must be greater than zero.
* unit_price must be greater than zero.

When a message passes validation:

* It is accepted.
* Derived fields are calculated.
* The enriched record is written to the output CSV file.
* Running analytics are updated.

When a message fails validation:

* The message is rejected or skipped.
* Validation errors are recorded in the logs.
* The invalid record does not affect analytics results.

Validation helps ensure that only accurate and trusted data is included in the final business analysis.

### Custom Enhancements

### Data Engineering and Enrichment

After a message passes validation, the consumer enriches the data by calculating additional
 business fields.

The following derived fields are created:

* subtotal
* tax_amount
* total
* high_value_order

Reference data from `regions.csv` is used to determine the correct tax rate for each region.

The enrichment process performs the following calculations:

1. Calculate the subtotal using:

   `subtotal = quantity × unit_price`

2. Calculate the tax amount using the regional tax rate.

3. Calculate the final total:

   `total = subtotal + tax_amount`

4. Determine whether the order is a high-value transaction.

A custom enhancement was added during Phase 4:

* `high_value_order = True` when total ≥ $150
* `high_value_order = False` when total < $150

This modification simulates real-world business monitoring where organizations track
important transactions as they occur.

### Streaming Analytics

The project performs streaming analytics while messages are being consumed.

The consumer continuously updates running summary statistics as new sales transactions arrive.

The following metrics are tracked:

* Total Sales Revenue
* Average Sale Amount
* Minimum Sale Amount
* Maximum Sale Amount

For the Phase 5 application, a custom Revenue Analytics Dashboard was developed.

The dashboard performs additional analysis on the processed sales data and generates
business intelligence visualizations.

Analytics generated include:

* Cumulative Revenue Growth
* Revenue by Course
* High-Value Order Distribution

Key findings from the streaming session included:

* Total Revenue: $3,835.10
* Total Orders Processed: 50
* High Value Orders: 7
* High Value Percentage: 14.0%

These analytics demonstrate how streaming data can be transformed into actionable business
 insights in near real time.

### Experiments

This project included both a Phase 4 technical modification and a Phase 5 application of the
learned skills.

#### Phase 4 Modification

A custom derived field called `high_value_order` was added to the consumer enrichment process.

The enhancement introduced a business rule that flags orders with a total value greater than
 or equal to $150.

This modification demonstrated:

* custom business logic
* streaming data enrichment
* derived field engineering
* real-time transaction monitoring

#### Phase 5 Application

The project was extended beyond the original example by creating a Revenue Analytics Dashboard.

A new analytics module called `revenue_dashboard.py` was developed to analyze processed sales data.

The dashboard generated three visualizations:

* Revenue Growth (`revenue_growth.png`)
* Revenue by Course (`course_revenue.png`)
* High Value Order Distribution (`high_value_distribution.png`)

This application transformed the project from a simple streaming validation workflow into a
business intelligence and analytics solution.

### Results

The producer and consumer executed successfully during testing.

Producer Results:

* 50 messages were produced successfully.
* 0 messages were rejected by the producer.

Consumer Results:

* 50 messages were consumed successfully.
* 50 messages were accepted and processed.
* 0 messages were rejected or skipped.

The output CSV file contained:

* Original transaction fields
* Calculated subtotal values
* Calculated tax amounts
* Calculated total values
* The custom `high_value_order` field

The logs showed successful message processing, validation, enrichment, and streaming
analytics updates throughout the execution.

Additional outputs generated during Phase 5 included:

* revenue_growth.png
* course_revenue.png
* high_value_distribution.png

These outputs provided visual evidence of revenue trends, product performance, and
high-value transaction activity.

### Generated Visualizations

#### Revenue Growth

![Revenue Growth](../data/output/revenue_growth.png)

#### Revenue by Course

![Revenue by Course](../data/output/course_revenue.png)

#### High Value Order Distribution

![High Value Order Distribution](../data/output/high_value_distribution.png)

### Interpretation

This project demonstrated the importance of validating, enriching, and analyzing streaming
data as it arrives.

Compared to the original example, the project was enhanced by adding a custom business field
 called `high_value_order` and by developing a Revenue Analytics Dashboard that generated
  business intelligence visualizations.

Through this workflow, I learned that validation is critical because inaccurate or
incomplete messages can negatively impact downstream analytics and business decisions.

I also learned that data enrichment can transform raw transaction records into more useful
 business information by calculating fields such as subtotal, tax amount, total revenue, and
 high-value transaction indicators.

The running analytics provided immediate insight into sales performance while messages were
 being processed. Metrics such as total revenue, average sales, minimum sales, and maximum
 sales helped summarize business activity in real time.

The Revenue Analytics Dashboard provided additional business intelligence by identifying
 revenue trends, top-performing products, and the proportion of high-value transactions.

Key business insights included:

* Revenue increased steadily throughout the streaming session.
* PY-STREAM-005 generated the highest revenue among all products.
* High-value transactions represented 14% of all processed orders.
* A relatively small number of transactions contributed a significant portion of total revenue.

Overall, the project demonstrated how Kafka streaming systems can be combined with
validation, enrichment, analytics, and visualization techniques to support real-time
business decision-making.
