import pprint

from IPython.display import clear_output
from pymongo import MongoClient

client = MongoClient("mongodb+srv://anhminh:anhminh@anhminh.fw1fy.mongodb.net/movies_initial?retryWrites=true&w=majority")

pipeline = [
    {
        '$group': {
            '_id':{'language':'$language'},
            'count':{'$sum':1}
            }
    },
        {
        '$sort':{'count':-1} #-1 sort in descending order else 1 #sorted on count
            }
            ]



pipeline1 = [
    {
        '$match': {'language':'Korean, English'}
        }
        ]


pipeline2 = [
    {
        '$sortByCount': '$language'

            },
    {
        '$facet':{
            'top language combinations': [{'$limit':100}],
            'unusual combination shared by':[{
                '$skip':100
            },
                {
                    '$bucketAuto':{
                        'groupBy':"$count",
                        'buckets':5,
                        'output':{
                            'language combinations':{'$sum':1}
                        }
                    }
                }
            ]
        }
    }


]
clear_output()
pprint.pprint(list(client.anhminh.movies_initial.aggregate(pipeline2)))