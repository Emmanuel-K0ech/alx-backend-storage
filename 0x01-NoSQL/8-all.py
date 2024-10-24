#!/usr/bin/env python3
""" Module 8-all.py (NoSQL)"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    Args
        mongo_collection: collection of documents to be passed
    Return: List of documents in the collection else empty list
    """
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find()
