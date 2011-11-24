from twisted.internet import reactor, defer
import time

def printTime():
    print (time.ctime())
    reactor.callLater(1, printTime)

if __name__ == '__main__':
    reactor.callLater(1, printTime)
    reactor.run()
    