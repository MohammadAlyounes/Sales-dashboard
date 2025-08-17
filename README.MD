📊 Overview
[Screenshots in my LinkedIn Profile]

An interactive sales analytics dashboard for executives.

✨ Key Features

* KPI Monitoring: Track sales, margins, and transaction values
* Time Series Analysis: View trends across customizable periods
* Comparative Analysis: MoM, QoQ, YoY performance comparisons
* Multi-dimensional Filtering: Segment by customer demographics, products, and locations
* Drill-down Analysis: Explore detailed data breakdowns

🏗️ Architecture

├── 📂 Data Layer: Loading and transformation (data_load.py, data_wrangling.py)

├── 📂 Business Logic: Metric calculations and configurations (metric.py, metric_config.py)

├── 📂 Presentation: UI components and visualizations (dashboard.py, charts, filters)

└── 📂 Utilities: Formatting helpers (formatting.py)

📊 Usage

1.Select Date Range: Choose periods and comparison type in sidebar

2.Apply Filters: Filter by demographics, products, and location

3.View Metrics: Monitor KPIs in the top metrics bar

4.Analyze Trends: Adjust time granularity for trend analysis

5.Explore Dimensions: Use pie charts for dimensional breakdown

6.Drill Down: Click "Drilldown" for detailed analysis

🔧 Customization

* Add metrics in metric_config.py
* Create new visualizations following existing patterns
* Modify data_load.py to connect to different data sources
