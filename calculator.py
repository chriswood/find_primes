


class Calc:
    """
        This class will handle doing the actual prime testing.
        All methods used will be stored here.
    """
    def __init__(self, slength):
        self.slength = slength
        self.errors = []
        self.result = []
        self.valid_stypes = ['brute_force']
        
    def run_method(self, stype):
        """
        Take the search type and find and run the desired method.
        We may need a translation dict or something for this.
        """
        if stype in self.valid_stypes:
            f = getattr(self, stype) #assumes naming conventions...
            self.result = f()            
        else:
            # Result stays empty
            self.errors.append('Invalid Search Type')
        
    def brute_force(self):
        """ 
        The basic generator of primes. 
        
        """
        plist = [2]
        last_tested_num = 1
        
        def is_prime_brute(num):
            if self.multiple_of_three(num):
                return False
            # We have tested 2 and 3.
            # num/2 is not an integer, num/3 is not an integer
            # So, we need to test 4 through num/4
            return(True)
        
        # We need slength primes.
        while len(plist) < self.slength:
            # weed out even mumbers...
            num = last_tested_num + 2
            if is_prime_brute(num):
                plist.append(num)
            last_tested_num = num
        return plist
    
    def multiple_of_three(self, n):
        """
        Since 3 is a very common mulitple it may be worth taking advantage of
        a trick that lets us avoid a large modulation, instead doing addition
        and a final small modulation.
        TODO: Test and see if this is quicker on average or for a given range.
        """
        return False