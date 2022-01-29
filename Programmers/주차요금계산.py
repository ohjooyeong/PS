# 주차요금계산

import math


def time_to_min(time):
    hour, min = time.split(":")
    hour_to_min = int(hour) * 60
    min = int(min)
    return hour_to_min + min


def res_money(fees, bet_time):
    time, fee, unit_time, unit_fee = fees
    if bet_time <= time:
        return fee
    else:
        res = fee + (math.ceil((bet_time - time) / unit_time) * unit_fee)
        return res


def solution(fees, records):
    answer = [0] * 10000
    res = []
    reco_dict = {}
    for record in records:
        car_time, car_num, car_status = record.split(" ")
        if car_num not in reco_dict:
            reco_dict[car_num] = [time_to_min(car_time)]
        else:
            if car_status == "IN":
                reco_dict[car_num].append(time_to_min(car_time))
            else:
                in_time = reco_dict[car_num].pop()
                out_time = time_to_min(car_time)
                answer[int(car_num)] += out_time - in_time

    for key in reco_dict:
        if len(reco_dict[key]) > 0:
            in_time = reco_dict[key].pop()
            out_time = time_to_min("23:59")
            answer[int(key)] += out_time - in_time

    for key in reco_dict:
        res.append([key, res_money(fees, answer[int(key)])])
    res.sort()
    res = [res[i][1] for i in range(len(res))]

    return res


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
