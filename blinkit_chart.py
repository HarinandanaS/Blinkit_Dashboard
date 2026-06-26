import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("blinkit_data.csv")
sales = df.groupby("Category")[("Revenue")].sum()
plt.figure(figsize=(8,5))
sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel(" Revenue")
plt.tight_layout()
plt.savefig("blinkit_chart.png")
plt.show()