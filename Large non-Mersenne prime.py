from functools import lru_cache

@lru_cache(maxsize=128)
def last_ten(): return str(1+28433*(2**7830457))[-10:]
if __name__ == '__main__':
    print(last_ten())

# The answer: 8739992577
# Note: I used the lru_cache because I was afraid that my machine gets lagged or damaged cuz of so much calculations!
