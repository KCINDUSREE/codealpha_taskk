import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Employee_ID': ['E001','E002','E003','E004','E005','E006','E007','E008'],
    'Department': ['IT','IT','HR','Finance','Finance','Marketing','Marketing','HR'],
    'Experience_Years': [1,3,2,5,7,4,6,8],
    'Monthly_Salary': [25000,40000,30000,60000,75000,45000,65000,70000],
    'Performance_Score': [60,72,65,85,92,78,88,90]
}

df = pd.DataFrame(data)

print("\nDATASET:\n")
print(df)

print("\nDATA INFO:\n")
print(df.info())

print("\nDESCRIPTIVE STATISTICS:\n")
print(df.describe())

# Experience vs Salary
plt.plot(df['Experience_Years'], df['Monthly_Salary'], marker='o')
plt.xlabel("Experience (Years)")
plt.ylabel("Monthly Salary")
plt.title("Experience vs Salary")
plt.show()

# Salary vs Performance
plt.scatter(df['Monthly_Salary'], df['Performance_Score'])
plt.xlabel("Monthly Salary")
plt.ylabel("Performance Score")
plt.title("Salary vs Performance")
plt.show()

# Check missing values
print("\nMISSING VALUES:\n")
print(df.isnull().sum())
