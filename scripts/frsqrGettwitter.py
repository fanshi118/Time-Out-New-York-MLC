#!/usr/bin/env python
# __author__ = "Yuxiang Zhang, Shi Fan"
# -*- coding: utf-8 -*-
import tweepy
import glob
import csv
import pandas as pd

from settings import *
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def getTwitterIDs(ids=[]):
    for data in glob.glob("../data/*output/part*"):
        f = open(data, 'r')
        csv_reader = csv.reader(f)
        for record in csv_reader:
            ids.append(record[0])
    return list(set(ids))

def getIDsFromCleanData():
	checkins = pd.read_csv("../data/checkinsFinal.csv")
	return checkins.user_id.unique()