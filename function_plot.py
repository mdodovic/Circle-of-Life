import numpy as np
import matplotlib.pyplot as plt


def main():
    x = 0.01
    x_array = []
    y_array = []
    while x <= 1:
        y = np.sqrt(-(50 * (1 - 2 * x) + 2500 * x * (x - 2)))
        x_array.append(x)
        y_array.append(y)
        x = x + 0.01

    plt.plot(x_array, y_array)
    plt.savefig('y=f(x).png', dpi=90)
    plt.show()


if __name__ == "__main__":
    main()
