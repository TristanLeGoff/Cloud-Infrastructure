import pandas as pd
import json
import time
import numpy as np

dfPlayer = pd.read_csv(filepath_or_buffer=r'.\players.csv', sep='	', header=0)

dfLikes = pd.read_csv(filepath_or_buffer=r'.\likes.csv', sep='	', header=0)

dfClears = pd.read_csv(filepath_or_buffer=r'.\clears.csv', sep='	', header=0)

dfPlays = pd.read_csv(filepath_or_buffer=r'.\plays.csv', sep='	', header=0)

dfRecords = pd.read_csv(filepath_or_buffer=r'.\records.csv', sep='	', header=0)

dfCourses = pd.read_csv(filepath_or_buffer=r'.\courses.csv', sep='	', header=0)

dfCourseMeta = pd.read_csv(filepath_or_buffer=r'.\course-meta.csv', sep='	', header=0)

dfCourses['maker'] = dfCourses['maker'].fillna('')
dfPlayer['name'] = dfPlayer['name'].fillna('')

dfPlays = dfPlays.set_index(['player','id','catch'])
dfClears = dfClears.set_index(['player','id','catch'])
dfCourses = dfCourses.set_index(['maker','id'])

tempPlayers = dfPlayer.iloc[0:100000]
c1 = tempPlayers.to_json(orient='index')
c1 = json.loads(c1)
jsonArray=[]
start_time = time.time()
for p in c1:
    tempObj = c1[p]
    tempObj['plays'] = []
    try:
        tempObj['plays'] = dfPlays.loc[tempObj['id']].reset_index().to_dict('records')
    except:
        pass

    tempObj['clears'] = []
    try:
        tempObj['clears'] = dfClears.loc[tempObj['id']].reset_index().to_dict('records')
    except:
            pass

    tempObj['maker'] = []        
    try:
        tempObj['maker'] = list(dfCourses.loc[tempObj['id']].index.values)
    except:
            pass
    jsonArray.append((tempObj))

print("--- %s seconds ---" % (time.time() - start_time))

with open('./playerDenorm.json', 'w') as fp:
    json.dump(jsonArray, fp)
