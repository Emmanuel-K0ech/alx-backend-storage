# NoSQL Project

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [MongoDB Commands](#mongodb-commands)
- [Python Scripts](#python-scripts)
- [Resources](#resources)
- [License](#license)

## Introduction
This project explores the concepts of NoSQL databases, with a focus on MongoDB. The goal is to understand the differences between SQL and NoSQL, how NoSQL databases work, and how to interact with MongoDB using Python.

## Learning Objectives
By the end of this project, you should be able to:
- Understand what NoSQL is and how it differs from SQL databases.
- Explain ACID properties and how they relate to NoSQL databases.
- Understand document storage and the various types of NoSQL databases.
- Describe the benefits of using NoSQL databases.
- Query, insert, update, and delete information in a NoSQL database.
- Use MongoDB for various operations through the command line and Python.

## Requirements
- **MongoDB Version**: MongoDB 4.2 running on Ubuntu 18.04 LTS.
- **Python Version**: Python 3.7 using the PyMongo library (version 3.10).
- **Coding Style**: Your Python code should follow the `pycodestyle` guidelines (version 2.5.*).
- **README**: A `README.md` file is mandatory at the root of your project directory.
- **File Requirements**:
  - All files should end with a new line.
  - The first line of your Python files should be exactly: `#!/usr/bin/env python3`.
  - All Python modules should be documented.
  - All Python functions should be documented.
  - Your Python code should not execute when imported (use `if __name__ == "__main__":`).

## Setup Instructions

### Installing MongoDB 4.2 on Ubuntu 18.04
1. Import the public key for MongoDB:
    ```bash
    wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
    ```

2. Create a list file for MongoDB:
    ```bash
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
    ```

3. Update your package list:
    ```bash
    sudo apt-get update
    ```

4. Install MongoDB:
    ```bash
    sudo apt-get install -y mongodb-org
    ```

5. Start the MongoDB service:
    ```bash
    sudo service mongod start
    ```

6. Verify that MongoDB is running:
    ```bash
    sudo service mongod status
    ```

7. Verify the MongoDB version:
    ```bash
    mongo --version
    ```

### Installing PyMongo
1. Install PyMongo via pip:
    ```bash
    pip3 install pymongo
    ```

2. Verify the installation:
    ```bash
    python3
    >>> import pymongo
    >>> pymongo.__version__
    '3.10.1'
    ```

### Potential Issues
- If you encounter the error: `Data directory /data/db not found`, you can create the directory using:
    ```bash
    sudo mkdir -p /data/db
    ```

- If `/etc/init.d/mongod` is missing, ensure MongoDB is properly installed by following the setup steps.

## MongoDB Commands
Here are a few useful MongoDB shell commands:

- List all databases:
    ```bash
    cat 0-list_databases | mongo
    ```

- Start MongoDB service:
    ```bash
    service mongod start
    ```

## Python Scripts
- Your Python scripts should:
  - Begin with `#!/usr/bin/env python3`.
  - Follow the `pycodestyle` style guidelines.
  - Include documentation for all modules and functions.

### Example Python Script
Here’s an example of a Python script that connects to a MongoDB database and lists all databases:

```python
#!/usr/bin/env python3
"""
This script connects to a MongoDB database and lists all databases.
"""

import pymongo

if __name__ == "__main__":
    # Connect to the MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # List all databases
    databases = client.list_database_names()
    print("Databases:", databases)
```

### How to Run Python Scripts
- Ensure MongoDB is running:
    ```bash
    sudo service mongod start
    ```

- Run the Python script:
    ```bash
    python3 your_script.py
    ```

## Resources
- [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
- [What is NoSQL?](https://www.ibm.com/cloud/learn/nosql-databases)
- [MongoDB with Python Crash Course](https://www.youtube.com/watch?v=J4b_TVYXkKI)
- [MongoDB Tutorial: Insert, Update, Remove, Query](https://www.tutorialspoint.com/mongodb/)
- [Aggregation in MongoDB](https://docs.mongodb.com/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)

## License
This project is licensed under the MIT License.
