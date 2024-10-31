# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd

# Dataset with season-long QBR and defensive rank for each Super Bowl-winning QB
season_data = {
    "Year": list(range(2004, 2024)),
    "Quarterback": [
        "Tom Brady", "Ben Roethlisberger", "Peyton Manning", "Eli Manning", "Ben Roethlisberger", 
        "Drew Brees", "Aaron Rodgers", "Eli Manning", "Joe Flacco", "Russell Wilson", "Tom Brady", 
        "Peyton Manning", "Tom Brady", "Nick Foles", "Tom Brady", "Patrick Mahomes", "Tom Brady", 
        "Matthew Stafford", "Patrick Mahomes", "Joe Burrow"
    ],
    "Season QBR": [
        67.5, 62.0, 68.8, 54.0, 60.4, 70.6, 67.5, 61.0, 46.8, 63.1, 77.1, 45.0, 79.4, 55.4, 
        71.6, 78.0, 72.5, 63.8, 77.6, 65.2
    ],
    "Defensive Rank": [
        9, 4, 21, 17, 1, 25, 5, 27, 17, 1, 13, 4, 8, 4, 21, 17, 6, 17, 11, 16
    ]
}

# Convert to DataFrame
df_season = pd.DataFrame(season_data)

# Plotting Season QBR vs Defensive Rank
plt.figure(figsize=(12, 8))
plt.scatter(df_season["Season QBR"], df_season["Defensive Rank"], color='b', marker='o')

# Adding QB names with Super Bowl year at each point
for i, txt in enumerate(df_season["Quarterback"]):
    label = f"{txt} ({df_season['Year'][i]})"
    plt.annotate(label, (df_season["Season QBR"][i], df_season["Defensive Rank"][i]), fontsize=9, ha='right')

# Adding title and axis labels
plt.title("Season QBR vs Defensive Rank for Super Bowl Winning Teams (2004–2023)")
plt.xlabel("Season QBR")
plt.ylabel("Defensive Rank (Lower is Better)")
plt.gca().invert_yaxis()  # Invert y-axis to show lower ranks at the top
plt.grid()

# Display the plot
plt.show()
