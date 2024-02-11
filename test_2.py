l_test1 = [1, 3, 2, 0, 2, 1]
l_test2 = [2, 4, 1, 0, 1, 0]

def cosine_distance(l1:list, l2:list):
    """ Calculate cosine distance between two vectors """

    # Verification of input data: lists have equal length and all elements are integers
    while True:
        try:
            if isinstance(l1, list) and isinstance(l2, list):
                
                if len(l1) != len(l2):
                    raise ValueError("Different length of vectors")
                
                for x, y in zip(l1, l2):
                    if (not isinstance(x, int)) | (not isinstance(y, int)):
                        raise ValueError("The elements of the list must be integers")
                    
                # Calculation of cosine distance
                denominator = (sum([i ** 2 for i in l1]) ** 0.5) * (sum([i ** 2 for i in l2]) ** 0.5)
                numerator = sum([i * j for i, j in zip(l1, l2)])
                return 1 - numerator / denominator                    

            else:
                raise TypeError("Invalid input type")
            
        except TypeError as e:
            print(e)

print(cosine_distance(l_test1, l_test2))