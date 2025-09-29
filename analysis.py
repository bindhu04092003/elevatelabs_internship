import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")

print("Data Preview:")
print(df.head())
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(sales_by_product)
sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(sales_by_region)
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)
sales_by_product.plot(kind="bar", title="Total Sales by Product")
plt.show()

sales_by_region.plot(kind="pie", autopct="%1.1f%%", title="Sales by Region")
plt.show()

monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.show()
