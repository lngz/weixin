#!/usr/bin/python
# -*-  coding: UTF-8 -*-

import sys
import urllib2
import json

reload(sys)
sys.setdefaultencoding('UTF-8')

# store params passed Splunk as optional alert properties
'''
$1 = number of events returned
$2 = search terms
$3 = fully qualified search string
$4 = name of the saved search
$5 = the reason the action/script was triggered (for example, the number of events returned was >1)
$6 = a link to the saved search in Splunk +
$7 = a list of the tags belonging to this saved search (this option was removed starting in Splunk 3.6)
$8 = path to a file where raw results of this search are located (as opposed to passing the actual results into the ticket--this could be a lot of data).
'''
userid = '2377600462'



if len(sys.argv) < 8 :
   sys.exit(-1)

details = {
   "numberOfEvents":sys.argv[1],
   "terms":sys.argv[2],
   "query":sys.argv[3],
   "searchName":sys.argv[4],
   "reason":sys.argv[5],
   "url":sys.argv[6],
   "tags":sys.argv[7],
   "result":sys.argv[8],
}

jdata = json.dumps(details)

alerturl = "http://3.splunk.sinaapp.com/sendmsg/" + userid
response = urllib2.urlopen(alerturl, jdata)

# splunkalert = json.loads(jdata)

# details = "搜索%s发出告警，搜索事件%s条" % (splunkalert["numberOfEvents"], splunkalert["searchName"])
