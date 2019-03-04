import numpy as np
import matplotlib.pyplot as plt


line_width = 1.0
label_length = 0.2
label_width = 3.0


def solve(xco, yco):
    x0, y0 = xco[0], yco[0]
    x1, y1 = xco[1], yco[1]
    A = np.array([
            [x0**3,   x0**2, x0, 1],
            [x1**3,   x1**2, x1, 1],
            [3*x0**2,  2*x0,  1, 0],
            [3*x1**2,  2*x1,  1, 0]])
    b = np.array([y0, y1, 0, 0])
    coeff = np.linalg.solve(A, b)
    xlink = np.linspace(x0, x1, 101)
    ylink = np.polyval(coeff, xlink)
    return xlink, ylink


def draw_mep(x, y, color, **kwargs):
    state = np.array(x)
    energy = np.array(y)
    # Draw the line connecting all images
    state_link = np.array([])
    energy_link = np.array([])
    for i in range(energy.size-1):
        xlink, ylink = solve(state[i:i+2], energy[i:i+2])
        state_link = np.append(state_link, xlink)
        energy_link = np.append(energy_link, ylink)
    plt.plot(state_link, energy_link, linewidth=line_width, color=color, **kwargs)
    # Add energy levels
    for i, coord in enumerate(state):
        label_x = np.array([coord - label_length / 2, coord + label_length / 2])
        label_y = np.array([energy[i], energy[i]])
        plt.plot(label_x, label_y, linewidth=label_width, color=color)


def main():
    state = [1, 2, 3, 4, 5, 6]
    energy1 = [0.0, 26.6, 16.7, 25.5, 26.5, 10.0]
    energy2 = [0.0, 28.6, 15.7, 27.5, 30.5, 11.0]
    state_label = ["R", "TS1", "IM1", "IM2", "TS2", "P"]
    plt.figure(figsize=(7,4))
    draw_mep(state, energy2, "red", label="cat-2")
    draw_mep(state, energy1, "blue", label="cat-1")
    plt.xticks(state, state_label)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()