import re

global data

with open("util\\list_from_thunderstore.txt", "r") as f:
    data = f.readlines()

out = ", \n".join([f'"{f.strip()}"' for f in data if not re.match(r"TheCoven-TheCovenModpack-[0-9]\.[0-9]\.[0-9]", f)])

print(out)