import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('./matches.xlsx')
# Step 2: Calculate the Differences
df['ShotsOnGoalDifference'] = df['home_shotsOnGoal'] - df['away_shotsOnGoal']
df['ScoreDifference'] = df['home_score'] - df['away_score']

# Step 4: Calculate and Plot the Line of Best Fit
# Fit the linear model (polynomial of degree 1)
# m, b = np.polyfit(df['ShotsOnGoalDifference'], df['ScoreDifference'], 1)

# # Use the slope and intercept to plot the line of best fit
# plt.plot(df['ShotsOnGoalDifference'], m*df['ShotsOnGoalDifference'] + b, color='red')


# Step 3: Create the Scatter Plot
plt.scatter(df['ShotsOnGoalDifference'], df['ScoreDifference'])
plt.xlabel('Shots on Goal')
plt.ylabel('Goals')
plt.title('Scatter Plot of Shots on Goal Difference vs Goal Difference')
plt.savefig('plot.png')
plt.close()
