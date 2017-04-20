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
os.chdir("./HITIDs")

def getComments(HitID):
    global connection
    print "Getting comments for " + HitID
    assignments = connection.get_assignments(HitID, sort_by='SubmitTime', sort_direction='Ascending')
    with open('../comments.csv', 'a') as csvoutput:
        writer = csv.writer(csvoutput)
        for assignment in assignments:
            comment= str(assignment.answers[0][0].fields)
            comment=comment.replace("\\n", " - ")
            comment=comment.replace("\\r", " - ")
            comment=comment.replace("']", "")
            comment=comment.replace("[u'", "")
            comment=comment.replace("[u\"", "")
            comment=comment.replace("\"]", "")
            comment=comment.replace("['", "")
            mturk= assignment.WorkerId
            writer.writerow([HitID]+[mturk]+[comment])


def createCommentsFile():
    des=open('../comments.csv', 'w')
    writer = csv.writer(des)
    writer.writerow(["HIT ID"]+["mturkID"]+["Comment"])
    des.close()
    for file in glob.glob("*.txt"):
        print "file:" + file
        with open(file,'r') as myfile:
            lines = myfile.readlines()
            for line in lines:
                getComments(line.replace("\n", ""))
                


                
createCommentsFile()

