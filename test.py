def compact(lst):
    return list(filter(lambda x: x, lst))
  
  
print(compact([0, 1, False, 2, '', 3, 'a', 's', 34])) # [ 1, 2, 3, 'a', 's', 34 ]