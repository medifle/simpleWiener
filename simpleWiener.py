import math


# # recursive version
# def cf_recur(n, d):
#     """Return the terms of the continued fraction when n is the numerator
#     and d the divisor as a list"""
#     if d == 0:
#         return []         # Ok it is finished
#     q = n//d                     # compute the integer quotient
#     r = n - q*d                  # the rest
#     return [q] + cf_recur(d, r)        # and recurse...


# iterative version
def cf(n, d):
    res = []
    q, r = divmod(n, d)
    while r != 0:
        res = res + [q]
        q, r = divmod(d, r)
        d = (d - r) // q
    return res + [q]


def cf_to_convergent(cfe):
    """
    cfe: continued fraction expansion, a list
    ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf (6)
    ref: https://github.com/orisano/owiener/blob/master/owiener.py
    """
    # owiener's version is slightly different from the pdf for q0, q1 to avoid extra 'if else'
    n1, n0 = 1, 0
    d1, d0 = 0, 1

    n, d = None, None
    for q in cfe:
        n = q * n1 + n0
        d = q * d1 + d0
        n0, d0 = n1, d1
        n1, d1 = n, d
    return n, d


def is_square(n):
    return math.isqrt(n) ** 2 == n


def simple_wiener_attack(e, n):
    cfe = cf(e, n)
    for i in range(0, len(cfe)):
        sub_cfe = cfe[:i + 1]
        k, d = cf_to_convergent(sub_cfe)
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            sum_pq = n - phi + 1
            # we know p+q and pq, solve the equation using high school knowledge:
            # given ax^2 - bx + c = 0, x = (-b ± sqrt(b^2 - 4ac))/2a
            # Here we only need to know the solution x is an integer
            # so we use is_square(...) to test if p and q are integer solution
            if sum_pq % 2 == 0 and is_square((sum_pq // 2) ** 2 - n):
                print("k={}\nd={}".format(k, d))
                print(sub_cfe)

# test
# print(cf(37, 101))
# print(cf_to_convergent(cf(37, 101)))
# print(cf_to_convergent([0, 2, 1, 2, 1, 2, 3]))

e = 9292162750094637473537
n = 13029506445953503759481
simple_wiener_attack(e, n)
