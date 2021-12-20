import pandas as pd


actors = pd.read_json('dataset.json')
actors
actors.info()

act = actors.copy()
act
act.info(memory_usage='deep')

act['dob'].count()
act['dob'] = pd.to_datetime(act['dob'])
act['dod'].count()
act.loc[~act['dod'].isna()].count()
act['dod'].value_counts()
act.loc[act['dod'] == '\n']
act.loc[act['dod'] == '\n'] = pd.n
act['dod'] = pd.to_datetime(act['dob'])

act['gender'].value_counts()
act.loc[act['gender'] == 'm']
act.loc[act['gender'] == 'm'] = 'M'
act['gender'] = act['gender'].astype('category')
