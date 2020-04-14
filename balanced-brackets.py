#!/bin/python

import math
import os
import random
import re
import sys

def isBalanced(string):
    TRUE_RESPONSE = 'YES'
    FALSE_RESPONSE = 'NO'

    if not is_even_string(string):
        return FALSE_RESPONSE
    
    string_without_matched_pairs = remove_matched_pairs(string)

    return TRUE_RESPONSE if not len(string_without_matched_pairs) else FALSE_RESPONSE
    
def is_even_string(string):
    return len(string) % 2 == 0

def remove_matched_pairs(string):
    matched_pairs = ['{}', '[]', '()']

    if len(string):
        for pair in matched_pairs:
            while pair in string:
                index = string.find(pair)
                new_string = string[0:index] + string[index+2:len(string)]
                return remove_matched_pairs(new_string)
    
    return string

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

    def base_test(self, string_to_validate, expected):
        result = isBalanced(string_to_validate)
        return result == expected

    def test_case_0(self):
        passed = True

        # Scenario 1
        string_to_validate = '{[()]}'
        expected_answer = 'YES'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        # Scenario 2
        string_to_validate = '{[(])}'
        expected_answer = 'NO'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        # Scenario 3
        string_to_validate = '{{[[(())]]}}'
        expected_answer = 'YES'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        return passed

    def test_case_1(self):
        passed = True

        # Scenario 1
        string_to_validate = '{{([])}}'
        expected_answer = 'YES'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        # Scenario 2
        string_to_validate = '{{)[](}}'
        expected_answer = 'NO'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        return passed

    def test_case_2(self):
        passed = True

        # Scenario 1
        string_to_validate = '{(([])[])[]}'
        expected_answer = 'YES'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        # Scenario 2
        string_to_validate = '{(([])[])[]]}'
        expected_answer = 'NO'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        # Scenario 3
        string_to_validate = '{(([])[])[]}[]'
        expected_answer = 'YES'
        passed = passed and self.base_test(string_to_validate, expected_answer)

        return passed

if __name__ == '__main__':
    tests = Tests()
    tests.validate_cases()