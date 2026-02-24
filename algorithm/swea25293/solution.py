from collections import deque
from math import gcd

train_list = {}

def init(N, K, mId, sId, eId, mInterval):
    global train_list
    train_list = {}
    for i in range(K):
        train_list[mId[i]] = (sId[i], eId[i], mInterval[i])

def add(mId, sId, eId, mInterval):
    train_list[mId] = (sId, eId, mInterval)

def remove(mId):
    train_list.pop(mId, None)





def _stops_at(t, x):
    s, e, d = t
    return s <= x <= e and (x - s) % d == 0

def _ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = _ext_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def _crt(a1, m1, a2, m2):
    g = gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None
    lcm = m1 // g * m2
    _, p, _ = _ext_gcd(m1, m2)
    m2_g = m2 // g
    k = ((a2 - a1) // g * p) % m2_g
    x = (a1 + m1 * k) % lcm
    return x, lcm

def _ceil_div(a, b):
    return -(-a // b)

def _trains_meet(t1, t2):
    s1, e1, d1 = t1
    s2, e2, d2 = t2
    L = max(s1, s2)
    R = min(e1, e2)
    if L > R:
        return False
    res = _crt(s1 % d1, d1, s2 % d2, d2)
    if res is None:
        return False
    x0, mod = res
    k = _ceil_div(L - x0, mod)
    x = x0 + k * mod
    return x <= R

def calculate(sId, eId):
    trains = list(train_list.values())

    T = len(trains)
    if T == 0:
        return -1

    start = []
    end = set()
    for i, t in enumerate(trains):
        if _stops_at(t, sId):
            start.append(i)
        if _stops_at(t, eId):
            end.add(i)

    if not start or not end:
        return -1

    for i in start:
        if i in end:
            return 0

    adj = [[] for _ in range(T)]
    for i in range(T):
        ti = trains[i]
        for j in range(i + 1, T):
            if _trains_meet(ti, trains[j]):
                adj[i].append(j)
                adj[j].append(i)

    dist = [-1] * T
    q = deque()
    for i in start:
        dist[i] = 1
        q.append(i)

    while q:
        cur = q.popleft()
        nd = dist[cur] + 1
        for nxt in adj[cur]:
            if dist[nxt] != -1:
                continue
            if nxt in end:
                return nd - 1
            dist[nxt] = nd
            q.append(nxt)

    return -1