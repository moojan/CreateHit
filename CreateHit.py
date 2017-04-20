#!/usr/bin/env python

import boto,boto3
import os
import sys
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
from boto.mturk.question import HTMLQuestion
from boto.mturk.price import Price
from boto.mturk.layoutparam import LayoutParameter
from boto.mturk.layoutparam import LayoutParameters
from boto.mturk.qualification import PercentAssignmentsApprovedRequirement,Qualifications, Requirement, LocaleRequirement, NumberHitsApprovedRequirement

from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
 
import datetime
import time



try:
    from mturk_credentials import make_mturk_connection
    from mturk_credentials import getLayout
except ImportError:
    try:
        from moojan_mturk import make_mturk_connection
        from moojan_mturk import getLayout
    except ImportError:
        print "error"


connection = make_mturk_connection()
layoutID = getLayout()
def createSeveralHits(numberOfSubjects):
    
    #    HOST = 'mechanicalturk.sandbox.amazonaws.com'
    #    HOST = 'mechanicalturk.amazonaws.com'

    global connection
    global layoutID
    url = 'THE LINK TO THE STUDY'
    title = "TITLE OF THE STUDY"
    description = "DESCRIPTION OF THE STUDY"
    keywords = ["KEYWORDS"]
    amount = 0.4
# game = ExternalQuestion(url, frame_height)
    remaining = numberOfSubjects
    create_hit_result = None
    timestr = time.strftime("%Y%m%d-%H%M%S")
    myfile=open("./HITIDs/"+timestr + '.txt', 'w')      # Saves all the created hits under HITIDS. The name of the file is based on the date and time of creation.
    ####Setting Worker Requirements:
    workerRequirements=Qualifications()
    req1= PercentAssignmentsApprovedRequirement(comparator = "GreaterThan", integer_value = "96",required_to_preview=True)
    workerRequirements.add(req1)
    req2= LocaleRequirement(comparator = "EqualTo",locale ="US",required_to_preview=True)
    workerRequirements.add(req2)
    req3=NumberHitsApprovedRequirement(comparator = "GreaterThan", integer_value = "50",required_to_preview=True)
    workerRequirements.add(req3)
    
   
    while remaining>0:
        no_assignments = min(9, remaining)
        create_hit_result = connection.create_hit(
            title=title,
            description=description,
            keywords=keywords,
            max_assignments=no_assignments,
            hit_layout=layoutID,
            lifetime=6*60*60,
            duration=3*60*60,
            approval_delay=3*60*60*24,
            reward=Price(amount=amount),
            qualifications=workerRequirements)
        remaining -= no_assignments
        myfile.write(create_hit_result[0].HITId+"\n")
        print "No. Assignments: ", no_assignments
        print "Results:", create_hit_result
        print "hit ID:", create_hit_result[0].HITId

num = int(sys.argv[1])
print("Creating %s HITs from layout %s."%(num,layoutID))

createSeveralHits(num)
