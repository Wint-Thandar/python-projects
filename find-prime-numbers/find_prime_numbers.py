# Create a function with an argument to get number of upper bound.
def primes_finder(num = 10):
    """
    Finds and returns all prime numbers within 2 and the given num args.
    If no argument is given, 10 is used as a default number.
    
    Args: 
      num (int): Upper bound number value. Default is 10. 
      
    Returns: 
      A list of all prime numbers within 2 and the given argument.
    """

    # Set the number range to be checked. 2 is set as a start number as it is 
    # the smallest true Prime number. num+1 is set as a stop number as to 
    # include the given num in the range.
    number_range = set(range(2, num + 1))

    # Define empty list to append discovered primes to.
    primes_list = []

    # Loop while there is an element in number_range.
    while number_range: 
        # pop method is used to remove and get the first element of the set.
        prime = number_range.pop()
        
        # The returned element is appended to the list of primes numbers.
        primes_list.append(prime)
        
        # Assign all the numbers until num+1 that are the multiples of the 
        # current prime element to a set. They are non-prime numbers.
        multiples = set(range(prime * 2, num + 1, prime))
        
        # Use difference_update method to remove all non-primes from the 
        # number_range set. 
        number_range.difference_update(multiples)

    # Set number of primes that were found.
    prime_count = len(primes_list)

    # Set largest prime.
    largest_prime = max(primes_list)

    # Print summary message.
    print(f"There are {prime_count} prime numbers between 2 and {num}, the largest of which is {largest_prime}")
    
    # Return the list of prime numbers found.
    return primes_list

primes_finder(100)
primes_finder(1000)
