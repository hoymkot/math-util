# create a map with all non-prime numbers X-marked. One can easily check whether a number is prime by simply calling primes.get(i,True); 

import math;
primes = {};

def elmin(num):
    i = 2;
    m = int(math.sqrt(num) + 1);
    while (i < m):
        if (primes.get(i, True) == True):
            j = i+1;
            while (j < num+1):
                if (primes.get(j, True) == True and j % i == 0):
                    primes[j] = False;
                j=j+1;            
        i = i +1;

primes.get(2,True)
