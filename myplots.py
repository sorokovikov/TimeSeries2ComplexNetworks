from matplotlib import pyplot as plt

import networkx as nx
import numpy as np
import pandas as pd


def time_series(data, ax: plt.axes):
    x = np.arange(len(data))
    ax.plot(x, data)


def complex_network(data, ax: plt.axes):
    x = np.arange(len(data))
    ax.bar(x, data, width=0.20, data=data)
    graph(x, data, ax)


def complex_network_graph(data, ax: plt.axes):
    x = np.arange(len(data))
    nodes = get_graph_edges(x, data)
    G = nx.from_pandas_edgelist(nodes, 'source', 'target', 'weight')
    pos = nx.circular_layout(G)
    node_labels = dict([(s, round(s, 3)) for s in G.nodes()])
    edge_labels = dict([((s, t), w['weight']) for s, t, w in G.edges(data=True)])
    nx.draw_networkx(G, pos=pos, ax=ax, with_labels=False, node_color='pink', edge_color='blue')
    nx.draw_networkx_labels(G, pos=pos, ax=ax, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos=pos, ax=ax, edge_labels=edge_labels, font_color='red')


def graph(x, y, ax):
    ax.plot(x, y, color='green')
    stop = len(y)
    for i in range(0, stop - 2):
        for j in range(i + 2, stop):
            for k in range(i + 1, j):
                if has_intersection([x[i], y[i]], [x[j], y[j]], [x[k], y[k]]):
                    break
            else:
                ax.plot([x[i], x[j]], [y[i], y[j]])


def get_graph_edges(x, y):
    edges = pd.DataFrame(columns=['source', 'target', 'weight'])
    for i in range(len(y) - 1):
        edges = edges.append({'source': y[i], 'target': y[i + 1], 'weight': 1}, ignore_index=True)
    stop = len(y)
    for i in range(0, stop - 2):
        for j in range(i + 2, stop):
            for k in range(i + 1, j):
                if has_intersection([x[i], y[i]], [x[j], y[j]], [x[k], y[k]]):
                    break
            else:
                weight = x[j] - x[i]
                edges = edges.append({'source': y[i], 'target': y[j], 'weight': weight,
                                      'x1': x[i], 'x2': x[j]}, ignore_index=True)
    return edges


def has_intersection(a, b, c):
    result = b[1] + (a[1] - b[1]) * ((b[0] - c[0]) / (b[0] - a[0]))
    if c[1] < result:
        return False
    return True


file_path = 'DailyDelhiClimateTest.csv'
df = pd.read_csv(file_path, header=0)
data = df.to_numpy()
data = data[0:10, 3]
x = np.arange(len(data))

nodes = get_graph_edges(x, data)
print(nodes)

G = nx.from_pandas_edgelist(nodes, 'source', 'target', 'weight')

figure, axs = plt.subplots(2)

complex_network_graph(data, axs[0])

complex_network(data, axs[1])

plt.show()
