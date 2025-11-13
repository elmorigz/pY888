def is_it_pos_or_neg():
   for i in [1,2,-6,-8]:
      if i>=0:
          print("[{}] is Positive number".format(i))
      else:
          print("[{}] is negative number".format(i))
   else:
      print("No numbers to check")
# Calling the above-created function
is_it_pos_or_neg()
# Output:
# [1] is Positive number    
# [2] is Positive number
# [-6] is negative number
# [-8] is negative number
# No numbers to check\
PendingDeprecationWarning: The 'warn' method is deprecated and will be removed in future versions. Use 'warnings.warn' instead.