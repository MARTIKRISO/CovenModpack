import re

global data

file = r"./list_from_thunderstore.txt"

with open(file, "r") as f:
    data = f.readlines()

out = ", \n".join([f'"{f.strip()}"' for f in data if not re.match(r"TheCoven-TheCovenModpack-[0-9]\.[0-9]\.[0-9]", f)])

with open(file, "w") as f:
    f.write(out)

print(out)