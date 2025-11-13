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