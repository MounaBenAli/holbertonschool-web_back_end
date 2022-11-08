#!/usr/bin/env python3
""" Find an element inside a document """


def schools_by_topic(mongo_collection, topic):
    """ method that returns the list of school having a specific topic"""
    return mongo_collection.find({ "topics": topic })

