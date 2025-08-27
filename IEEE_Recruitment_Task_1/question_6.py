from collections import defaultdict
list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Eco", 271),
    ("Pilani", "Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Eco", 263),
    ("Goa", "Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Eco", 261),
    ("Hyderabad", "Bio", 234),
]

d=defaultdict(dict)
for campus, branch, marks in list:
    d[campus][branch] = marks

d=dict(d)
print(d)