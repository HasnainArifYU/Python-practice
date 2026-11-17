# ============================================
# BUILDING THE EMAIL BODY AS ONE STRING
# ============================================
#
#   msg = "Hello"
#   msg += " world"        ->  msg is now "Hello world"
#
#   "\n" means new line:
#   print("line one\nline two")
#   ->  line one
#       line two
#
# --------------------------------------------
# YOUR TASK
# --------------------------------------------
type_counts = {"Normal": 3, "Standard": 2, "Emergency": 1}
#
# Same report as before, but DON'T print inside the loop.
# Instead, build everything into ONE variable called body,
# then print(body) once at the very end.
#
# Start with:   body = "RFC Summary\n"
# In the loop:  add one line per type to body (end each with \n)
# After loop:   add the Total line to body
#
# Expected output (same as before):
#   RFC Summary
#   Normal: 3
#   Standard: 2
#   Emergency: 1
#   Total: 6
#
# Write your code below this line:

body = ("RFC Summary\n")
Total = 0;
for key, value in type_counts.items():
    body += key+": "+str(value)+"\n"
    Total += value
body += "Total :"+str(Total)
print(body)