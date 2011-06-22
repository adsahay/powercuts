#
# Tweet analysis engine for powercuts.in
# Details in README
#

# imports
import urllib2
import datetime
import re
import simplejson as sj

since_id = "75106982176112640" # search tweets more recent than this number

search_api = "http://search.twitter.com/search.json?q=%23powercutindia&since_id=" + since_id
search_response = ''.join(urllib2.urlopen(search_api).readlines())
results_json = sj.loads(search_response)

for tweet in results_json['results']:
    """
    Going through every tweet to analyse and extract useful information
    """
    # exclude old school RT
    if tweet['text'][:3] == 'RT ':
        continue
    
    # exclude tweets from PowerCutsIN
    if 'PowerCutsIN' in tweet['from_user']:
        continue

    # if we came here this tweet is of interest
    print tweet

    # dirty work begins.
    #report = tweet_to_report(tweet)

from helpers.py import IST

def tweet_to_report(tweet):
    """
    This method takes a tweet and returns a dictionary with:
    1) Reporter
    2) Start time
    3) End time
    4) Location
    5) Planned

    All times are in IST.
    """
    date_format_str = '%a, %d %b %Y %H:%M:%S +0000'

    reporter = tweet['from_user']
    start_time = end_time = None
    planned = False # default is unplanned (this is India)

    # TODO: Is this a report of power coming back? in this case, we need to close a previously
    # opened report. Only end time is important here.
    
    # default start time is the tweet time
    # NOTE: must translate to IST
    start_time = datetime.datetime.strptime(tweet['created_at'], date_format_str).astimezone(IST())
    

