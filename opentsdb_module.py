import time
from opentsdb import TSDBClient
import potsdb

tsdb = TSDBClient('0.0.0.0')
'''
tsdb.send('metric.test4', 'fwe', t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 'fwe', t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 'fwe', t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 22, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 22, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 22, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 202, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 23, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 24, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 25, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 6, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 206, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 20, t1='v1')
time.sleep(2)
tsdb.send('metric.test4', 24, t1='v1')
time.sleep(2)
'''
# tsdb.send('metric.test4', '209', t1='v1', t2='v2', t3='v3')
# time.sleep(2)


def insert_to_opentsdb(data, c):
    print(tsdb.is_connected())
    if tsdb.queue_size() >= 9999:
        print('wait for queue')
        time.sleep(0.1)
    # stat1 = tsdb.send('metric.weather', data[0], wd_tag='wind_dir')
    # print(f'done 1, i = {c}, {stat1}')
    tsdb.send('metric.weather', data[1], ws_tag='wind_speed')
    print(f'done 2, i = {c}')


# tsdb.close()
# tsdb.wait()
