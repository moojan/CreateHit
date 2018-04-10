
#######################################################################
#  Author: Moojan Ghafurian  moojan@alumni.psu.edu   www.moojan.com   #
#  Copyright (C) 2016  Moojan Ghafurian                               #
#######################################################################


from boto.mturk.connection import MTurkConnection

def make_mturk_connection ():
    return MTurkConnection(aws_access_key_id='ID',
                           aws_secret_access_key='Secret', 
                           host='mechanicalturk.amazonaws.com') ## mechanicalturk.sandbox.amazonaws.com for the sandbox

def getLayout():
    return 'LAYOUT_ID'
