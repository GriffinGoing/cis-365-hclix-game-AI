class node:
  def __init__(self, name, adjacentTo, walls):
    self.name = name
    self.adjacentTo = adjacentTo
    self.walls = walls


def buildGraph():
  graph = {}  # dictionary of nodes

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

  for i in range(0, 16):
    print(letters[i])
    for k in range(0, 16):
      nodeName = letters[i] + str(k)
      newNode = node(nodeName, [0], [0])
      graph[nodeName] = newNode

  return graph


board = buildGraph()

#print('a' + str(1))

for node in board:
  print(board[node].name)
