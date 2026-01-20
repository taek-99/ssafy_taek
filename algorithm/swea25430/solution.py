
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

    global house_list

    N = len(house_list)
    INF = 10**18

    def multisource_dijkstra(sources):
        dist = [INF] * N
        pq = []

        # 여러 시작점 모두 0으로
        for s in sources:
            if dist[s] != 0:
                dist[s] = 0
                heapq.heappush(pq, (0, s))

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            if d > R:
                continue  # R 넘으면 더 확장할 필요 없음(가중치 양수 가정)

            for v, w in house_list[u].items():
                nd = d + w
                if nd <= R and nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        return dist

    coffee_dist = multisource_dijkstra(mCoffee)
    bakery_dist = multisource_dijkstra(mBakery)

    ans = INF
    for i in range(N):
        # 기존 의도 유지: 가게 노드(거리 0)는 제외
        if 0 < coffee_dist[i] < INF and 0 < bakery_dist[i] < INF:
            s = coffee_dist[i] + bakery_dist[i]
            if s < ans:
                ans = s

    return -1 if ans == INF else ans
