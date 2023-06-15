class SingleServerQueueing:
    def __init__(self):
        self.cust_no = 0
        self.rd_ar = 0
        self.inter_arr_time = 0
        self.arr_time = 0
        self.rd_se = 0
        self.service_begin = 0
        self.service_time = 0
        self.time_ser_end = 0
        self.waiting_time = 0
        self.idle_time = 0
        self.spend = 0


def schedule_arrival_time(lOf_Instance, nCust_SSQ):
    for i in range(2, nCust_SSQ + 1):
        lOf_Instance[i].arr_time = lOf_Instance[i - 1].arr_time + lOf_Instance[i].inter_arr_time


def schedule_service_time(lOf_Instance, nCust_SSQ):
    for i in range(2, nCust_SSQ + 1):
        if lOf_Instance[i].arr_time > lOf_Instance[i - 1].time_ser_end:
            lOf_Instance[i].service_begin = lOf_Instance[i].arr_time
        else:
            lOf_Instance[i].service_begin = lOf_Instance[i - 1].time_ser_end


def schedule_completion_of_service(lOf_Instance, nCust_SSQ):
    for i in range(1, nCust_SSQ + 1):
        lOf_Instance[i].time_ser_end = lOf_Instance[i].service_begin + lOf_Instance[i].service_time


def waiting_and_idle_time(lOf_Instance, nCust_SSQ):
    lOf_Instance[1].waiting_time = 0
    lOf_Instance[1].idle_time = 0
    total_waiting_time = 0
    total_idle_time = 0
    wait_count = 0
    for i in range(2, nCust_SSQ + 1):
        if lOf_Instance[i].arr_time > lOf_Instance[i - 1].time_ser_end:
            lOf_Instance[i].idle_time = lOf_Instance[i].arr_time - lOf_Instance[i - 1].time_ser_end
            total_idle_time += lOf_Instance[i].idle_time
            lOf_Instance[i].waiting_time = 0
        else:
            lOf_Instance[i].waiting_time = lOf_Instance[i - 1].time_ser_end - lOf_Instance[i].arr_time
            total_waiting_time += lOf_Instance[i].waiting_time
            lOf_Instance[i].idle_time = 0
        if lOf_Instance[i].waiting_time != 0:
            wait_count += 1
    return total_waiting_time, total_idle_time, wait_count


def schedule_spend_time(lOf_Instance, nCust_SSQ):
    total_spend_time = 0
    for i in range(1, nCust_SSQ + 1):
        lOf_Instance[i].spend = lOf_Instance[i].service_time + lOf_Instance[i].waiting_time
        total_spend_time += lOf_Instance[i].spend
    return total_spend_time


def main():
    nCust_SSQ = int(input("Enter customer number: "))
    lOf_Instance = [SingleServerQueueing() for _ in range(nCust_SSQ + 1)]
    total_service_time = 0

    for i in range(1, nCust_SSQ + 1):
        if i == 1:
            print("  RD.Arrival[1]: 0")
            lOf_Instance[i].cust_no = 1
            lOf_Instance[i].rd_ar = 0
            lOf_Instance[i].inter_arr_time = 0
        else:
            print(f"  RD.Arrival[{i}]: ", end="")
            lOf_Instance[i].rd_ar = int(input())
            lOf_Instance[i].cust_no = i

            # Arrival Time ----------------------------

            if 0 <= lOf_Instance[i].rd_ar <= 1000:
                lOf_Instance[i].inter_arr_time = (lOf_Instance[i].rd_ar - 1) // 125 + 1
            else:
                print("Enter Random Number. Up to 1000")
                return

    schedule_arrival_time(lOf_Instance, nCust_SSQ)

    print("Enter Random Digit for [ Service Time ] for each customer: ")

    for i in range(1, nCust_SSQ + 1):
        if i == 1:
            lOf_Instance[i].service_begin = 0

        print(f"  RD.Service[{i}]: ", end="")
        lOf_Instance[i].rd_se = int(input())

        # Service Time ----------------------------

        if 1 <= lOf_Instance[i].rd_se <= 10:
            lOf_Instance[i].service_time = 1
        elif 11 <= lOf_Instance[i].rd_se <= 30:
            lOf_Instance[i].service_time = 2
        elif 31 <= lOf_Instance[i].rd_se <= 60:
            lOf_Instance[i].service_time = 3
        elif 61 <= lOf_Instance[i].rd_se <= 85:
            lOf_Instance[i].service_time = 4
        elif 86 <= lOf_Instance[i].rd_se <= 95:
            lOf_Instance[i].service_time = 5
        elif 96 <= lOf_Instance[i].rd_se <= 100:
            lOf_Instance[i].service_time = 6
        else:
            print("Enter Random Number. Up to 100")
            return

        total_service_time += lOf_Instance[i].service_time

    for _ in range(1, nCust_SSQ + 1):
        schedule_service_time(lOf_Instance, nCust_SSQ)
        schedule_completion_of_service(lOf_Instance, nCust_SSQ)

    total_waiting_time, total_idle_time, wait_count = waiting_and_idle_time(lOf_Instance, nCust_SSQ)
    total_spend_time = schedule_spend_time(lOf_Instance, nCust_SSQ)

    print("\n ", "-" * 116)
    print(
        "  | Cust.| RN. for | Inter_arrival | Arrival | RN. for | Service | T.Service| T.Service| Waiting | Server | Spend in |")
    print(
        "  |  No. |Arrival.T|     Time      |  Time   |Service.T|  Time   |  Begin   |    End   | in Queue| Idle.T |  System  |")
    print("  |" + "-" * 114 + "|")
    for i in range(1, nCust_SSQ + 1):
        print(
            f"    {lOf_Instance[i].cust_no:3d}     {lOf_Instance[i].rd_ar:3d}         {lOf_Instance[i].inter_arr_time:3d}          {lOf_Instance[i].arr_time:3d}       {lOf_Instance[i].rd_se:3d}        {lOf_Instance[i].service_time:3d}       {lOf_Instance[i].service_begin:3d}         {lOf_Instance[i].time_ser_end:3d}       {lOf_Instance[i].waiting_time:3d}       {lOf_Instance[i].idle_time:3d}       {lOf_Instance[i].spend:3d}")
        if i != nCust_SSQ:
            print("  |" + "-" * 114 + "|")
        else:
            print(" ", "=" * 116)

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t    {}\t\t\t\t\t\t\t    {}\t      {}\t\t\t{}".format(total_service_time,
                                                                                            total_waiting_time,
                                                                                            total_idle_time,
                                                                                            total_spend_time))

    try:
        print(f"\n Average waiting time = {total_waiting_time / nCust_SSQ:.2f}")
        print(f" Probability(wait) = {wait_count / nCust_SSQ:.2f}")
        print(f" Probability of idle server = {total_idle_time / lOf_Instance[nCust_SSQ].time_ser_end:.2f}")
        print(f" Average service time = {total_service_time / nCust_SSQ:.2f}")
        print(f" Average time between arrival = {lOf_Instance[nCust_SSQ].arr_time / (nCust_SSQ - 1):.2f}")
        print(f" Average waiting time of those who wait = {total_waiting_time / wait_count:.2f}")
        print(f" Average time customer spends in the system = {total_spend_time / nCust_SSQ:.2f}\n\n")


    except ZeroDivisionError as e:
        print("An exception occurred:", type(e).__name__)


if __name__ == "__main__":
    main()
