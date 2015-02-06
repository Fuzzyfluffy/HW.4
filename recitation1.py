def loopOverDict(dic):
    for element in dic:
        print 'before', dic(element)
        dic(element) += 1
        print 'after', dic(element)
