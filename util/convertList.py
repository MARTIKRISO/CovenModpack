import re

global data
with open("list_from_thunderstore.txt", "r") as f:
    data = f.readlines()

out = ", \n".join([f'"{f.strip()}"' for f in data if not re.match(r'(?:Coven)', f)])

print(out)