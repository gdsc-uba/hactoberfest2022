def can_segment_string(s, dictionary):
  for i in range(1, len(s) + 1):
    first = s[0:i]
    if first in dictionary:
      second = s[i:]
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False
  
s = "hellonow";
dictionary= set(["hello","hell","on","now"])
if can_segment_string(s, dictionary):
  print("String Can be Segmented")
else:
  print("String Can NOT be Segmented")
