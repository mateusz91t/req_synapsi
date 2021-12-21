# MateuszTrzuskowski021370
# 93553b6234ed0b263f6f84e80191318b

import pandas as pd
import numpy as np
import re


actors = pd.read_json('dataset.json')

# split data to actors and movies with actors' indexes
actors.reset_index(inplace=True)
movies = list()

for idx in range(actors['movies'].size):
    for dct in actors['movies'].loc[idx]:
        movies.append({'actor_id': idx, 'movie': dct})

movies = pd.json_normalize(movies)
actors.drop('index', axis=1, inplace=True)

# actors cleaning
actors.sample(n=5)
actors.shape
actors.info(memory_usage='deep')

actors['dob'].count()
actors['dob'] = actors['dob'].astype(np.datetime64)

actors['dod'].count()
actors.loc[~actors['dod'].isna()].count()
actors['dod'].value_counts()
actors.loc[actors['dod'] == '\n']
actors.loc[actors['dod'] == '\n', 'dod'] = np.NaN
actors['dod'] = pd.to_datetime(actors['dod'])

actors['gender'].value_counts()
actors.loc[actors['gender'] == 'm']
actors.loc[actors['gender'] == 'm', 'gender'] = 'M'
actors['gender'] = actors['gender'].astype('category')

# movies cleaning
movies.sample(n=5)
movies.shape
movies.info(memory_usage='deep')

movies.rename(columns={'movie.title':'title', 'movie.year':'year'},
    inplace=True)

mv = movies.copy()
mv.loc[50:100, 'year']
movies.loc[50:100, 'year']

movies['year'].isin([np.NaN, 'None']).value_counts()
movies.loc[movies['year'].isin([np.NaN, 'None', None, '', '11111']), 'year'] = 0
movies['year'] = movies['year'].apply(lambda s: int(re.sub('\t|\n', '', str(s))))
movies['year'] = movies['year'].astype(np.int16)
