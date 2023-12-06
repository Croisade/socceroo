import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main () :
    df = pd.read_excel('./matches.xlsx')
    df.reset_index(inplace=True)
    # Step 2: Calculate the Differences
    # df['ShotsOnGoalDifference'] = df['home_shotsOnGoal'] - df['away_shotsOnGoal']
    # df['ScoreDifference'] = df['home_score'] - df['away_score']

    # Step 4: Calculate and Plot the Line of Best Fit
    # Fit the linear model (polynomial of degree 1)
    # m, b = np.polyfit(df['ShotsOnGoalDifference'], df['ScoreDifference'], 1)

    # # Use the slope and intercept to plot the line of best fit
    # plt.plot(df['ShotsOnGoalDifference'], m*df['ShotsOnGoalDifference'] + b, color='red')


    # Step 3: Create the Scatter Plot
    # plt.scatter(df['ShotsOnGoalDifference'], df['ScoreDifference'])
    # plt.xlabel('Shots on Goal')
    # plt.ylabel('Goals')
    # plt.title('Scatter Plot of Shots on Goal Difference vs Goal Difference')
    # plt.savefig('plot.png')
    # plt.close()
    # offRtng = getOffensiveRating(df)
    # defRtng = getDefensiveRating(df)
    # print(defRtng)
    print(getAverageGoalsScored(df))

def getOffensiveRating(data):
    # Step 2: Split and Rename DataFrame
    # For home games
    home_games = data[['index', 'home', 'year', 'home_score']].rename(columns={'home': 'team', 'home_score': 'score'})
    # print(home_games)

    # For away games
    away_games = data[['index', 'away', 'year', 'away_score']].rename(columns={'away': 'team', 'away_score': 'score'})

    # Step 3: Concatenate DataFrames
    all_games = pd.concat([home_games, away_games])

    # Step 4: Filter for the Year 2020
    games_2022 = all_games[all_games['year'] == 2022].sort_values(by='index')
    print(games_2022[games_2022['team'] == 'Philadelphia Union'])

    # Group by team and take the first 5 games
    first_five = games_2022.groupby('team').head(5)

    # Calculate the average score for these games
    avg_score = first_five.groupby('team')['score'].mean()
    return avg_score

def getDefensiveRating(data):
    home_games = data[['index', 'home', 'year', 'away_score']].rename(columns={'home': 'team', 'away_score': 'score'})
    # print(home_games)

    # For away games
    away_games = data[['index', 'away', 'year', 'home_score']].rename(columns={'away': 'team', 'home_score': 'score'})

    # Step 3: Concatenate DataFrames
    all_games = pd.concat([home_games, away_games])

    # Step 4: Filter for the Year 2020
    games_2022 = all_games[all_games['year'] == 2022].sort_values(by='index')
    print(games_2022[games_2022['team'] == 'Philadelphia Union'])

    # Group by team and take the first 5 games
    first_five = games_2022.groupby('team').head(5)

    # Calculate the average score for these games
    avg_score = first_five.groupby('team')['score'].mean()
    return avg_score

def getAverageGoalsScored(data):
    home_games = data[['index', 'home', 'year', 'part_of_competition', 'home_score']].rename(columns={'home': 'team', 'home_score': 'score'})

    away_games = data[['index', 'away', 'year', 'part_of_competition', 'away_score']].rename(columns={'away': 'team', 'away_score': 'score'})

    filtered_home_games = home_games[(home_games['year'] == 2021) & (home_games['part_of_competition'] == ' Regular Season')]

    filtered_away_games = away_games[(away_games['year'] == 2021) & (away_games['part_of_competition'] == ' Regular Season')]

    return filtered_away_games['score'].mean() + filtered_home_games['score'].mean()




main()