import sys

try:
  print 5/0
except:
  print "Exception : ", sys.exc_info()[0]
