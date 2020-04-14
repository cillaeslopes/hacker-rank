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

class LevelOrderTree:
    ROOT_LEVEL = 0
       
    def __init__(self, root):
        self.root = root
        self.levels = {}

    def build_levels(self):
        self.build_levels_from(self.root, self.ROOT_LEVEL)
    
    def build_levels_from(self, node, level):
        if level not in self.levels:
            self.levels[level] = []

        if node is not None:
            self.levels[level].append(str(node.info))
            self.build_levels_from(node.left, level+1)
            self.build_levels_from(node.right, level+1)
    
    def print_levels(self):
        tree_in_level_order = []
        for level in self.levels:
            nodes_in_level = self.levels[level]
            if len(nodes_in_level):
                tree_in_level_order += nodes_in_level
        
        print ' '.join(tree_in_level_order)

    def get_levels(self):
        tree_in_level_order = []
        for level in self.levels:
            nodes_in_level = self.levels[level]
            if len(nodes_in_level):
                tree_in_level_order += nodes_in_level
        
        return ' '.join(tree_in_level_order)
    
def levelOrder(root):
    ordered_tree = LevelOrderTree(root)
    ordered_tree.build_levels()
    return ordered_tree.get_levels()

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

        return levelOrder(tree.root)

    def test_case_0(self):
        number_of_nodes = 6
        nodes = '1 2 5 3 6 4'
        
        result = self.base_test(number_of_nodes, nodes)
        
        return result == '1 2 5 3 6 4'

    def test_case_1(self):
        return True

    def test_case_2(self):
        return True

if __name__ == '__main__':
    tests = Tests()
    tests.validate_cases()
