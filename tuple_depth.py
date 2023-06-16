# Iver Macaulay
# 19 Nov 2019

# Tuples

# Define the function
def deep_length( a_tuple ):
    # Initialize the tuple depth counter to 1
    deep_length = 1
    # Iterate through the tuple
    for element in a_tuple:
        # If the element is a tuple..
        if( isinstance(element, tuple) ):
            # Then the tuple depth is 2
            deep_length = 2
            # Iterate through embedded tuple
            for element2 in element:
                # If the element is another tuple then add 1 to the tuple depth counter
                if( isinstance(element2, tuple) ):
                    deep_lenth += 1
                # When there are no more elements in the tuple, exit iteration    
                else:
                    break

    return deep_length

# TEST
tuple1 = (1, (2, 3), 4, (5, (6, 7) ), 8 )
print( deep_length( tuple1 ) )
