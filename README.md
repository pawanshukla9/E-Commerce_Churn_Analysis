# 📊 E-Commerce Customer Churn Analysis

A data analysis and interactive dashboard project focused on understanding customer churn behavior in an e-commerce business. The project uses Python for data cleaning, exploratory analysis, visualization, and dashboard development with Dash and Plotly.

The analysis explores customer demographics, engagement behavior, purchasing activity, lifetime value, churn trends, and customer value segments to identify patterns that can help improve retention and business decision-making.

---

## 📌 Project Overview

Customer churn is one of the most important metrics for subscription-based and e-commerce businesses. This project analyzes an e-commerce customer dataset to understand which factors are associated with customer churn and how different customer segments behave.

The notebook includes:

- Data loading from a GitHub-hosted CSV file
- Data cleaning and preprocessing
- Feature engineering for customer segmentation
- Exploratory data analysis using pandas, matplotlib, and seaborn
- Correlation analysis between customer behavior variables
- Interactive dashboard development using Dash and Plotly
- Dashboard sharing through ngrok

---

## 🎯 Objectives

The main goals of this project are to:

- Clean and prepare raw e-commerce customer data for analysis
- Understand customer behavior across age groups, countries, quarters, and value segments
- Identify relationships between engagement metrics and purchase activity
- Analyze churn rate across customer segments
- Build an interactive dashboard for exploring churn behavior dynamically
- Present business insights in a clear and visual format

---

## 🧰 Technologies Used

| Category | Tools / Libraries |
|---|---|
| Programming Language | Python |
| Data Manipulation | pandas, NumPy |
| Data Visualization | matplotlib, seaborn, Plotly |
| Dashboarding | Dash, dash-bootstrap-components |
| App Sharing | ngrok, pyngrok |
| Environment Variables | python-dotenv |
| Notebook Environment | Jupyter Notebook |

---

## 📂 Dataset

The project uses an e-commerce customer churn dataset loaded directly from GitHub.

The cleaned dataset contains:

- **49,950 rows**
- **30 columns**

Key columns include:

- `Age`
- `Gender`
- `Country`
- `Login_Frequency`
- `Session_Duration_Avg`
- `Pages_Per_Session`
- `Cart_Abandonment_Rate`
- `Wishlist_Items`
- `Total_Orders`
- `Average_Order_Value`
- `Lifetime_Value`
- `Signup_Quarter`
- `Churned`

---

## 🧹 Data Cleaning Steps

The raw dataset was cleaned and prepared using the following steps:

- Renamed `Total_Purchases` to `Total_Orders`
- Removed invalid age values
- Clipped negative and out-of-range values in selected numeric columns
- Filled missing values in `Wishlist_Items` with `0`
- Filled missing numeric values using column medians
- Converted selected columns to integer data types
- Rounded decimal values where appropriate
- Standardized text formatting
- Standardized country abbreviations
- Removed duplicate rows
- Exported the cleaned data as `e-commerce_churn_clean.csv`

---

## 🏗️ Feature Engineering

New columns were created to make the analysis and dashboard easier to understand:

| Feature | Description |
|---|---|
| `Churn_Status` | Converts churn values into readable labels: `Active` and `Churned` |
| `Payment_Mode` | Maps payment method codes to payment names |
| `Age_Group` | Groups customers into age ranges |
| `Engagement_Tier` | Segments customers based on login frequency |
| `Value_Segment` | Divides customers into Bronze, Silver, Gold, and Platinum segments based on lifetime value |

---

## 📊 Exploratory Data Analysis

The notebook analyzes several business questions, including:

### 1. Which Age Group Spends the Most?

The average lifetime value is very similar across all age groups. The **18-25** age group has the highest average lifetime value at approximately **$1,446.60**, but the difference across age groups is small.

This suggests that age group alone may not be a strong predictor of customer spending behavior.

### 2. Which Country Shops the Most?

The USA contributes the largest share of total orders at approximately **34.7%**. The UK contributes around **15.1%**, Canada contributes around **12.0%**, and Japan has the smallest share at approximately **5.1%**.

