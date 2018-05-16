#!/usr/bin/python3
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


class DbOperation():
    def __init__(self, dbName):
        client = MongoClient('localhost', 27017)
        self.dbName = dbName
        self.db = client[self.dbName]
        

    def getCollection(self, collection):
        if collection in self.db.collection_names(include_system_collections=False):
            return self.db[collection]


    def dbInsert(self, article):
        articles = self.db['articles']
        article_id = articles.insert_one(article).inserted_id
        return article_id


    def dbFindByCategory(self, category):
        collection = self.getCollection('articles')
        articles = list(collection.find({"categoryPredicted": "placeholderCategory"}))
        new_articles = []
        for article in articles:
            article['_id'] = str(article['_id'])
            new_articles.append(article)
        return new_articles

    def dbFindById(self, id):
        collection = self.getCollection('articles')
        article = collection.find_one({"_id": ObjectId(id)})
        article['_id'] = str(article['_id'])
        return article




if __name__ == '__main__':
    db = DbOperation('newsapp')
    collection = db.getCollection('articles')
    # print(collection.find_one({"_id": ObjectId('5af963201d41c81e212fbf1d')}))
    # print(ObjectId("5af967141d41c82971e8a695").generation_time)
    results = db.dbFindByCategory('sports')
    print(results[0]['url'])
    