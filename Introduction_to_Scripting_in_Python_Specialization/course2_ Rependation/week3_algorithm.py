"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for index in range(2, bound):
    	for num in answer:
    		if num%index == 0 and num != index:
    			answer.remove(num)
    return answer

print(compute_primes(10))


print(len(compute_primes(200)))
print(len(compute_primes(2000)))