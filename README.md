# 📊 E-Commerce Customer Churn Analysis

A data analytics and dashboarding project that explores customer churn behaviour in an e-commerce dataset. The project uses Python for data cleaning, feature engineering, exploratory data analysis, and interactive dashboard development with Plotly Dash.

The goal of this project is to identify patterns related to customer churn, purchasing behaviour, customer lifetime value, engagement, and high-risk customer segments.

---

## 🚀 Project Overview

This project analyzes an e-commerce customer dataset to answer business-focused questions such as:

- Which customer groups generate the highest lifetime value?
- Which countries contribute the most orders?
- How does mobile app usage relate to total orders?
- Which customer segments show higher churn risk?
- How do engagement level, value segment, country, gender, and age group affect churn behaviour?

The notebook also includes an interactive Dash dashboard that allows users to filter the dataset and explore churn insights dynamically.

---

## 🧰 Tech Stack

- **Python**
- **pandas** – data loading, cleaning, and transformation
- **NumPy** – numeric operations
- **Matplotlib** – static visualizations
- **Seaborn** – exploratory visualizations
- **Plotly Express / Plotly Graph Objects** – interactive charts
- **Dash** – interactive web dashboard
- **Dash Bootstrap Components** – responsive dashboard layout
- **ngrok** – optional public sharing of the local dashboard
- **python-dotenv** – environment variable management for ngrok token

---

## 📁 Project Structure

```text
.
├── E-Commerce_Analysis_G5(2).ipynb      # Main Jupyter Notebook
├── e-commerce_churn_clean.csv           # Cleaned dataset generated from the notebook
├── README.md                            # Project documentation
└── .env                                 # Optional: stores NGROK_AUTH_TOKEN locally
```

---

## 📦 Dataset

The project uses an e-commerce customer churn dataset containing customer demographics, engagement metrics, purchase behaviour, payment information, churn status, and signup quarter.

Key columns include:

- `Age`
- `Gender`
- `Country`
- `City`
- `Login_Frequency`
- `Session_Duration_Avg`
- `Pages_Per_Session`
- `Cart_Abandonment_Rate`
- `Wishlist_Items`
- `Total_Orders`
- `Average_Order_Value`
- `Lifetime_Value`
- `Mobile_App_Usage`
- `Social_Media_Engagement_Score`
- `Customer_Service_Calls`
- `Payment_Method_Diversity`
- `Churned`
- `Signup_Quarter`

The notebook loads the raw dataset from GitHub, cleans it, creates new analytical features, and exports a cleaned CSV file.

---

## 🧼 Data Cleaning Steps

The raw dataset is cleaned and prepared using the following steps:

- Renamed `Total_Purchases` to `Total_Orders` for clearer business meaning.
- Removed invalid age values outside the realistic age range.
- Clipped negative or out-of-range values in numeric columns.
- Filled missing `Wishlist_Items` values with `0`.
- Filled missing numeric values using the median.
- Converted selected numeric columns to integer format.
- Rounded decimal columns for cleaner reporting.
- Standardized text values such as country names and abbreviations.
- Removed duplicate rows.
- Exported the cleaned dataset as `e-commerce_churn_clean.csv`.

---

## 🛠️ Feature Engineering

Additional columns were created to make analysis and dashboarding easier:

| Feature | Description |
|---|---|
| `Churn_Status` | Converts churn values into readable labels: `Active` and `Churned`. |
| `Payment_Mode` | Maps payment method codes to names such as Cash, Debit Card, Credit Card, PayPal, and Others. |
| `Age_Group` | Groups customers into age bands such as `18-25`, `26-35`, `36-45`, `46-55`, and `55 and above`. |
| `Engagement_Tier` | Classifies customers into Low, Medium, High, and Very High engagement groups. |
| `Value_Segment` | Segments customers into Bronze, Silver, Gold, and Platinum based on lifetime value. |

---

## 📈 Exploratory Data Analysis

