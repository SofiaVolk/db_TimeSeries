import time
from opentsdb_module import insert_to_opentsdb

TEST_1_SEC = 1
TEST_1_MIN = 60
TEST_3_MIN = 180
TEST_5_MIN = 300
TEST_15_MIN = 900
TEST_30_MIN = 1800
BATCH_1 = 1
BATCH_2 = 2
BATCH_10 = 10
BATCH_50 = 50

TEST_DURATION = TEST_3_MIN
BATCH_SIZE = BATCH_50


def form_data():
    with open('dataset', 'r') as file:
        row_dataset = file.readline()

    data = []
    data_temp = [i for i in row_dataset.split(']')]
    for _ in data_temp[:233]:
        data.append(_.split('[')[1])
    data_temp = []
    for _ in data:
        data_temp.append(_.split('"')[1::2])

    write_each(data_temp[1:])


def write_each(data_temp):
    c = 0
    start_write_to_db = time.time()
    stop_write_to_db = start_write_to_db + TEST_DURATION
    with open('logs/logs_3m_each_1t_ts.txt', 'w') as file:
        for i in data_temp:
            while time.time() < stop_write_to_db:
                start_time = time.time()
                insert_to_opentsdb(i[4:], c)
                c += 1
                # print(time.time() - start_time)
                file.write(str(time.time() - start_time) + '\n')

    print(f'total_write_to_db = {time.time() - start_write_to_db}')


def write_batch(data_temp):
    data_list = []
    start_write_to_db = time.time()
    stop_write_to_db = start_write_to_db + TEST_DURATION
    with open('logs_30min_batch_ts.txt', 'w') as file:
        while time.time() < stop_write_to_db:
            for i in data_temp[1:len(data_temp) - 2]:
                data = []
                for w in i:
                    data.append(w.split('"')[1])

                if len(data_list) == BATCH_SIZE:
                    start_time = time.time()
                    #insert_to_opentsdb(data_temp)
                    file.write(str(time.time() - start_time) + '\n')
                    data_list = []
                else:
                    data_list.append(tuple(data))

    print(f'total_write_to_db = {time.time() - start_write_to_db}')


form_data()
