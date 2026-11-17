# ============================================
# TURNING COUNTS INTO REPORT LINES
# ============================================
#
# Last time you built a counts dictionary like this one.
# Now we print it as readable lines instead of a raw {...}.
#
# Reminder: .items() gives you the key AND the value:
#
#   for key, value in some_dict.items():
#       print(f"{key}: {value}")
#
# --------------------------------------------
# YOUR TASK
# --------------------------------------------
type_counts = {"Normal": 3, "Standard": 2, "Emergency": 1}
#
# Print this exactly:
#   RFC Summary
#   Normal: 3
#   Standard: 2
#   Emergency: 1
#   Total: 6
#
# Hints:
#   - "RFC Summary" prints once, BEFORE the loop
#   - the total: add up the values while you loop
#     (same idea as your response-time total)
#   - "Total" prints once, AFTER the loop
#
# Write your code below this line:
print("RFC Summary")
Total = 0;
for key, value in type_counts.items():
    print(f"{key}: {value}")
    Total += value
print(f"Total: {Total}")