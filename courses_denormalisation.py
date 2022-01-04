import pandas as pd
import json

dfPlayer = pd.read_csv(filepath_or_buffer=r'.\players.csv', sep='	', header=0)
dfLikes = pd.read_csv(filepath_or_buffer=r'.\likes.csv', sep='	', header=0)
dfClears = pd.read_csv(filepath_or_buffer=r'.\clears.csv', sep='	', header=0)
dfPlays = pd.read_csv(filepath_or_buffer=r'.\plays.csv', sep='	', header=0)
dfRecords = pd.read_csv(filepath_or_buffer=r'.\records.csv', sep='	', header=0)
dfCourses = pd.read_csv(filepath_or_buffer=r'.\courses.csv', sep='	', header=0)
dfCourseMeta = pd.read_csv(filepath_or_buffer=r'.\course-meta.csv', sep='	', header=0)

dfCourseMeta['firstClear'] = dfCourseMeta['firstClear'].fillna('')
dfCourseMeta['tag'] = dfCourseMeta['tag'].fillna('')
dfCourses['maker'] = dfCourses['maker'].fillna('')
dfCourses['title'] = dfCourses['title'].fillna('')

dfPlays = dfPlays.set_index(['id','player','catch'])
dfClears = dfClears.set_index(['id','player','catch'])
dfLikes = dfLikes.set_index(['id','player','catch'])
dfRecords = dfRecords.set_index(['id','player','catch','timeRecord'])
dfCourseMeta = dfCourseMeta.set_index(['id','firstClear','catch','clearRate','attempts','clears','tweets','players','stars','tag'])

c1 = dfCourses.to_json(orient='index')
c1 = json.loads(c1)
jsonArray=[]
for c in c1:
    tempObj = c1[c]
    tempObj['playedBy'] = []
    try:
        tempObj['playedBy'] = dfPlays.loc[tempObj['id']].reset_index().to_dict('records')
    except:
        pass
    
    tempObj['clearedBy'] = []
    try:
        tempObj['clearedBy'] = dfClears.loc[tempObj['id']].reset_index().to_dict('records')
    except:
        pass

    tempObj['likedBy'] = []
    try:
        tempObj['likedBy'] = dfLikes.loc[tempObj['id']].reset_index().to_dict('records')
    except:
        pass

    tempObj['recordedBy'] = []
    try:
        tempObj['recordedBy'] = dfRecords.loc[tempObj['id']].reset_index().to_dict('records')
    except:
        pass

    tempObj['courseMeta'] = []
    try:
        tempObj['courseMeta'] = dfCourseMeta.loc[tempObj['id']].reset_index().to_dict('records')
    except:
        pass

    jsonArray.append((tempObj))

with open('./denorm1Courses.json', 'w') as fp:
    json.dump(jsonArray, fp)
