from csv import DictReader
import numpy as np


def electrostatic_solver():
    """This function calculates and returns unknown potential nodes in 2 dimensions and linear electrostatic problem,
    through the variational methods from the element finite method"""

    nodes = {}  # Dictionary to register the coordinates from each node

    k_potential = []  # List to store the known potential nodes.
    b = []  # List to store the value of potential nodes
    elements = {}  # Dictionary that contais all the elements and its aspects
    k = 0

    with open('entries.csv') as csv_file:  # Opening the CSV file.

        # -------------------------------- Collecting the coordinates and potential for the nodes ----------------------
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            # Creation of the nodes matrix
            nodes[k] = [float(row['coord_x']), float(row['coord_y']), row['potential']]

            if row['potential']:
                k_potential.append(k)
                b.append(float(row['potential']))
            else:
                b.append(0.0)
            k += 1

        # Global Matrix
        n_nodes = len(nodes)
        global_system = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]

        # ------------------------------ Calculating aspects from each element -----------------------------------------

        k = 0
        csv_file.seek(0)  # Returns the iterator to the first row.
        csv_reader = DictReader(csv_file)

        for row in csv_reader:
            if row['elem_global_nodes']:
                l_nodes = list(map(int, row['elem_global_nodes'].split("-")))
                l_nodes = [n - 1 for n in l_nodes]

                # Obtaining x, y, p, q, r and d_;
                x = [nodes[l_nodes[0]][0],
                     nodes[l_nodes[1]][0],
                     nodes[l_nodes[2]][0]]

                y = [nodes[l_nodes[0]][1],
                     nodes[l_nodes[1]][1],
                     nodes[l_nodes[2]][1]]

                p = [x[1] * y[2] - x[2] * y[1],
                     x[2] * y[0] - x[0] * y[2],
                     x[0] * y[1] - x[1] * y[0]]

                q = [y[1] - y[2],
                     y[2] - y[0],
                     y[0] - y[1]]

                r = [x[2] - x[1],
                     x[0] - x[2],
                     x[1] - x[0]]

                d_ = abs(p[0] + p[1] + p[2])
                elements[k] = {'nodes': l_nodes, 'permissiveness': float(row['permissiveness']), 'x': x, 'y': y, 'p': p,
                               'q': q, 'r': r, 'd_': d_}
                k += 1

    # ----------------------------------------- Contributions to the Global Matrix -------------------------------------
    for element in elements:
        for i in range(3):
            for j in range(3):
                i_g = elements[element]['nodes'][i]
                j_g = elements[element]['nodes'][j]
                perm = elements[element]['permissiveness']
                q_t = elements[element]['q'][i] * elements[element]['q'][j]
                r_t = elements[element]['r'][i] * elements[element]['r'][j]
                d_g = elements[element]['d_']

                global_system[i_g][j_g] += (perm / (2 * d_g)) * (q_t + r_t)

    for i in k_potential:
        for j in range(n_nodes):
            if i == j:
                global_system[i][j] = 1
            else:
                global_system[i][j] = 0

    # ---------------------------------------- Solving the equations ---------------------------------------------------

    global_system = np.array(global_system)
    b = np.array(b)
    v = np.linalg.solve(global_system, b)
    v = list(v)
    v = [round(n, 8) for n in v]
    return v
