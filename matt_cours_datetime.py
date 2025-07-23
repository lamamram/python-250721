# %%
from datetime import datetime, timedelta

# maintenant
dt = datetime.now()
dt
# %%

date_str = "2025-07-23 17:30"

# strptime => "p" comme parse: str => dt
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
# timestamp => nb de secondes depuis le 1er janvier 1970 à Minuit => temps UNIX
dt.day, dt.weekday(), dt.year, dt.timestamp()

delta = dt - datetime.now()
delta

cuisson_oeuf_coque = timedelta(minutes=3)
a_table = datetime.now() + cuisson_oeuf_coque
# strftime => "f" comme format: dt => str
print(a_table.strftime("%d/%m/%Y %H:%M:%S"))

# %%
