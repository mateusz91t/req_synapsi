import pandas as pd
import numpy as np
import re


actors = pd.read_json('dataset.json')


# actors cleaning
actors.sample(n=5)
actors.shape
actors.info(memory_usage='deep')
actors.name.value_counts()

## doubles
actors[actors['name'] == 'Robin Williams']

rw_list = \
actors.loc[actors['name'] == 'Robin Williams', 'movies'][7] + \
actors.loc[actors['name'] == 'Robin Williams', 'movies'][27]
rw_list.sort(key=lambda d: d['title'])
rw_list

to_del = list()

for idx in range(len(rw_list)):
    d = rw_list[idx]
    dy = 'year' in d.keys()
    if dy:
        try:
            int(d['year'])
        except ValueError:
            del d['year']
    for idx2 in range(idx + 1, len(rw_list)):
        d2 = rw_list[idx2]
        if d['title'] == d2['title']:
            d2y = 'year' in d2.keys()
            if dy:
                to_del.append(d2)
            else:
                to_del.append(d)

for d in to_del:
    del rw_list[rw_list.index(d)]

actors[actors['name'] == 'Robin Williams']
actors.drop(labels=actors[actors['name'] == 'Robin Williams'].index[-1], inplace=True)
actors.reset_index(drop=True, inplace=True)

## types
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

# split data to actors and movies with actors' indexes
actors.reset_index(inplace=True)
movies = list()

for idx in range(actors['movies'].size):
    for dct in actors['movies'].loc[idx]:
        movies.append({'actor_id': idx, 'movie': dct})

movies = pd.json_normalize(movies)
actors.drop('index', axis=1, inplace=True)

# movies cleaning
movies.sample(n=5)
movies.shape
movies.info(memory_usage='deep')

movies.rename(columns={'movie.title':'title', 'movie.year':'year'},
    inplace=True)

mvcp = movies.copy()
mvcp.loc[50:100, 'year']
movies.loc[50:100, 'year']

movies['year'].isin([np.NaN, 'None']).value_counts()
movies.loc[movies['year'].isin([np.NaN, 'None', None, '', '11111']), 'year'] = 0
movies['year'] = movies['year'].apply(lambda s: int(re.sub('\t|\n', '', str(s))))
movies['year'] = movies['year'].astype(np.int16)

# save files
actors.to_csv('actors.csv')
movies.to_csv('movies.csv')
