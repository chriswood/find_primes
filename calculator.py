


class Calc:
    """
        This class will handle doing the actual prime testing.
        All methods used will be stored here.
    """
    def __init__(self, slength):
        self.slength = slength
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
        return True
        
    def brute_force(self):
        """ 
        The basic generator of primes. 
        
        """
        last_tested_num = 1
        
        def gen_primes(number):
            while True:
                if self.is_prime(number):
                    yield number
                number += 1
        
        for n_prime in gen_primes(3): #start with 3 since we already have 2
            if len(self.result) < self.slength:
                self.result.append(n_prime)
            else:
                return
    
    def multiple_of_three(self, n):
        """
        Since 3 is a very common mulitple it may be worth taking advantage of
        a trick that lets us avoid a large modulation, instead doing addition
        and a final small modulation.
        TODO: Test and see if this is quicker on average or for a given range.
        """
        return False