import sys
from contextlib import contextmanager

class redirect_stdout(object):
    def __init__(self, filename):
        self.outputFilename = filename
        
    def __enter__(self):
        self.oldstdout = sys.stdout
        self.openOutputFile = open(self.outputFilename, 'a')
        sys.stdout = self.openOutputFile
        
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.openOutputFile.close()
        sys.stdout = self.oldstdout
        
@contextmanager
def redirect_stdout2(filename):
    outputFilename = filename
    oldstdout = sys.stdout
    openOutputFile = open(outputFilename, 'a')
    sys.stdout = openOutputFile
    yield
    openOutputFile.close()
    sys.stdout = oldstdout

if __name__ == '__main__':
    print 'Start'
    with redirect_stdout('Ex1_4_3.output'):
        print 'In with'
    print 'Out of with'
    
    print 'Start2'
    with redirect_stdout2('Ex1_4_3.output2'):
        print 'In with2'
    print 'Out of with2'