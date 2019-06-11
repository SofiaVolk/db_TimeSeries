import requests
import to_sqlite


url = "https://www.ncei.noaa.gov/access/services/data/v1?" \
      "dataset=global-marine&dataTypes=WIND_DIR,WIND_SPEED&" \
      "stations=AUCE&startDate=2019-01-01&endDate=2019-01-31&" \
      "boundingBox=90,-180,-90,180"


r = requests.get(url)
row_dataset = [i for i in r.text.split('\n')]

data_temp = []
with open('dataset', 'w') as file:
    for _ in row_dataset:
        data_temp.append(_.split(','))
    file.write(str(data_temp[1:len(data_temp) - 2]))

# to_sqlite.write_each(data_temp)
to_sqlite.write_batch(data_temp)
