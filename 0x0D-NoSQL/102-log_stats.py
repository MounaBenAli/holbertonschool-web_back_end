#!/usr/bin/env python3
"""  Adding the top 10 of the most present IPs in the collection nginx of the database logs:"""

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

    ips = logs.find().sort("ip" -1)
    print("IPs:")
    for ip in ips:
        z = logs.count_documents({"ip": ip})
        print(f"\tip {ip}: {z}")