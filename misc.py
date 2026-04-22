# l=[x for x in range(10)]

# print(l)

import time
from datetime import datetime,timedelta

print(f"time: {time.time()} datetime: {datetime.now()}")
tomorrow=datetime.now()+timedelta(days=1)
print(tomorrow)
print(tomorrow.strftime("%d-%m-%Y"))