#!/usr/bin/env python3
""" Module 9-insert_school.py"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Args:
        mongo_client: pymongo collection object
        **kwargs: unlimited list of documents to be added
    Return: the new '_id'
    """
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id
