# SpaceX Launch Analysis
#
# Main question:
# How has SpaceX's launch success rate changed over time?
#
# Sub-question:
# How has the number of SpaceX launches per year changed?


import pandas as pd
import matplotlib.pyplot as plt


# Load the data
data = pd.read_csv("spacex_launches_20251222.csv")


# Prepare the data

# Convert the date column to a date format
data["date_utc"] = pd.to_datetime(data["date_utc"])

# Create a column containing the year
data["Year"] = data["date_utc"].dt.year

# Only keep launches with a known result
data = data[data["success"].isin(["True", "False"])]

# Convert True and False into numbers
# True = 1, False = 0
data["Success"] = (data["success"] == "True").astype(int)


# Analyze the data
# Group launches by year
yearly = data.groupby("Year")

# Count total launches per year
total_launches = yearly.size()

# Count successful launches per year
successful_launches = yearly["Success"].sum()

# Calculate success rate
success_rate = (successful_launches / total_launches) * 100


#  RESULTS
print("\nNumber of launches per year:")
print(total_launches)

print("\nSuccess rate by year:")
print(success_rate.round(1))

print("\nMean annual success rate:",
      round(success_rate.mean(), 1), "%")

print("Median annual success rate:",
      round(success_rate.median(), 1), "%")

print("Standard deviation:",
      round(success_rate.std(), 1))


# GRAPH 1 

plt.plot(success_rate.index,
         success_rate.values,
         marker="o")

plt.xlabel("Year")
plt.ylabel("Success rate (%)")
plt.title("SpaceX Launch Success Rate Over Time")
plt.ylim(0, 105)
plt.grid()

plt.show()


# GRAPH 2 

plt.plot(total_launches.index,
         total_launches.values,
         marker="o")

plt.xlabel("Year")
plt.ylabel("Number of launches")
plt.title("Number of SpaceX Launches Per Year")
plt.grid()

plt.show()




