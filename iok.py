def run(): 
  file = "main.iok"
  file = open(file, "r")
  script = file.read()
  file.close()
  
  script = script.split(" ")
  res = 0
  
  for char in script:
    if char == "i+":
      res += 1
    elif char == "i-":
      res -= 1
    elif char == "i*":
      res *= 2
    elif char == "i/":
      res //= 2
     elif char == "i--":
      res -= 2
    elif char == "i++":
      res += 2
  
  if res > 15 and res < 25:
    res = chr(res + 81)
  elif res < -15 and res > -26:
    res = "!@#$%^&*()"[-res - 16]
  elif res > 24 or res < -25:
    res = "null"
  
  print(res)
