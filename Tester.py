from tests import *

class Tester:   
    def __init__(self):
        self._tests = []  #list of questions at startup
        self._load_tests() 
        

    def _load_tests(self):
        for test in tests:
            self._tests.append(_test(test))

    @property
    def Tests(self):
        return self._tests
            
        
        
        
  
    #things it can do
    #form and run a question and answer
    pass



class _test:
    #things it knows
    def __init__(self, test):
        self.test_number = test['test_number']
        self.question = test['question']
        self.parts = self._get_parts(test)
        
    def _get_parts(self, test):
        parts = []
        for value in test['parts']:
            parts.append((value['question'], value['ans']))
        return parts
        
        
    #the answers
    #Things it can do
    #serialise from dictionary at startup
    pass

