#!/usr/bin/env python3
""" Update a document """


def update_topics(mongo_collection, name, topics):
    """ method to changes all topics of a school document based on the name"""
    name = {'name': name}
    topics = {"$set": {'topics': topics}}
    mongo_collection.update_many(name, topics)
