import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import os
import time

import numpy as np
import pandas as pd
import json
import glob

from collections import Counter
from collections import defaultdict
import copy

import sqlite3
import json

import pymongo
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')  # DB接続
    db = client['GTO4']                                 # データベースを選択
    collection = db['ranges']                           # コレクションを選択


    # pipeline = [
    #     {"$match": {"board": "AsQh9d"}},
    #     {"$project": {"file_name": {"$substr": ["$board", 0, 8]}}},
    # ]

    # # print(len(list(collection.aggregate(pipeline))))
    # print(list(collection.aggregate(pipeline)))

    pipeline = [
        {"$match": {"board": {"$regex": "^AsQh9d"}}},
        # {"$project": {"board": {"$substr": ["$board", 0, 8]}}},
        {"$project": {"board": {"$substr": ["$board", 8, 10]}}},
        # {"$project": {"$substr": ["$board", 0, 8]}},
    ]
    num_lank = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}

    print(list(collection.aggregate(pipeline)))
    # print({s["board"][6:8] for s in collection.aggregate(pipeline)})
    # print(sorted({s["board"][6:8] for s in collection.aggregate(pipeline) if s["board"] != "AsQh9d"}, key=lambda x: num_lank[x[0]])[::-1])
    # print(sorted({s["board"][8:10] for s in collection.aggregate(pipeline) if len(s["board"]) <= 8}, key=lambda x: num_lank[x[0]])[::-1])
    # print(sorted({s["board"] for s in collection.aggregate(pipeline) }, key=lambda x: num_lank[x[0]])[::-1])
    print(sorted({s["board"] for s in collection.aggregate(pipeline) if s["board"] != ""}, key=lambda x: num_lank[x[0]])[::-1])




    # DB接続を解除
    client.close()
    