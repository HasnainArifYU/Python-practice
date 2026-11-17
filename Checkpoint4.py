# ============================================
# LESSON 4 CHECKPOINT: MINI RFC REPORT
# ============================================
# This is your work project in miniature:
# rows in -> stats -> email body.
#
changes = [
    {"number": "CHG0030001", "type": "Normal",    "state": "Closed",    "close_code": "Successful"},
    {"number": "CHG0030002", "type": "Standard",  "state": "Closed",    "close_code": "Successful"},
    {"number": "CHG0030003", "type": "Emergency", "state": "Closed",    "close_code": "Unsuccessful"},
    {"number": "CHG0030004", "type": "Normal",    "state": "Scheduled", "close_code": None},
    {"number": "CHG0030005", "type": "Normal",    "state": "Closed",    "close_code": "Successful"},
    {"number": "CHG0030006", "type": "Standard",  "state": "Implement", "close_code": None},
    {"number": "CHG0030007", "type": "Standard",  "state": "Closed",    "close_code": "Successful"},
    {"number": "CHG0030008", "type": "Normal",    "state": "Scheduled", "close_code": None},
]
#
# Build ONE string called body, then print(body) once.
#
# Expected output (exactly, including the blank line):
#   RFC Weekly Summary
#   Total changes: 8
#   Closed: 5
#   Success rate: 80.0%
#
#   By type:
#   Normal: 4
#   Standard: 3
#   Emergency: 1
#
# You need, from ONE loop over changes:
#   - how many are Closed
#   - how many Closed ones were Successful
#   - a count of each type (frequency count)
# Then build body from those numbers.
#
# Hints:
#   - Total changes is len(changes)
#   - Success rate = successful / closed * 100
#   - A blank line is just an extra "\n"
#   - You'll need a second, small loop over your
#     type counts to add the "By type" lines
#
# BONUS: make sure it doesn't crash if nothing is closed.
#
# Write your code below this line:
Body = "RFC Weekly Summary/n"
Total = 0;
Closed = 0;
Success = 0;
count = {}
for i in changes:
    Total +=1
    if i["type"] in count:
        count[i["type"]] +=1;
    else:
        count[i["type"]] = 1;
    if i["state"] == "Closed":
        Closed+=1;
    if i["close_code"] == "Successful":
        Success+=1;
Success_rate = (Success/Closed)*100
print("RFC Weekly Summary")
print("Total Change: "+str(Total))
print("Closed: "+str(Closed))
print("Success rate: "+str(Success_rate))
print("By type: ")
for key, value in count.items():
    print(f"{key}: {value}")




