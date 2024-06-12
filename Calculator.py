# working



def f(x):
  return (x**2)  # change this function to whatever you want, applies to all other functions

def fact(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

def compute_e():
  sum = 1
  for i in range(1, 1000):
    sum += 1/fact(i)
  return sum
  
e = compute_e()

def sqrt(x):
  return x ** 0.5

def e_to_x(x):
  return e ** x


def atan(x):
  if abs(x) <= 1:
    Sum=0
    for n in range(0,100):
      Sum += ((-1)**n) * x**(2*n+1) / (2*n+1)
    return Sum
  else:
    def arctan(x):
      TrigList = []
      a = 1 
      for n in range(0,10000):
          m = 2 * n + 1  
          p = a * (x**m) / m  
          TrigList.append(p)
          a *= -1 
      Sum = sum(TrigList)
      return Sum
    return pi/2 - arctan(1/x)
 

    
 
  



def acos(x):
    if x == -1:  
        return pi
    elif x >= -1 and x <= 1: 
      if x == 1:  
        result = 0
      else:
        result = pi / 2 - atan(x / (1 - x**2) ** 0.5)
    else:
        result = float('nan')  
    return result

print(acos(3))



def asin(x):
    result = pi/2 - acos(x)
    return result

pi = (4*atan(0.2) - atan(1/239)) * 4

def ln(x):
  Freak = []
  a = 1
  x = x - 1
  for n in range(100000):
    m = n + 1
    p = a * (x**m) / m  
    Freak.append(p)
    a *= -1 
  SumFreak = sum(Freak)
  return SumFreak

def Ln(x):  #use this one for calculations
  if x <= 0:
      return float('nan')
  elif x == 1:
      return 0
  elif x < 2:
      return ln(x)
  else:
      m = 0
      while x >= 2:
          x = x / 2
          m = m + 1
      return ln(x) + m * ln(2)

def log(base, result):
  return Ln(result) / Ln(base)

def sin(x):
  sum = 0
  a = x % (2*pi) 
  for n in range(0, 100):
    sum += ( ((-1)**n) / fact(2*n+1)) * a**(2*n+1)
  if abs(sum) < 10**-5:
    return 0
  return sum

def cos(x):
  sum = 0
  a = x % (2*pi) 
  for n in range(0, 100):
    sum += ( ((-1)**n) / fact(2*n)) * a**(2*n)
    if abs(sum) < 10**-5:
      return 0
  return sum

def tan(x):
  if cos(x) < 0.00000000000001:
    pass
  else:
    return sin(x)/cos(x)


def first_function(x):
  return 2 * x - 2

def second_function(x):
  return 3 * x


def find_intersection(func1, func2):
  intersections = []
  for x in range(-1000, 1000):
      if func1(x) == func2(x):
          intersections.append((x, func1(x)))
  return intersections


def print_intersects():
  intersections = find_intersection(first_function, second_function)
  if intersections:
    print("Intersection points:")
    for point in intersections:
        print(point)
  else:
    print("No intersection points found.")



##      calculus operations     ##
def derivative(x):
  h = 10**-7
  result = (f(x + h) - f(x)) / h
  return result

def integral(a, b, n):
  dx = (b - a) / n
  sum = 0
  for i in range(n):
    x = a + i*dx
    sum += f(x) * dx  
  return sum


def euler_method(x0, y0, x_end, step_size):
    x = x0
    y = y0
    results = []

    while x < x_end:
        results.append((x, y))
        y += step_size * derivative(x)
        x += step_size

    results.append((x, y))  
    return results

x0 = 0
y0 = f(x0)
x_end = 2 #Final X Value
step_size = 0.1







 # print(integral(0,3,100000))
# work in progress

#returns the zero closest to the initial guess
def zero(initial_guess):
  tolerance = 0.0000000001
  for i in range(1,1000):
    df_x = derivative(initial_guess)
    if df_x == 0:
      print("cannot compute with 0 derivative")
    adjustment = initial_guess - f(initial_guess)/df_x
    if abs(adjustment - initial_guess) < tolerance:
      return adjustment
    initial_guess = adjustment
      

  
#print(ln(.5))










  

# test cases
  
#print(sin(1)) # = 0.84147
#print(sin(-300))  # = 0.9997
#print(sin(1000000)) # = -0.34999
#print(cos(1)) # = 0.5403
#print(cos(-300))  # = -0.0220966
#print(cos(1000000)) # = 0.93675

#print(tan(1)) # = 1.55740772465
#print(tan(pi/2)) # = none
#print(tan(1000000)) # = -0.37362445398
#print(atan(2)) # = 1.10714872
#print(atan(6)) # = 1.40564765
#print(atan(1000000)) # = 1.57079533

#print(asin(.5)) # = 0.523598776
#print(asin(-.67)) # = -0.734208787
#print(asin(1000000)) # = nan

#print(acos(.5)) # = 1.04719755
#print(acos(-.67)) # = 2.30500511
#print(acos(1000000)) # = nan

#print(Ln(.5)) #= -.693147
#print(Ln(2)) #= .693147
#print(Ln(1000000)) #= 13.81551056
#print(log(3, 100)) # = 4.19180

#print(derivative(4)) # f(x) = x**2, f'(x) = 2x, result should = 8

#print(pi)



#---------- user interface ----------#
def Driver():
  actions = ["sqrt","sin","cos","tan","e^x","ln","log","asin","acos","atan","deriv","integral","euler","zero"]
  for func in actions:
    print(func)
  action = input("Select action: ") 
  if action == "sqrt":            
   x = float(input("x value: "))
   print(sqrt(x))
  if action == "sin":             
     x = float(input("x value: "))
     print(sin(x))
  if action == "cos":              
     x = float(input("x value: "))
     print(cos(x))
  if action == "tan":              
     x = float(input("x value: "))
     print(tan(x))
  if action == "e^x":              
     x = float(input("x value: "))
     print(e_to_x(x))
  if action == "ln":              
     x = float(input("x value: "))
     print(Ln(x))
  if action == "log":
    b = float(input("base: "))
    a = float(input("argument: "))
    print(log(b, a))
  if action == "asin":              
     x = float(input("x value: "))
     print(asin(x))
  if action == "acos":              
     x = float(input("x value: "))
     print(acos(x))
  if action == "atan":              
     x = float(input("x value: "))
     print(atan(x))
  if action == "deriv":
    x = float(input("x value: "))
    print(derivative(x))
  if action == "integral":
    a = float(input("upper bound: "))
    b = float(input("lower bound: "))
    n = int(input("iterations (the more iterations the more accurate, but too high will mess up the function so find a sweet spot): "))
    print(integral(b, a, n))
  if action == "euler":
    x0 = float(input("initial x: "))
    y0 = float(input("initial y: "))
    x_end = float(input("terminating x: "))
    step = float(input("step size: "))
    print(euler_method(x0, y0, x_end, step))
  if action == "zero":
    x = float(input("initial guess: "))
    print(zero(x))
  if action not in actions:
    print("\nnot a valid action\n \ntry again: \n")
    Driver()
      
    


Driver()
#print((f(41)-4)/41)

#print(0.3 - 0.758)
#print(-.458 * 0.1)
#print(f(0.4835177))

#print(f(10))

#print(pi)
