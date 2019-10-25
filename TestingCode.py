#crear la clase persona primero, con el metodo constructor que se define
#def __init__.... Lo que esta dentro de parentesis son los atributos que va a terner la persona
#en este caso, nombre, edad y correo(El self siempre se pone)
class Person(object):
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

  def sumarDosNumeros(self, num1,num2):
      print(num1 + num2)


#en esta parte utilizo la clase persona, y creo un objeto de tipo persona, con nombre, edad y correo
#una vez que cree la persona puedo acceder a sus atributos y los imprimo usando print
p1 = Person("Allan", 28,"allan.monge19@gmail.com")
print(p1.name)
print(p1.age)

p1.sumarDosNumeros(2,5)