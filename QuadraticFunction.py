import math


class QuadraticFunction:
  def __init__(self, a, b, c, xs, ys):
    self.a = float(input("coefficient a: "))
    while (self.a==0):
      print("Coefficient can not equal 0")
      self.a = float(input("coefficient a: "))
    self.b = float(input("coefficient b: "))
    self.c = float(input("coefficient c: "))
    self.xs = -(self.b/(2*self.a))
    self.ys = ((4 * self.a * self.c - pow(self.b,2)) / (4*self.a))
    
    
    
  def vertex(self):
    print("S("+str(self.xs)+"|"+str(self.ys)+")")
    print("y = " + str(self.a) + "(x -(" + str(self.xs) + "))^2 + (" + str(self.ys) + ")")
    print("Press entry to continue")
    

  def find_y(self):
    x = float(input("Coordinate x: "))
    y = self.a * pow((x),2) + (self.b*x) + (self.c)
    print("y exact: " + str(y))
    y = round(y,2)
    print("y rounded: " + str(y))
    print("the y coordinate equal: "+str(y))
    print("Press entry to continue")
  

  def PonParabel(self):
    x_input = float(input("Coordinate x: "))
    y_input = float(input("Coordinate y: "))
    x_output = (self.a * (x_input - self.xs) * (x_input - self.xs)) + self.ys
    rx_output = round(x_output, 10)
    if (y_input == rx_output): 
      print("True -> The point is on the Parabola")
      print("Because "+str(y_input)+" = "+str(x_output))
    else: 
      print("False - > The point is not on the Parabola")
      print("Because "+str(y_input)+" != "+str(x_output))
    print("Press entry to continue")
    
    

  def zero(self):
    D = pow(self.b, 2) - 4 * self.a * self.c
    if(D>0): 
      nL = (-self.b - math.sqrt(D))/(2*self.a)
      pL = (-self.b + math.sqrt(D))/(2*self.a)
      print ("Have two solution")
      print ("L = {"+str(nL)+"; "+str(pL)+"}")
    elif(D==0): 
      pL = (-self.b + math.sqrt(D))/(2*self.a)
      print ("Have one solution")
      print ("L = {"+str(pL)+"}")
    else: 
      print ("Solution do not exist")
      print ("L = {"+"}")
    print("Press entry to continue")
    
    

  def describeFunction(self):
    print("The Graph is a: ")
    if (self.a>1 or self.a<-1): print("stretched Parabola")
    else: print("hosed Parabola")
    if (self.a>0): print("which opens upwards")
    else: print("which opens downwards")
    print("and the Parabola is moved "+str(self.xs)+" units along the x-axis\nand "+str(self.ys)+" units along the y-axis")
    print("Press entry to continue")
    
    

  def menu(self):
    print ("\n\nMain Menu - Current Equation:  y = ("+str(self.a)+")*x^2 + ("+str(self.b)+")*x + ("+str(self.c)+")")
    print ("==============================")
    print ("1. The vertex of Parabola")
    print ("2. Find the Y-Coordinate")
    print ("3. Point on Parabola")
    print ("4. Find the Zero-Coordinates")
    print ("5. Describe the Parabola")
    print ("0. Change the Equation")
    print ("Press -1 to exit")
    print ("-----------------------------")
    choice = float(input("Select: "))
    
    if choice == 0.0:
      self.__init__
      self = QuadraticFunction(0,0,0,0,0)
      self.menu()

    if choice == 1.0:
      self.vertex()
      self.menu()
      
    if choice == 2.0: 
      self.find_y()
      self.menu()
      
    if choice == 3.0:
      self.PonParabel()
      self.menu()
      
    if choice == 4.0:
      self.zero()
      self.menu()

    if choice == 5.0:
      self.describeFunction()
      self.menu()


class LinearFunction:
  def __init__(self, m, t):
    self.m = m
    self.t = t
  def menu(self):
    pass


class Poly3rd:
  def __init__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
  def menu(self):
    pass

#######################################################################

select = int(input("Select you Polynom Degree:"))
if select == 1: 
  print("\nInitialize your Linear:")
  print("==========================")
  liner = LinearFunction(0,0)
  liner.menu()

if select == 2:
  print("\nInitialize your Parabole:") 
  print("==========================")
  quadra = QuadraticFunction(0,0,0,0,0)
  quadra.menu()

if select == 3:
  print("\nInitialize your Polynom of 3rd Degree")
  print("===========================")
  poly3rd = Poly3rd(0,0,0,0)
  poly3rd.menu()




#Layt
