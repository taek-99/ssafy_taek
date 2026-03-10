class RESULT_E:
    def __init__(self, success, locname):
        self.success = success
        self.locname = locname

class RESULT_S:
    def __init__(self, cnt, carlist):
        self.cnt = cnt
        self.carlist = carlist # [str] * 5

car_data = {}

towing_list = []

global_n = 0
global_m = 0
global_l = 0

park_name = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def init(N: int, M: int, L: int) -> None:
    global car_data, towing_list, timer_l, park_name
    global global_l, global_m, global_n

    car_data = {}

    for idx in range(N):

        car_data[park_name[idx]] = {
            "parking": [""] * M,
            "visited": [False] * M,
            "timer": [0] * M,
            "count": M
        }

    towing_list = []
    global_n = N
    global_m = M
    global_l = L


def enter(mTime : int, mCarNo : str) -> RESULT_E:
    global car_data, towing_list, park_name
    global global_l, global_m, global_n

    ## 빈슬롯이 가장 많은 구역 중 영역의 대문자 순서가 가장 앞선 구역 선택
    max_park = -1
    max_park_num = ""
    for idx in park_name[:global_n]:
        if car_data[idx]["count"] > max_park:
            max_park = car_data[idx]["count"]
            max_park_num = idx


    ## 선택된 구역에서 숫자 번호가 가장 앞선 빈 슬롯에 차량이 보관이 된다.
    for idx, val in enumerate(car_data[max_park_num]["visited"]):
        if val == False:
            ## 주차 성공
            car_data[max_park_num]["parking"][idx] = mCarNo
            car_data[max_park_num]["visited"][idx] = True
            car_data[max_park_num]["timer"][idx] = mTime
            car_data[max_park_num]["count"] -= 1
            return RESULT_E(1, f"{max_park_num}{idx:03}")
        


    ## 견인차량 확인
    for val, park_time, towing_time in towing_list:
        if val == mCarNo:
            towing_list.remove((val, park_time, towing_time))


    ## 만약 어느 구역에도 빈 슬롯이 없는 경우 주차는 실패한다
    return RESULT_E(-1, "")
    

def pullout(mTime : int, mCarNo : str) -> int:
    global car_data, towing_list, park_name
    global global_l, global_m, global_n


    ## 견인된건지부터 확인
    for val, park_time, towing_time in towing_list:
        if val == mCarNo:
            towing_list.remove((val, park_time, towing_time))
            return (((mTime-park_time)+(mTime-towing_time)) * 5) * -1


    ## 주차장에 있는지 확인
    for idx in park_name[:global_n]:
        for num, val in enumerate(car_data[idx]["parking"]):
            if val == mCarNo:
                park_time = car_data[idx]["timer"][num]

                car_data[idx]["parking"][num] = ""
                car_data[idx]["visited"][num] = False
                car_data[idx]["timer"][num] = 0
                car_data[idx]["count"] += 1

                return mTime - park_time

    return -1

def search(mTime : int, mStr : str) -> RESULT_S:
    global car_data, towing_list, park_name
    global global_l, global_m, global_n

    search_car_count = 0
    search_car_list = []


    ## 주차장에 있는지 확인
    for idx in park_name[:global_n]:
        for val in car_data[idx]["parking"]: 
            if mStr == val[:-4]:
                search_car_count += 1
                search_car_list.append(val)     

            if search_car_count == 5:
                return RESULT_S(search_car_count, search_car_list)
    

    ## 견인목록에 있는지 확인     
    for val, park_time, towing_time in towing_list:
        if mStr == val[:-4]:
            search_car_count += 1
            search_car_list.append(val)     

        if search_car_count == 5:
            return RESULT_S(search_car_count, search_car_list)
        
    
    return RESULT_S(search_car_count, ["", "", "", "", ""])
