# 📊 Economic Indicators Dashboard

## Overview
This project is a **Dash-based interactive web application** that visualizes historical **economic indicators in the United States** over the past 75 years. The application enables users to explore various economic trends, compare indicators, and analyze recession periods.

## Features
✅ Select multiple economic indicators via a dropdown menu.  
✅ Toggle between **line charts** and **bar charts** for different data representations.  
✅ Adjust the **time range** using a slider to focus on specific years.  
✅ Enable a **recession indicator** to highlight historical recession periods.  
✅ Data preprocessing includes **handling missing values**, **interpolation**, and **forward-filling**.

## Technologies Used
- **Python**
- **Dash** (for interactive web applications)
- **Plotly** (for visualizations)
- **Pandas** (for data handling and preprocessing)
- **Matplotlib & Seaborn** (for exploratory data visualization)

## How to Run Locally
To run this project locally, follow these steps:

## Install Dependencies  
Ensure you have Python installed. Then, install required libraries:
```bash
pip install dash plotly pandas matplotlib seaborn


## Dataset
The dataset consists of historical economic indicators obtained from **FRED (Federal Reserve Economic Data)**. The data includes:
- **Inflation (CPI)**
- **Unemployment Rate**
- **Federal Funds Interest Rate**
- **Personal Savings Rate**
- **Disposable Personal Income**
- **Consumer Price Index (CPI)**
- **PCE Durable and Non-Durable Goods**  
And more.

## Key Visualizations
### ** Time Series Trends**
- Line charts display economic indicators over time, highlighting patterns.
- Recession periods (gray shaded areas) help analyze economic downturns.

### ** Distribution Analysis**
- Histograms show the distribution of key economic metrics.

### ** Correlation Heatmap**
- A **lower-triangle correlation matrix** reveals relationships between indicators.

## Challenges & Solutions
### **Handling Missing Data**
- **Problem:** Some indicators had large gaps.
- **Solution:** Used `forward-fill`, `backward-fill`, and `linear interpolation`.

### **Ensuring Visual Clarity**
- **Problem:** Crowded x-axis labels.
- **Solution:** Used `tickangle=-45` to improve readability.

## Conclusion
This dashboard provides a **data-driven way** to explore economic trends and assess market conditions over time. The ability to toggle indicators and compare trends makes it a useful tool for **students, researchers, and economists**.



## Repository Link
🔗 **[GitHub Repository](https://github.com/wisemichael/economic-indicators-dashboard)**

