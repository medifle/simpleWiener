import math
from typing import Tuple, List


##
# recursive version, for the curious :)
##
# def cf_recur(n: int, d: int) -> List[int]:
#     """Return the terms of the continued fraction when n is the numerator
#     and d the divisor as a list
#     ref: https://stackoverflow.com/questions/48094595/convert-fraction-to-continued-fraction"""
#     if d == 0:
#         return []  # Ok it is finished
#     q = n // d  # compute the integer quotient
#     r = n - q * d  # the rest
#     return [q] + cf_recur(d, r)  # and recurse...


# iterative version
def cf(n: int, d: int) -> List[int]:
    res = []
    q, r = divmod(n, d)
    while r != 0:
        res = res + [q]
        q, r = divmod(d, r)
        d = (d - r) // q
    return res + [q]


def cf_to_convergent(cfe: list) -> Tuple[int, int]:
    """
    cfe: continued fraction expansion
    ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf (6)
    ref: https://github.com/orisano/owiener/blob/master/owiener.py
    """
    # owiener's version is slightly different from the pdf for q0, q1 to avoid extra if else
    n1, n0 = 1, 0
    d1, d0 = 0, 1

    n, d = None, None
    for q in cfe:
        n = q * n1 + n0
        d = q * d1 + d0
        n0, d0 = n1, d1
        n1, d1 = n, d
    return n, d


def is_square(n: int) -> bool:
    # isqrt is a new feature in python3.8
    return math.isqrt(n) ** 2 == n


def check_phi(_k: int, _d: int, e: int, n: int, round: int = 10) -> bool:
    for i in range(1, round + 1):
        k = _k * i
        d = _d * i
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            sum_pq = n - phi + 1
            # We know p+q and pq, solve the quadratic equation using high school knowledge:
            # Given ax^2 - bx + c = 0, x = (-b ± sqrt(b^2 - 4ac))/2a
            # We only need to know if the solution x is an integer
            # We use is_square(...) to test if p and q are integer solution
            # BTW, p+q should be an even number if we assume none of p or q is 2
            if sum_pq % 2 == 0 and is_square((sum_pq // 2) ** 2 - n):
                print("\nphi={}\nk={}\nd={}\n".format(phi, k, d))
                return True
    return False


def simple_wiener_attack(e: int, n: int) -> None:
    cfe = cf(e, n)
    for i in range(0, len(cfe)):
        sub_cfe = cfe[:i + 1]
        k, d = cf_to_convergent(sub_cfe)
        if check_phi(k, d, e, n, 50):
            return
    print('Not Found')


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        e = int(sys.argv[1])
        n = int(sys.argv[2])
        simple_wiener_attack(e, n)
    else:
        print("Usage: python3 -m simpleWiener.core e n")
