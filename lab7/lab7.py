import csv

list_of_info = []

with open('communication_wells.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';', quotechar='|')
    for row in reader:
        list_of_info.append((row[0], row[1], int(row[2])))

class UnionFind:
    def __init__(self, elements):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def minimum_spanning_tree(well_distances, start_node='K1'):
    nodes = {u for u, v, _ in well_distances} | {v for u, v, _ in well_distances}
    class_obj = UnionFind(nodes)

    def sort_edges(edges):
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                if edges[i][2] > edges[j][2]:
                    edges[i], edges[j] = edges[j], edges[i]
        return edges
    
    sorted_edges = sort_edges(well_distances)

    group_of_well = []

    for u, v, w in sorted_edges:
        if class_obj.union(u, v):
            group_of_well.append((u, v, w))

    root_k1 = class_obj.find(start_node)

    counter = 0
    total_weight = 0
    for u, v, w in group_of_well:
        if class_obj.find(u) == root_k1:
            total_weight += w
            counter += 1

    if counter == 1:
        return -1
    return total_weight

def maximum_spanning_tree(well_distances, start_node='K1'):
    nodes = {u for u, v, _ in well_distances} | {v for u, v, _ in well_distances}
    class_obj = UnionFind(nodes)

    def sort_edges(edges):
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                if edges[i][2] < edges[j][2]:
                    edges[i], edges[j] = edges[j], edges[i]
        return edges
    
    sorted_edges = sort_edges(well_distances)

    group_of_well = []

    for u, v, w in sorted_edges:
        if class_obj.union(u, v):
            group_of_well.append((u, v, w))

    root_k1 = class_obj.find(start_node)

    counter = 0
    total_weight = 0
    for u, v, w in group_of_well:
        if class_obj.find(u) == root_k1:
            total_weight += w
            counter += 1

    if counter == 1:
        return -1
    return total_weight

def profit_count(min_length, max_length):
    if min_length == -1 or max_length == -1:
        return -1
    difference = max_length - min_length
    pay_to_government = (min_length* 30 * 15)/100
    profit = (difference * 30) - pay_to_government
    return profit

print(f"Мінімальна довжина кабелю: {minimum_spanning_tree(list_of_info)}")

money_we_can_get = profit_count(minimum_spanning_tree(list_of_info), maximum_spanning_tree(list_of_info))
if money_we_can_get <= 0:
    print("Неможливо наварити грошей")
else:
    print(f"Можна наварити грошей: {money_we_can_get}")
