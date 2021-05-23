def run(): 
  file = "main.iok"
  file = open(file, "r")
  script = file.read()
  file.close()
  script = script.split(" ")
  res = 0
  a = 16
  for char in script:
    if char == "i+":
      res += 1
    elif char == "i-":
      res -= 1
    elif char == "i*":
      res *= 2
    elif char == "i/":
      res /= 2
     elif char == "i--":
      res -= 2
    elif char == "i++":
      res += 2
  if res == a:
    res = "a"
  elif res == a + 1:
    res = "b"
  elif res == a + 2:
    res = "c"
  elif res == a + 3:
    res = "d"
  elif res == a + 4:
    res = "e"
  elif res == a + 5:
    res = "f"
  elif res == a + 6:
    res = "g"
  elif res == a + 7:
    res = "h"
  elif res == a + 8:
    res = "i"
  elif res >= a + 9:
    res = "null"
  elif res == ps: #special chars
    res = "!"
  elif res == ps - 1:
    res = "@"
  elif res == ps - 2:
    res = "#"
  elif res == ps - 3:
    res = "$"
  elif res == ps - 4:
    res = "%"
  elif res == ps - 5:
    res = "^"
  elif res == ps - 6:
    res = "&"
  elif res == ps - 7:
    res = "*"
  elif res == ps - 8:
    res = "("
  elif res == ps - 9:
    res = ")"
  elif res <= ps - 10:
    res = "null"
  print(res)
