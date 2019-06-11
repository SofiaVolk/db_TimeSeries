from statistics import median

DATASET = 'logs/logs_1m_each_1t_ts.txt'

dataset_list = []
with open(DATASET, 'r') as file:
    dataset_list = file.read().split('\n')
dataset_list = [float(item) for item in dataset_list[:len(dataset_list)-1]]
print(median(dataset_list))
