"""Binomial coefficient"""


def BinomialCoefficientUtil(n,k):
    if k>n:
        return 0
    if k==0 or k==n:
        return 1
    return BinomialCoefficientUtil(n-1,k-1)+BinomialCoefficientUtil(n-1,k)



def binomialCoeff(n,k):
    dp=[[-1 for y in range(k+1)]for x in range(n+1)]
    print(dp)
    return BinomialCoefficientUtil(n,k,dp)
    n=5
    k=2
    print("Value of C(" + str(n) +
               ", " + str(k) + ") is",
               binomialCoeff(n, k))