### 3. Correlation Analysis

The correlation analysis shows that `Total_Orders` has a strong positive relationship with engagement-related features such as:

- `Session_Duration_Avg`
- `Pages_Per_Session`
- `Mobile_App_Usage`
- `Login_Frequency`

`Lifetime_Value` is also strongly related to `Total_Orders`, while `Cart_Abandonment_Rate` has a negative relationship with `Total_Orders`.

### 4. Mobile App Usage vs Total Orders

The scatter plot shows a moderate positive relationship between mobile app usage and total orders. The correlation between `Mobile_App_Usage` and `Total_Orders` is approximately **0.59**.

This suggests that improving mobile app engagement may help increase customer purchasing activity.

### 5. Signup Trend Across Quarters

Customer signups are almost evenly distributed across all four quarters. Q3 has the highest number of signups with **12,551** customers, but the difference between quarters is small.

### 6. Value Segment Summary

The customer value segmentation separates customers into clear lifetime value groups:

| Segment | Average Lifetime Value |
|---|---:|
| Platinum | $2,690.88 |
| Gold | $1,530.02 |
| Silver | $1,009.79 |
| Bronze | $531.70 |

Platinum customers contribute the highest average lifetime value, while Bronze customers contribute the lowest.

---

## 📈 Interactive Dashboard

The project includes an interactive Dash dashboard for exploring churn behavior across different customer segments.

### Dashboard Filters

Users can filter the dashboard by:

- Country
- Signup Quarter
- Gender
- Age Group

By default, all filter options are selected.

### KPI Cards

The dashboard displays three key performance indicators:

- Total Customers
- Churn Rate
- Average Lifetime Value

When a filter has no selected value or returns no matching records, the KPI cards display `0` and the charts show a clear **"No data is available"** message.

### Dashboard Visuals

The dashboard includes:

| Visual | Purpose |
|---|---|
| Churn Distribution Pie Chart | Shows churned vs active customers |
| Churn Rate by Engagement Tier Bar Chart | Compares churn rate across engagement levels |
| Quarterly Churn vs Retention Line Chart | Tracks churn and retention rates across quarters |
| Engagement × Value Segment Heatmap | Shows churn rate across engagement and value segments |
| Behavior Comparison Subplots | Compares login frequency, session duration, and pages per session for churned vs retained customers |

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Install Required Libraries

```bash
pip install pandas plotly dash dash-bootstrap-components seaborn matplotlib numpy python-dotenv pyngrok
```

### 3. Open the Notebook

```bash
jupyter notebook
```

Then open:

```text
E-Commerce_Analysis_G5(3).ipynb
```

### 4. Run the Notebook Cells

Run the notebook cells from top to bottom to:

1. Load the raw dataset
2. Clean and transform the data
3. Export the cleaned dataset
4. Perform exploratory data analysis
5. Launch the Dash dashboard

### 5. Launch the Dashboard

The dashboard runs locally on:

```text
http://127.0.0.1:8050/
```

---

## 🌐 Sharing the Dashboard with ngrok

The notebook also includes code to share the local Dash dashboard using ngrok.

Create a `.env` file in the project folder and add your ngrok auth token:

```env
NGROK_AUTH_TOKEN=your_ngrok_auth_token_here
```

Then run the ngrok section in the notebook to generate a public dashboard URL.

To stop the tunnel, run:

```python
ngrok.kill()
```
---

## 📌 Key Insights

- Customer spending is similar across age groups, so age alone may not be the strongest churn or revenue indicator.
- The USA contributes the largest share of total orders in the dataset.
- Engagement metrics such as login frequency, session duration, pages per session, and mobile app usage are positively related to total orders.
- Higher cart abandonment is associated with fewer total orders.
- Platinum customers have the highest average lifetime value and represent the most valuable segment.
- Interactive filtering makes it easier to explore churn behavior across demographics and engagement groups.

---

## 👤 Authors

- **Gouri Biju**
- **Narjes Atashimsina**
- **Pawan Shukla**
- **Srijana Shrestha**
- **Tesfalem Beyene**
- **Zachary Henry**

