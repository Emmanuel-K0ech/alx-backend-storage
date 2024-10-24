#!/usr/bin/env python3
""" 11-schools_by_topic.py"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic
    Args:
        mongo_collection: collection object from pymongo
        topic: common factor/criteria to query document
    Return: list(documents)
    """
    return list(mongo_collection.find({"topics": topic}))
