
house_list = {}
ans_coffee_dict = {}
ans_bakery_dict = {}

def init(N, K, sBuilding, eBuilding, mDistance):
	global house_list, ans_coffee_dict, ans_bakery_dict

	ans_coffee_dict = {x: float('inf') for x in range(N)}
	ans_bakery_dict = {x: float('inf') for x in range(N)}
	house_list = {x: {} for x in range(N)}	

	for idx in range(K):
		s = sBuilding[idx]
		e = eBuilding[idx]
		d = mDistance[idx]

		house_list[s][e] = d
		house_list[e][s] = d
	return


def add(sBuilding, eBuilding, mDistance):
	global house_list

	s = sBuilding
	e = eBuilding
	d = mDistance

	house_list[s][e] = d
	house_list[e][s] = d
	return


def calculate(M, mCoffee, P, mBakery, R):
	import heapq
	from collections import defaultdict

	global house_list, ans_coffee_dict, ans_bakery_dict

	heap_list = {x: float('inf') for x in range(len(house_list))}
	## 커피점
	for idx in range(M):
		min_heap = []
		heapq.heappush(min_heap, [0, mCoffee[idx]])
		heap_list[mCoffee[idx]] = 0

		while min_heap:
			v, pos = heapq.heappop(min_heap)

			if heap_list[pos] < v or heap_list[pos] > R:
				continue
			
			if v != 0 :
				ans_coffee_dict[pos] = min(v, ans_coffee_dict[pos])

			for next_pos, weight in house_list[pos].items():
				distance = weight + v
				if distance < heap_list[next_pos]:
					heap_list[next_pos] = distance
					heapq.heappush(min_heap, [distance, next_pos])


	heap_list = {x: float('inf') for x in range(len(house_list))}
	## 베이커리
	for idx in range(P):	
		min_heap = []
		heapq.heappush(min_heap, [0, mBakery[idx]])
		heap_list[mBakery[idx]] = 0

		while min_heap:
			v, pos = heapq.heappop(min_heap)

			if heap_list[pos] < v or heap_list[pos] > R:
				continue
			
			if v != 0 :
				ans_bakery_dict[pos] = min(v, ans_bakery_dict[pos])

			for next_pos, weight in house_list[pos].items():
				distance = weight + v
				if distance < heap_list[next_pos]:
					heap_list[next_pos] = distance
					heapq.heappush(min_heap, [distance, next_pos])


	print ("===============")
	print (ans_coffee_dict)
	print (ans_bakery_dict)
	print ("===============")

	return -1