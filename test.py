import numpy as np
import matplotlib.pyplot as plt


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


def initialization():
    epsilon = 1e-4

    A = 100
    L = 30

    p = 6

    return epsilon, A, L, p


def main():
    epsilon, A, L, p = initialization()

    # q = (A + p / 100 * A - A) * 100 / (A + p / 100 * A)
    # r = (A + q / 100 * A - A) * 100 / (A + q / 100 * A)
    q = round(5.660377358490566, 3)
    r = round(5.357142857142855, 3)

    array_t = [0]
    array_A = [A]
    array_L = [L]

    current_t = 0
    end_t = 100

    while current_t < end_t:
        print(A, L)

        A = apply_p(A, p)
        print(A, L)
        A, L = apply_q(L, A, q)
        print(A, L)
        L = apply_r(L, r)
        print(A, L)

        current_t += 1

        array_t.append(current_t)
        array_A.append(A)
        array_L.append(L)
        print()

    array_A = np.asarray(array_A)
    array_L = np.asarray(array_L)

    plt.plot(array_t, array_A)
    plt.plot(array_t, array_L)
    plt.show()

    # ratio = array_A / array_L
    #
    # plt.plot(array_t, ratio)
    # plt.show()
    #
    # for i in range(1, len(ratio)):
    #     if np.abs(ratio[i] - ratio[i - 1]) > epsilon:
    #         return None, None, None

    return p, q, r


if __name__ == "__main__":
    p, q, r = main()

    print(f"p = {p}, q = {q}, r = {r}")
