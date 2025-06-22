valid = False 
n = 0 
while not valid: 
  try: 
    n = int(input("Please enter a number:")) 
    if n < 0: 
      print("Error") 
    else: 
      valid = True 
  except:  
    print("Error") 
     
x = n-1 
for row in range(n): 
  x = n-1 
  for col in range(n): 
     
    if row == x: 
      print("1 ", end=" ") 
    else: 
      print("0 ", end=" ") 
    x -= 1 
  print() 
