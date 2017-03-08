import pdb
import types
import unittest


class BinaryTree():

    def __init__(self, value):                                                             
        print 'Inserting new tree element: %s' % value                                                 
                                                                                           
        self.value = value                                                                  
        self.left = None                                                                   
        self.right = None                                                                  

    def add_item(self, value):                                                 
        """Add a new integer value into the binary tree
           Inputs: self, value
           Returns: True|False based on if the element was added or not"""

        if type(value) is not types.IntType:
            print 'Error: Invalid value: ==>%s<==. Not added.' % str(value)
            return False

        if self.value:
            if value > self.value:
                if self.right == None:
                    # add it here
                    self.right = BinaryTree(value)
                    return True
                else:
                    # move left one layer down                                                 
                    self.right.add_item(value)

            elif value < self.value:
                if self.left == None:
                    # add it here
                    self.left = BinaryTree(value)
                    return True
                else:
                    # move left one layer down                                                 
                    self.left.add_item(value)

            else:
                 print 'Error: Duplicate value: %s not added' % value
                 return False
        else:
            self.value = value

    def get_items(self):
        """Get all values in the tree. We need this to verify any number of tests to be
           run"""

        tree = []
        current = self
        items = []

        while tree != [] or current: 
            if current:
                tree.append(current)
                # go left
                current = current.left
            else:
                current = tree.pop()
                # print '=>>>> Adding current node value: %s' % current.value
                items.append(current.value)
                current = current.right

        return items

    def print_items(self):                                                        
        """in-order traversal of binary tree                                                
           NOTE: this routine only prints values"""

        if self.left != None:
            self.left.print_items()

        print self.value

        if self.right != None:
            self.right.print_items()


class TestTree(unittest.TestCase):
    """UnitTest class to test the binary tree"""

    def setUp(self):                                                                       
        """Create our trees under test...
           This op could be broken into it's own test case function if needed."""
        for tree in trees.keys():
            for node in trees[tree]['nodes']:
                if trees[tree]['object'] == None:
                    trees[tree]['object'] = BinaryTree(trees[tree]['root_value'])
                                                                                             
    def tearDown(self):
        pass
                                                                                             
    def test_001_verify_insert_values(self):                                                                    
        """Verify valid values can be added to each tree"""

        for tree in trees.keys():
            print 'Testing tree:', tree
            node_count = 1

            for node in trees[tree]['nodes']:
                # print 'Here is the latest element to be inserted:', node

                trees[tree]['object'].add_item(node)
                node_count += 1

                # Our node count and tree values length should always be the same here
                self.assertEquals(len(trees[tree]['object'].get_items()),
                                  node_count)

    def test_002_verify_in_order_search(self):                                                                    
        """Verify an in-order traversal reports the proper sequence of node values"""

        for tree in trees.keys():
            in_order_values = trees[tree]['object'].get_items()

            print 'In order values are: %s' % str(in_order_values)

            expected_values = sorted([trees[tree]['root_value']] + trees[tree]['nodes'])

            self.assertEquals(expected_values, in_order_values,
                'In-order values are out of proper sequence: %s Expecting: %s' % \
                    (str(in_order_values), str(expected_values)))

    def test_003_verify_bad_insertions(self):
        """Verify bad value types cannot be added to a tree"""

        for tree in trees.keys():
            for node in trees[tree]['bad_nodes']:
                self.assertNotEquals(trees[tree]['object'].add_item(node), node)

    def test_004_verify_duplicate_insertions(self):
        """Verify duplicate value types cannot be added to a tree"""

        for tree in trees.keys():
            for node in trees[tree]['dups']:
                self.assertNotEquals(trees[tree]['object'].add_item(node), node)

    def test_005_verify_in_order_search(self):                                                                    
        """Verify a second in-order traversal reports the proper sequence of node values
           This re-confirms no unwanted junk was added"""

        for tree in trees.keys():
            in_order_values = trees[tree]['object'].get_items()

            print 'In order values are: %s' % str(in_order_values)

            expected_values = sorted([trees[tree]['root_value']] + trees[tree]['nodes'])

            self.assertEquals(expected_values, in_order_values,
                'In-order values are out of proper sequence: %s Expecting: %s' % \
                    (str(in_order_values), str(expected_values)))


# main():
                                                                                           
if __name__ == '__main__':                                                                 
    """
        Be sure to on the command line as:

        python binary_tree_for_oblong.py

        Test cases covered:

        1) insertion of N elements to the tree
        2) in-order traversal verification
        3) invalid values into the tree
        4) duplicate values into the tree (not allowed)
        5) re-verify in-order traversal verification to ensure tree is still the same

        Some other test cases to consider based on logic currently in place:

        1) insertion of many elements into the tree, where n > 100, n > 1000, etc
        2) more negative values (currently only use one)
        3) other invalid data types to try to be inserted (should not get inserted)
        4) break the setUp() logic into it's own test routine

        Also, can move the 'trees' data structure into the TestTree() class for py.test/nosetests harness
    """

    """
       Our trees to test against

       NOTE: These are currently setup this way to be looped though per test case
    """
    trees = {
        1: {
            'object': None,
            'root_value': 10,
            'nodes': [5, 15, -3, 20, -100, 4, 100, 1],
            'dups':  [10, 5, -100, 15, -3, 20, 100, 4, 1],
            'bad_nodes': ['hello', 21.5, (1, 2), {'a':'b'}, [1, 2, 3]]
        },
        2: {
            'object': None,
            'root_value': 5,
            'nodes': [15, -200, 20, -3, 4, 200, 1, 10],
            'dups':  [5, 15, -200, 20, -3, 4, 200, 1, 10],
            'bad_nodes': ['hello', 21.5, (1, 2), {'a':'b'}, [1, 2, 3]]
        },
    }

    unittest.main()
    quit()


    """
    tree_1 = BinaryTree(10)                                                                
    tree_1.add_item(5)                                                          


    tree_1.add_item(5)                                                          
    tree_1.add_item(10)                                                         
    tree_1.add_item(15)                                                          
    tree_1.add_item(20)                                                          
    tree_1.add_item(4)                                                          
    tree_1.print_items()

    print "========================"
    print 'here are the values %s' % str(tree_1.get_items())
    print "========================"

    count = 0

    quit()

    for i in tree_1.get_items():
        print i
        count+=1
    print 'node count:', count

    quit()

    for node in bad_nodes:
        tree_1.assertEquals(tree_1.add_item(node), False)

    quit()
    """
