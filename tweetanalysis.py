#
# Tweet analysis engine for powercuts.in
# Details in README
#

# imports
import urllib2
import re
import simplejson as sj

# crude regex for detecting presence of a time in the tweet text
time_regex = re.compile(r'\d{2,}[^a-zA-z]*\d{2,}')

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

    # if there's no "time" in the tweet skip
    if not re.search(time_regex, tweet['text']):
        continue

    # if we came here this tweet is of interest
    print tweet['from_user'] + ': ' + tweet['text']
