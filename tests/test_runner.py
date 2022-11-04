# test_runner23.py

if __name__ == '__main__':
    import sys
    import unittest
    from test_buys import BuyStockTest
    from test_sells import SellStockTest

    suite = unittest.TestSuite()
    # suite = unittest.TestSuite( [suite1, suite2] ) 
    # no specific test runner to run, runs all   
    if len(sys.argv) == 1:
        suite1 = unittest.TestLoader().loadTestsFromTestCase(BuyStockTest)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(SellStockTest)
        suite = unittest.TestSuite([suite1, suite2])
    else:
        for test_case in sys.argv[1:]:
            # Unsure of the correct implementation to add a specific test case
            # when there are multiple test suites possible, so hard coded a try-catch statements
            try: 
                suite.addTest(BuyStockTest(test_case))
            except:
                pass
            try: 
                suite.addTest(SellStockTest(test_case))
            except:
                pass 
    unittest.TextTestRunner(verbosity = 2).run(suite)
