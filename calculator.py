


class Calc:
    """
        This class will handle doing the actual prime testing.
        All methods used will be stored here.
    """
    def __init__(self, slength):
        self.search_length = slength
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
        1) get an empty list
        2) for every odd #, test for prime
        3) If it is, add it to list
        """
        return [2,3,5,7,11,13,17,19,23,29,31,37]
