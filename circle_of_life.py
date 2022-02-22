import numpy as np
import matplotlib.pyplot as plt

from automate import *

SAME_VALUE = 0
SAME_RATIO = 1


def initialization():
    decimal_places = 2
    epsilon = 10 ** (-decimal_places)
    delta = epsilon

    start_time = 0
    delta_time = 1
    end_time = 100

    A = 100.
    L = 30.

    p = 6.

    return decimal_places, epsilon, delta, A, L, start_time, delta_time, end_time, p


def run_single_circle_of_life(start_A, start_L, start_t, end_t, delta_t, p, q, r):
    current_time = start_t
    end_time = end_t

    array_t = [0]
    array_A = [start_A]
    array_L = [start_L]

    A = start_A
    L = start_L

    while current_time < end_time:
        A = apply_p(A, p)
        A, L = apply_q(L, A, q)
        L = apply_r(L, r)

        current_time += delta_t

        array_t.append(current_time)
        array_A.append(A)
        array_L.append(L)

    array_A = np.asarray(array_A)
    array_L = np.asarray(array_L)

    return array_t, array_A, array_L


def equal_number_check(array_time, array_antelope, array_lion, epsilon):

    for i in range(1, len(array_antelope)):
        if np.abs(array_antelope[i] - array_antelope[i - 1]) > epsilon:
            return False

    for i in range(1, len(array_lion)):
        if np.abs(array_lion[i] - array_lion[i - 1]) > epsilon:
            return False

    plt.plot(array_time, array_antelope)
    plt.plot(array_time, array_lion)
    plt.show()

    return True


def equal_ratio_check(array_time, array_antelope, array_lion, epsilon):

    array_ratio = array_lion / array_antelope
    #print(array_antelope, array_lion)

    for i in range(1, len(array_ratio)):
        if np.abs(array_ratio[i] - array_ratio[i - 1]) > epsilon:
            return False

    if (max(array_ratio) - min(array_ratio)) > epsilon:
        return False

    plt.plot(array_time, array_ratio)
    plt.show()

    return True


def check_animal_number(check_type, array_time, array_antelope, array_lion, epsilon):

    if check_type == SAME_VALUE:
        return equal_number_check(array_time, array_antelope, array_lion, epsilon)
    elif check_type == SAME_RATIO:
        return equal_ratio_check(array_time, array_antelope, array_lion, epsilon)


def main():
    decimal_places, epsilon, delta, A, L, start_time, delta_time, end_time, p = initialization()
    """
    q = round(5.660377358490566, decimal_places)
    r = round(5.357142857142855, decimal_places)
    array_t, array_A, array_L = run_single_circle_of_life(A, L, start_time, end_time, delta_time, p, q, r)

    if check_animal_number(SAME_RATIO, array_t, array_A, array_L, epsilon):
        print(q, r)
    """
    q = delta
    while q < 100:

        r = delta
        while r < 100:

            # print(q, r)
            array_t, array_A, array_L = run_single_circle_of_life(A, L, start_time, end_time, delta_time, p, q, r)

            if check_animal_number(SAME_RATIO, array_t, array_A, array_L, epsilon):
                return p, q, r

            r = round(r + delta, decimal_places)

        q = round(q + delta, decimal_places)

        if (q * 100) % 10 == 0:
            print(f"{q}% finished")

    return None, None, None


if __name__ == "__main__":
    p, q, r = main()

    print(f"p = {p}, q = {q}, r = {r}")
