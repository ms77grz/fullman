from my_classes import Person

person1 = Person('John')
person1.print_info()

person2 = Person('Susan')
person2.print_info()

person2._Person__age=30
print(person2._Person__age)
person2.print_info()

# print(person2.get_age())
# person2.set_age(1)
# print(person2.get_age())

print(person2.age)
person2.age = 80
person2.print_info()


