#!/usr/bin/env python3
""" Insert a document """


def insert_school(mongo_collection, **kwargs):
    """ method to insert a new document in a collection based on kwargs:"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
