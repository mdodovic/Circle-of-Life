import numpy as np
import matplotlib.pyplot as plt

from automate import *

SAME_VALUE = 0

def initialization():
    epsilon = 1e-3
    delta = epsilon * 10

    start_time = 0
    delta_time = 1
    end_time = 100

    A = 100.
    L = 30.

    p = 6.

    return epsilon, delta, A, L, start_time, delta_time, end_time, p


def run_single_circle_of_life(start_A, start_L, start_t, end_t, delta_t, p, q, r):
    current_time = start_t
    end_time = end_t

    array_t = [0]
    array_A = [start_A]
    array_L = [start_L]

    A = start_A
    L = start_L

    while current_time < end_time:
        #        print(A, L)

        A = apply_p(A, p)
        #        print(A, L)
        A, L = apply_q(L, A, q)
        #        print(A, L)
        L = apply_r(L, r)
        #        print(A, L)

        current_time += delta_t

        array_t.append(current_time)
        array_A.append(A)
        array_L.append(L)
    #        print()

    array_A = np.asarray(array_A)
    array_L = np.asarray(array_L)

    # plt.plot(array_t, array_A)
    # plt.plot(array_t, array_L)
    # plt.show()

    return array_A, array_L


def check_animal_number(array_antelope, array_lion, epsilon):
    for i in range(1, len(array_antelope)):
        if np.abs(array_antelope[i] - array_antelope[i - 1]) > epsilon:
            return False

    for i in range(1, len(array_lion)):
        if np.abs(array_lion[i] - array_lion[i - 1]) > epsilon:
            return False

    return True


def main():
    epsilon, delta, A, L, start_time, delta_time, end_time, p = initialization()

    q = round(5.660377358490566, 3)
    r = round(5.357142857142855, 3)

    array_A, array_L = run_single_circle_of_life(A, L, start_time, end_time, delta_time, p, q, r)

    if check_animal_number(SAME_VALUE, array_A, array_L, epsilon):
        return p, q, r

    # current_q = 0
    # while current_q < 100:
    #
    #     current_r = 0
    #     while current_r < 100:
    #
    #         print(current_q, current_r)
    #
    #         array_A, array_L = run_single_circle_of_life(A, L, start_time, end_time, delta_time, p, q, r)
    #
    #         if check_animal_number(array_A, array_L, epsilon):
    #             return p, q, r
    #
    #         current_r = current_r + delta
    #
    #     current_q = current_q + delta

    return None, None, None


if __name__ == "__main__":
    p, q, r = main()

    print(f"p = {p}, q = {q}, r = {r}")
