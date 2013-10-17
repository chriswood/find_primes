
import math

class Calc:
    """
        This class will handle doing the actual prime testing.
        All methods used will be stored here.
    """
    def __init__(self, slength):
        self.slength = int(slength)
        self.errors = []
        self.result = [2]
        self.valid_stypes = ['brute_force']
        
    def run_method(self, stype):
        """
        Take the search type and find and run the desired method.
        We may need a translation dict or something for this.
        """
        if stype in self.valid_stypes:
            f = getattr(self, stype) #assumes naming conventions...
            f()            
        else:
            # Result stays empty
            self.errors.append('Invalid Search Type')
            
    def is_prime(self, N):
        '''
        Check a number N and see if it is divisible by anything (less that
        it's square root) evenly.
        '''
        # check predefined values
        if N in (1, 4):
            return False
        if N in (2, 3):
            return True
        
        #get last value to test for even division into N
        last_value = math.ceil(math.sqrt(N))

        for n in range(2, int(last_value) + 1):
            if (N%n == 0):
                return False
        return True
        
    def brute_force(self):
        """ 
        The straight forward (somewhat) method of creating primes
        through a generator. 
        """
        def gen_primes(number):
            while True:
                if self.is_prime(number):
                    yield number
                number += 1
        #start with 3 since we already know 2 is not valid
        for n_prime in gen_primes(3): 
            if len(self.result) < self.slength:
                self.result.append(n_prime)
            else:
                return
