# Looping through some numbers... are they grades? Maybe?
grades = [85, 92, 78, 99, 65]
for score in grades:
  # High numbers = good? 
  if score >= 90:
    print(score, "is an A. pass")
  # Maybe lower numbers are okay? 
  elif score >= 80:
    print(score, "is a B.")
