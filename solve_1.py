dist = {1:{2:1,3:12},
        2:{3:9,4:3},
        3:{5:5},
        4:{3:4,5:13,6:15},
        5:{6:4},
        6:{6:0}}
cost = {1:0,2:1,3:12,4:999,5:999,6:999}

parents = {1:None,2:1,3:2,4:2,5:3,6:5}
visited = [1]

def findshoresNoed(cost):
	minDist = 999
	node = None
	for i in dist.keys():
		if (cost[i]<minDist)&(i not in visited):
			minDist = cost[i]
			node = i
	return node

node = findshoresNoed(cost)
while node:
	for i in dist[node]:
		newcost = cost[node] + dist[node][i]
		if newcost < cost[i]:
			parents[i] = node
			cost[i] = newcost
	visited.append(node)
	node = findshoresNoed(cost)
	
parent = parents[6]
while parent:
	print(parent)
	parent = parents[parent]
	
print(cost)

	

