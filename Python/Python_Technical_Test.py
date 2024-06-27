import unittest

def remove_duplicates(lst):
    seen = set()        # Initialize set for storing unique item
    result = []         # Initialize result list
    
    # Removes duplicate elements from a list while maintaining the order.
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

class TestRemoveDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        # Test when there are no duplicates
        input_list = [1, 2, 3, 4]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(remove_duplicates(input_list), expected_result)

    def test_with_duplicates(self):
        # Test with duplicates
        input_list = [1, 2, 2, 3, 4, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(input_list), expected_result)

    def test_character_with_no_duplicates(self):
        # Test with no duplicates
        input_list = ['a','b','c','d','e','f']
        expected_result = ['a','b','c','d','e','f']
        self.assertEqual(remove_duplicates(input_list), expected_result)
    
    def test_character_with_duplicates(self):
        # Test with duplicates
        input_list = ['a','b','ac','ab','b','c','a','ca','c']
        expected_result = ['a','b','ac','ab','c','ca']
        self.assertEqual(remove_duplicates(input_list), expected_result)
    
    def test_item_list_with_no_duplicates(self):
        # Test with no duplicates
        input_list = ['Car','Bus','Bike','Train','Motorcycle']
        expected_result = ['Car','Bus','Bike','Train','Motorcycle']
        self.assertEqual(remove_duplicates(input_list), expected_result)
    
    def test_item_list_with_duplicates(self):
        # Test with duplicates
        input_list = ['Orange','Egg','Banana','Milk','Basil','Milk','Orange','Egg','Banana','Milk']
        expected_result = ['Orange','Egg','Banana','Milk','Basil']
        self.assertEqual(remove_duplicates(input_list), expected_result)

if __name__ == "__main__":
    """
    # Here you can try to customize input and see your output for the program
    custom_input_list = ['a','b','ac','ab','b','c','a','ca','c']
    actual_result = remove_duplicates(custom_input_list)
    print("Your custom input = ", actual_result)
    print("")
    """
    unittest.main(verbosity=2)