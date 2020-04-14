class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    return calc_depth_from(root, 0)

def calc_depth_from(node, level):
    if node == None:
        return 0

    left_depth = calc_depth_from(node.left, level+1)
    right_depth = calc_depth_from(node.right, level+1)

    return max(left_depth, right_depth) or level

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

    def base_test(self, number_of_nodes, nodes):
        tree = BinarySearchTree()

        arr = list(map(int, nodes.split()))

        for i in xrange(number_of_nodes):
            tree.create(arr[i])

        return height(tree.root)

    def test_case_0(self):
        number_of_nodes = 7
        nodes = '3 5 2 1 4 6 7'
        height = self.base_test(number_of_nodes, nodes)
        return height == 3

    def test_case_1(self):
        number_of_nodes = 1
        nodes = '15'
        height = self.base_test(number_of_nodes, nodes)
        return height == 0
    
    def test_case_2(self):
        number_of_nodes = 5
        nodes = '3 1 7 5 4'
        height = self.base_test(number_of_nodes, nodes)
        return height == 3

    def test_case_3(self):
        number_of_nodes = 15
        nodes = '1 3 2 5 4 6 7 9 8 11 13 12 10 15 14'
        height = self.base_test(number_of_nodes, nodes)
        return height == 9

if __name__ == '__main__':
    tests = Tests()
    tests.validate_cases()