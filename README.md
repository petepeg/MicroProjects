# Micro Projects
Here is where I'm putting project that interest me but are too small to merrit their own repo.

## Farey Algorithm
This is an algorithm for computing a rational approximation of a decimal. It works by starting with 0 and 1, and taking the halfway point  (1/2) and checking if the decimal expansion of 1/2 is equal to, greater than or less than the input number. If they are equal, jobs done. Otherwise if 1/2 is greater than our number we know our number's rational approximation lives in the lower half, between 0-1/2 and if 1/2 is less than our number we know our number lives between 1/2-1. We than repeat this process either till we find the fraction or get bored and decide we are close enough. This is essentially a binary search of all possible fractions between 0 and 1 which works surprisingly well.

Just for fun I implemented this as a recursive function and a looping function and raced them. Just to be fair I set the number of loops to the recursion limit. What I found was the recursion was a bit slower but really not by much. I also played around with walrus operators and lambdas to see if they were faster than more basic syntax and it was by just a small amount, but not really worth noting.

## Sieve Of Erathosthenes
This is a method for generating primes. You start with a list of bools, initially all true. Than setting index 0, and 1 to false for not being primes, this is done manually cause it just makes everything easier. From here we iterate over this list starting at 2, each index represents the number and its bool value if it is prime. We take the current index and iterate through all multiples of it setting them to false since we know that they cant be prime if it is a multiple of a smaller number.

There are a few optimizations I applied which are very common and yanked right off wikipedia. First for our outer loop we only iterate up to the square root of the end of our primes list, since we know that will will have set all the non primes by that point. Next for our inner loop we start iterating over multiples at the index times itself for a similar reason. Doing both of these drastically reduces the number of iterations required.
