import datetime

# date1 = datetime.datetime.now()
date1 = datetime.datetime.now().replace(microsecond=0)
date2 = datetime.datetime(2023, 2, 19, 21, 41, 30)
date1_in_sec = date1.timestamp()
date2_in_sec = date2.timestamp()
print(date1_in_sec - date2_in_sec)