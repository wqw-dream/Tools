import sys 

if len(sys.argv) == 1:
    print "\n*******************************"
    print "please run this script like this:"
    print "python appinfo.py 12345"
    print "\n*******************************\n\n"
    sys.exit()

appinfoid = int(sys.argv[1])
mc_id = (appinfoid >> 8) & 0xFFFFFFFF
print "appinfo:%u" % appinfoid
print "mc_id:%u" % mc_id