The notebook explores several customer behaviour and churn-related questions.

### Key Analysis Areas

- Average lifetime value by age group
- Total orders by country
- Correlation between numeric variables
- Mobile app usage vs total orders
- Signup trends across quarters
- Customer value segmentation
- Lifetime value contribution by customer segment

---

## 🔍 Key Insights

- The **18-25 age group** has the highest average lifetime value at approximately **$1,446.60**, but the difference across age groups is small.
- The **USA** contributes the largest share of total orders at approximately **34.7%**.
- The **UK** contributes around **15.1%**, while **Canada** contributes around **12.0%**.
- **Japan** has the smallest order share at approximately **5.1%**.
- `Mobile_App_Usage` has a moderate positive relationship with `Total_Orders`, with a correlation of approximately **0.59**.
- Signup volume is fairly balanced across quarters, with **Q3** slightly leading at **12,551 signups**.
- **Platinum customers** have the highest average lifetime value at approximately **$2,690.88**.
- Platinum and Gold customers represent the most valuable segments, making them strong candidates for retention-focused marketing.

---

## 🖥️ Interactive Dashboard

The project includes a professional interactive dashboard built with Dash and Plotly.

### Dashboard Features

- Responsive layout using Dash Bootstrap Components
- Dark theme with custom CSS styling
- KPI cards for high-level business metrics
- Interactive filters for customer segmentation
- Dynamic charts that update based on selected filters
- High-risk churn segment table
- Optional public sharing using ngrok

### Dashboard Filters

Users can filter the dashboard by:

- Country
- Gender
- Age group
- Engagement tier
- Value segment
- Payment mode
- Signup quarter
- Churn status
- Lifetime value range

### Dashboard Visuals

The dashboard includes the following visual components:

- Customer status split donut chart
- Churn rate by country
- Signup trend by quarter
- Churn rate by age group and gender
- Churn heatmap by engagement tier and value segment
- Social media engagement vs session duration scatter plot
- Top cities by churn rate
- Top risk segments table

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn dash dash-bootstrap-components plotly pyngrok python-dotenv
```

---

## ▶️ How to Run the Project

### Option 1: Run the Jupyter Notebook

Start Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```

Then open:

```text
E-Commerce_Analysis_G5(2).ipynb
```

Run the notebook cells from top to bottom.

---

### Option 2: Run the Dash Dashboard from the Notebook

The dashboard runs on port `8050`:

```python
app.run(debug=False, port=8050, jupyter_mode="external")
```

After running the dashboard cell, open the local dashboard URL in your browser.

---

## 🌐 Optional: Share Dashboard with ngrok

To share the local dashboard publicly, create a `.env` file in the project root:

```env
NGROK_AUTH_TOKEN=your_ngrok_auth_token_here
```

Then run the ngrok cell from the notebook:

```python
from pyngrok import ngrok
from dotenv import load_dotenv
import os

load_dotenv()

ngrok_token = os.getenv("NGROK_AUTH_TOKEN")
ngrok.set_auth_token(ngrok_token)

public_url = ngrok.connect(8050)
print("Dash app public URL:", public_url)

app.run(port=8050, debug=False, jupyter_mode="external")
```

To stop the tunnel:

```python
ngrok.kill()
```

---

## 📊 Business Value

This project demonstrates how customer data can be transformed into actionable business insights. By combining data cleaning, exploratory analysis, customer segmentation, and dashboarding, the project helps identify high-value customers, understand churn behaviour, and support data-driven retention strategies.

---

## ✅ Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Customer segmentation
- Churn analysis
- Business insight generation
- Data visualization
- Interactive dashboard development
- Dash callback implementation
- Environment variable handling
- Public dashboard sharing with ngrok

---

## 👤 Authors

- **Gouri Biju**
- **Narjes Atashimsina**
- **Pawan Shukla**
- **Sai Tirupati Voona**
- **Srijana Shrestha**
- **Tesfalem Beyene**
- **Zachary Henry**

