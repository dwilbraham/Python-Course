from twisted.internet import reactor, defer

def printData(data):
    print (data)

if __name__ == '__main__':
    reactor.callLater(5, printData, "Data1")
    reactor.run()
    #THIS WILL NEVER BE REACHED!!!
    print "Reactor running"
    reactor.callLater(5, printData, "Data2")
    reactor.callLater(5, printData, "Data3")
    