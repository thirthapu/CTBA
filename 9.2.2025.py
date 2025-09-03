import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
file_path = "data/livedata-weekly-job-changes-2025-07-23.csv"
df = pd.read_csv(file_path)

#convert date columns to datetime
df["current_job.started_at"] = pd.to_datetime(df["current_job.started_at"], errors = "coerce")
df["previous_job.ended_at"] = pd.to_datetime(df["previous_job.ended_at"], errors = "coerce")

#create a "month" column directly for arrivals vs departures
df["month"] = df.apply(
    lambda row:row["current_job.started_at"]
    if row["arrival/departure"] == "arrival" else row["previous_job.ended_at"],
    axis = 1
).dt.tz_localize(None).dt.to_period("M").dt.start_time #Normalize to start of month and remove timezone

#filter to only 2025
df_2025 = df[df["month"].dt.year == 2025].copy() #work on a copy to avoid warning

#count arrivals and departures by month
monthly_counts = (df_2025.groupby(["month", "arrival/departure"])
                  .size() #counts occurances
                  .reset_index(name = "count") #reset index to turn groupby object into a data frame
                  )

#pivot to arrivals/departure columns
pivot_monthly = monthly_counts.pivot(index = "month", columns = "arrival/departure", values = "count").fillna(0)
#ensure all months in 2025 are represented

#Format x-axis labels as "Mon"
pivot_monthly.index = pivot_monthly.index.strftime("%b") #format as "Jan","Feb","Mar", etc.

#plot monthly bars
pivot_monthly.plot(kind="bar", stacked=False, color=["#382261", "#D4A421"])

plt.title("Monthly Job Arrivals vs. Departures (2025)")
plt.ylabel("Number of Changes")
plt.xlabel("Month")
plt.xticks(rotation=45, ha="right") #rotate x-axis labels for better readability
plt.tight_layout() #adjust layout to prevent clipping
plt.show()

#filter for departures
departures = df[df["arrival/departure"] == "departure"]

#get top 10 companies with the most departures
top_departure_companies = departures["previous_job.company.name"].value_counts().nlargest(10)

#top companies by number of departures
sns.barplot(
    x=top_departure_companies.values, #use values for x-axis
    y=top_departure_companies.index, #use index for y-axis
    hue=top_departure_companies.index,
    dodge=False,
    legend=False,
    palette="coolwarm"
)
plt.title("Top Companies by Number of Departures")
plt.xlabel("Number of Departures")
plt.ylabel("Company")
plt.grid(axis="x", linestyle = "--", alpha=0.5)
plt.show()

#Plot top 10 job functions by number of departures
#get top 10 job functions
departures_by_function = (
    departures["previous_job.company.name"]
    .value_counts()
    .nlargest(10)
    .reset_index()
)
#rename columns for clarity
departures_by_function.columns = ["previous_job.function", "count"]
#barplot with function as hue for distinct colors
sns.barplot(
    data=departures_by_function,
    x="count",
    y="previous_job.function",
    hue="previous_job.function",
    palette= "Reds_r",
    legend=False
)
plt.title("Top 10 Job Functions by Number of Departures")
plt.xlabel("Number of Departures")
plt.ylabel("Job Function")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.show()