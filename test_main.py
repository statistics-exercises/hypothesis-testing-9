import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for d in xvals : 
            pd = scipy.stats.norm.cdf(d)
            u = scipy.stats.norm.ppf(pd + 0.95)
            self.assertTrue(  np.fabs( u - upperBound(d) )<1e-4, "your upperBound function does not return the correct values" )
