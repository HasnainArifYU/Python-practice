# ============================================
# LESSON 5: TUPLES
# ============================================
#
# A tuple is like a list, but with round brackets,
# and it CAN'T be changed after it's created.
#
#   row = ("CHG0030001", "Normal", "Closed")
#
# Get items by index, like a list:
#   row[0]    ->  CHG0030001
#
# Trying to change one crashes:
#   row[0] = "x"
#   ->  TypeError: 'tuple' object does not support item assignment
#
# UNPACKING: split a tuple into separate variables in one line.
# The number of variables must match the number of items.
#
#   number, change_type, state = row
#   print(change_type)    ->  Normal
#
# You can unpack right in a for loop. (This is what
# "for key, value in d.items()" has been doing all along.)
#
#   for number, change_type, state in rows:
#       print(number)
#
# --------------------------------------------
# YOUR TASK
# --------------------------------------------
# This is how rows come back from Oracle: a list of tuples.
# The columns are (number, type, state), in that order.
rows = [
    ("CHG0030001", "Normal", "Closed"),
    ("CHG0030002", "Standard", "Closed"),
    ("CHG0030003", "Emergency", "Scheduled"),
    ("CHG0030004", "Normal", "Closed"),
]
#
# Loop through rows, unpacking each one in the for line.
# Print the Closed changes, then a count at the end.
#
# Expected output (exactly):
#   CHG0030001 (Normal)
#   CHG0030002 (Standard)
#   CHG0030004 (Normal)
#   Closed: 3 of 4
#
# Write your code below this line:
closed = 0;
total = 0;
for i in rows:
    total+=1;
    if i[2]=="Closed":
        print(i[0]+" ("+i[1]+")")
        closed+=1
print("Closed: "+str(closed)+" of "+str(total))
   