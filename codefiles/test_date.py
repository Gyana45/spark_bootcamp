from datetime import datetime, timedelta
import numpy as np



START_DATE = datetime(2000, 1, 1)
END_DATE = datetime(2024, 12, 31)

def random_dates(n, start, end):
    delta = end - start
    return [start + timedelta(days=np.random.randint(0, delta.days)) for _ in range(n)]


random_dates=random_dates(1, START_DATE, END_DATE)
print(random_dates)