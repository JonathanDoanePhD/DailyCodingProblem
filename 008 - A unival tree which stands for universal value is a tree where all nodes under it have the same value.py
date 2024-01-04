nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
values = [0, 1, 0, 1, 1, 1, 0]
edges = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f'), ('c', 'g')]
tree = [nodes, values, edges]

illustration = """

   a0
  /  \\
 b1  c0
    /  \\
   d1   g0
  /  \\
 e1   f1
 
 """
print(illustration)

def Edge_Good(in_edge=edges[0], in_tree=tree):
    e = in_edge
    N, V, E = in_tree
    i, j = N.index(e[0]), N.index(e[1])
    v, u = V[i], V[j]
    return v == u

def Node_Local_Good(in_node=nodes[3], in_tree=tree):
    n = in_node
    N, V, E = in_tree
    es = [x for x in E if n == x[0]]
    return bool(min([1] + [int(Edge_Good(e)) for e in es]))

def Nodes_in_Subtree(in_node=nodes[2], in_tree=tree):
    n = in_node
    N, V, E = in_tree
    out = [n]
    es = [x for x in E if n == x[0]]
    new = [x[1] for x in es]
    while new != []:
        out = out + new
        es = []
        for y in new:
            es = es + [x for x in E if y == x[0]]
        new = [x[1] for x in es]
    return out

def Node_Fully_Good(in_node=nodes[4], in_tree=tree):
    n = in_node
    N, V, E = in_tree
    t = in_tree
    nis = Nodes_in_Subtree(n, t)
    es = []
    for y in nis:
        es = es + [x for x in E if y == x[0]]
    # print(n)
    return bool(min([1] + [int(Edge_Good(e)) for e in es]))

# def Path_Good(in_path=[('a', 'c'), ('c', 'g')], in_tree=tree):
#     p = in_path
#     N, V, E = in_tree
#     return bool(min([int(Edge_Good(e)) for e in p]))

# def Path_Elig(in_path=)

def ANS(in_tree=tree):
    N, V, E = in_tree
    return sum([1 for x in N if Node_Fully_Good(x)])

print(ANS())
