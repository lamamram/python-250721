from datetime import datetime

def log(obj, level="info"):
  print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:{level}: {obj}")