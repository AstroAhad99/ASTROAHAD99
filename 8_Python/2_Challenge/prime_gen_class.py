class primegenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2
 
    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n    # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator
            
my_gen = primegenerator(5)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

