#!/usr/bin/env python3
""" Sort a document """


def schools_by_topic(mongo_collection, topic):
    """ method that returns the list of school having a specific topic"""
    return mongo_collection.find_one({"topic": topic})
