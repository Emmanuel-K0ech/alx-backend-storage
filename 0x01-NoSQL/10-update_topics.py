#!/usr/bin/env python3
""" 10-update_topics.py """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name
    Args:
        mongo_collection: collection to be changed
        name(str): school name to update
        topics(list[str]): list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
