# CreateHit
Running Experiments on Mechanical Turk


CreateHit.py gets the total number of assignements and creates hits in batches of 9 assignments. The information about the HIT IDs are kept in the HITIDs file. HIT layout should be added in sample.py and passed to CreateHIt.py.
getComments.py goes through all the HITs created in the previous step and gets the Worker's comments.
approveAndPay.py approves assignments and pays bonuses. 
