print "How big would you like your multiplication table to be?"
n = int(raw_input())
x = 0
for i in xrange (1,n+1):
    ##print i,
    for j in xrange(1,n+1):
        
        print  i * j, 
        j+=1
        x+=1
        if x == n:
            print "\n"
            
            x = 0


