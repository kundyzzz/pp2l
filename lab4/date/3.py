from datetime import datetime
curdt= datetime.now()
curmic = curdt.replace(microsecond=0)
print(curmic)