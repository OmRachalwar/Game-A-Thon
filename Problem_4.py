def caught_speeding(speed, is_birthday):
  
  if  is_birthday and speed<=65:
    return 0
  
  elif is_birthday and 65<speed<=85:
    return 1
  
  elif speed<=60:
    return 0
  
  elif 60<speed<=80:
    return 1
  
  else:
    return 2
