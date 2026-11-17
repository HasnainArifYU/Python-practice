# ============================================
# WARM-UP (it's been a while, so take it easy)
# ============================================
servers = [
    {"name": "web-01", "region": "us-east-1", "cpu": 45},
    {"name": "web-02", "region": "eu-west-1", "cpu": 92},
    {"name": "db-01",  "region": "us-east-1", "cpu": 78},
    {"name": "db-02",  "region": "us-east-1", "cpu": 30},
]
#
# PART A: loop through servers and print each one like this:
#   web-01 (us-east-1): 45%
#   web-02 (eu-west-1): 92%
#   db-01 (us-east-1): 78%
#   db-02 (us-east-1): 30%
#
# Reminder: `server` already IS the row, so use server["name"].
#
# PART B: count how many servers are in each region.
#   {'us-east-1': 3, 'eu-west-1': 1}
#
# Reminder: empty dictionary, loop, pull out the region,
# then "current count (0 if new) + 1, save it back."
#
# Write your code below this line:
slist = {}
for i in servers:
    print(f"{i['name']} ({i['region']}): {i['cpu']}%")
    if i["region"] in slist:
        slist[i["region"]] += 1
    else:
        slist[i["region"]] = 1

print(slist)

