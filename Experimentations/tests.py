class Tests:
    failed_cases = []

    def __init__(self):
        self.test_cases = {
            0: self.test_case_0(),
            1: self.test_case_1(),
            2: self.test_case_2()
        }
    
    def validate_cases(self):
        for test_case in self.test_cases:
            passed = self.test_cases[test_case]
            
            if not passed:
                self.failed_cases.append(str(test_case))
        
        self.print_results()

    def print_results(self):
        if len(self.failed_cases):
            print 'Some tests have failed: '
            print ', '.join(self.failed_cases)
        else:
            print 'All test cases have passed'

    def base_test(self):
        return True

    def test_case_0(self):
        self.base_test()
        return True

    def test_case_1(self):
        self.base_test()
        return True

    def test_case_2(self):
        self.base_test()
        return True

if __name__ == '__main__':
    tests = Tests()
    tests.validate_cases()