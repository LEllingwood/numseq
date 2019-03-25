def primes(n):  
    prime_list = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            prime_list.append(possiblePrime)
    
    return(prime_list)


def is_prime(m):
    if m >= 2:
        for y in range(2, m):
            if not (m % y):
                return False
    else:
	    return False
    return True
