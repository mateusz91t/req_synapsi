import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta


actors = pd.read_csv('actors.csv', index_col=0)
movies = pd.read_csv('movies.csv', index_col=0)
actors
movies
actors.info()
movies.info()

actors['dob'] = actors['dob'].astype(np.datetime64)
actors['dod'] = actors['dod'].astype(np.datetime64)

# questions
# 1. Who is the oldest actor? - Morgan Freeman: 84
alive = actors['dod'].isnull()
oldest_alive_date = actors.loc[alive]['dob'].min()
actors.loc[actors['dob'] == oldest_alive_date]

# 2. Who is the youngest actor? - Léa Seydoux: 36
youngest_alive_date = actors.loc[alive]['dob'].max()
actors.loc[actors['dob'] == youngest_alive_date]

# 3. How old is the oldest actor? - 84
relativedelta(datetime.now(), oldest_alive_date).years

# 4. How old is the youngest actor? - 36
relativedelta(datetime.now(), youngest_alive_date).years

# 5. Who has the biggest filmography? - Charlie Chaplin: 10
actors.loc[movies['actor_id'].value_counts().index[0]]

# 6. Who's dead for the longest period of time? - Charlie Chaplin
oldest_dead_date = actors.loc[~ alive]['dob'].min()
actors.loc[actors['dob'] == oldest_dead_date]

# 7. Which movie is the oldest one? - The Kid: 1921
exists_date = movies['year'] != 0
oldest_movie_date = movies.loc[exists_date]['year'].min()
movies.loc[movies['year'] == oldest_movie_date]

# 8. List the actors born in the same year (if any).
actors['dobY'] = pd.DatetimeIndex(actors['dob']).year
same_years = [
    y[0]
    for y
    in (actors['dobY'].value_counts() > 1).items()
    if y[1] == True]
actors.loc[actors['dobY'].isin(same_years)].sort_values('dobY')  # DF answer
list(actors.loc[actors['dobY'].isin(same_years)]['name']) # list answer

# 9. How many dead actors do we have in the dataset? - 6
len(actors.loc[actors['dod'].notnull()])

# 10. What's the average age of alive actors in the dataset? - 55.05128205128205
actors['years_since_dob'] = actors.apply(
    lambda row: relativedelta(datetime.now(), row['dob']).years,
    axis=1)
actors.loc[alive]['years_since_dob'].mean()

# 11. What's the average number of movies per actor? - 4.217391304347826
movies['actor_id'].value_counts().mean()
