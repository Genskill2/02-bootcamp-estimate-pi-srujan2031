import math
import unittest


def wallis(iterations):
    
    num = 2.0
    den = 1.0
    pi = 1.0
    for i in range(1, iterations + 1):
        pi=pi* (num / den)
        if (i%2) == 1:
            den+= 2.0
           
        else:
            num+= 2.0 
        
    pi*=2.0
    return pi
def monte_carlo(iterations):
    import math as m
    import random as r
    
    inside=0
    
    
    for i in range(0,iterations):
        x2=r.random()**2
        y2=r.random()**2
        
        if m.sqrt(x2+y2) < 1.0:
            inside+=1
    
    pi=(float(inside)  / iterations) * 4
    
    return pi



















class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
