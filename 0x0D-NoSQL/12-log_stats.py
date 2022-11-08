#!/usr/bin/env python3
"""  Provides some stats about Nginx logs stored in MongoDB"""

import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    logs = client.logs.nginx
    print(logs.count_documents({}), 'logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        x = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {x}")

    y = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{y} status check")
