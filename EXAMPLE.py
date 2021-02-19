# Algorithm created to solve Electrostatic Problems in 2 dimensions of first order, using the numpy library.
import numpy as np

nodes = {}  # Dictionary to register the coordinates from each node
n_nodes = int(input("How many nodes?\n"))
k_potential = []  # List to store the known potential nodes.
b = []  # List to store the value of potential nodes
elements = {}  # Dictionary that contais all the elements and its aspects

# -------------------------------- Collecting the coordinates and potential for the nodes ------------------------------
for n in range(n_nodes):
    info = input(f'Insert the coordinates of the node {n + 1} separating with semicolons: "X;Y:')
    l_info = list(map(float, info.split(";")))
    nodes[n] = l_info
    v_n = input(f'Insert the potential of the node {n + 1} if its known otherwise just press enter:')
    if v_n:
        k_potential.append(n)
        b.append(float(v_n))
    else:
        b.append(0)

# Global Matrix
global_system = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]

n_elements = int(input('Insert the number of elements: \n'))

# ------------------------------ Calculating aspects from each element -------------------------------------------------
for n in range(n_elements):
    e_nodes = input(
        'Insert the global nodes of element ' + str(n + 1) + ' separating with "-": "1-2-4"\n')
    l_nodes = list(map(int, e_nodes.split("-")))
    l_nodes = [n - 1 for n in l_nodes]
    permissiveness = float(input('Insert the permissiveness of the material:\n'))

    # Obtaining x, y, p, q, r and D;
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

    D = p[0] + p[1] + p[2]
    D = abs(D)

    elements[n] = {'nodes': l_nodes, 'permissiveness': permissiveness, 'x': x, 'y': y, 'p': p, 'q': q, 'r': r, 'D': D}

# ----------------------------------------- Contributions to the Global Matrix -----------------------------------------
for element in elements:
    for i in range(3):
        for j in range(3):
            i_g = elements[element]['nodes'][i]
            j_g = elements[element]['nodes'][j]
            perm = elements[element]['permissiveness']
            q_t = elements[element]['q'][i] * elements[element]['q'][j]
            r_t = elements[element]['r'][i] * elements[element]['r'][j]
            D_g = elements[element]['D']

            global_system[i_g][j_g] += (perm / (2 * D_g)) * (q_t + r_t)

for i in k_potential:
    for j in range(n_nodes):
        if i == j:
            global_system[i][j] = 1
        else:
            global_system[i][j] = 0

# ---------------------------------------- Solving the equations -------------------------------------------------------
global_system = np.array(global_system)
b = np.array(b)
V = np.linalg.solve(global_system, b)
for n in range(n_nodes):
    print(f'V{n+1}={V[n]}\n')
