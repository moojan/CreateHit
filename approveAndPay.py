
#######################################################################
#  Author: Moojan Ghafurian  moojan@alumni.psu.edu   www.moojan.com   #
#  Copyright (C) 2017  Moojan Ghafurian                               #
#######################################################################


import glob, os
import boto,boto3
import sys
from boto.mturk.connection import MTurkConnection
import csv

try:
    from mturk_credentials import make_mturk_connection
except ImportError:
    try:
        from moojan_mturk import make_mturk_connection
    except ImportError:
        from sample import make_mturk_connection

connection = make_mturk_connection()

bonuses=getBonuses()
HIT=getHIT()

def approveAndPay(HitID, pay):
    global connection
    print ("Approving Workerss for HIT ID" + HitID)
    if (!pay):
        print ("This is a TEST run.")
    if (pay):
        print ("This is a REAL run")
    assignments = connection.get_assignments(HitID, sort_by='SubmitTime', sort_direction='Ascending')
    with open('../payment.csv', 'a') as csvoutput:
        writer = csv.writer(csvoutput)
        for assignment in assignments:
            mturkID = assignment.WorkerId
            assignmentID=assignment.AssignmentId
            if (pay):
                approve_assignment(AssignmentId, feedback=None)
                grant_bonus(mturkID, AssignmentId, bonuses[mturkID], "")
            print ("approved assignment for" + mturkID + "and paid a bonus of"+str(bonuses[mturkID]))
            writer.writerow([HitID]+[mturk]+["approved"]+[bonuses[mturkID]])


def createPaymentFile(pay):
    des=open('../payment.csv', 'w')
    writer = csv.writer(des)
    writer.writerow(["HIT ID"]+["mturkID"]+["status"]+["Bonus"])
    des.close()
    for file in glob.glob("*.txt"):
        print "file:" + file
        with open(file,'r') as myfile:
            lines = myfile.readlines()
            for line in lines:
                approveAndPay(line.replace("\n", ""), pay)

pay = int(sys.argv[1])               
createCommentsFile(pay)

