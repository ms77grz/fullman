class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name

a = A()
b = A()

print(a.property1)
print(a.say_hi())
print(a.say_hi('John'))