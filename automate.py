def apply_p(A: float, p: float):
    new_a = A + A * p / 100

    return new_a


def apply_q(L: float, A: float, q: float):
    new_a = A - A * q / 100
    new_l = L + L * q / 100

    return new_a, new_l


def apply_r(L: float, r: float):
    new_l = L - L * r / 100

    return new_l
