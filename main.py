from pyscript import document, display

"""class car:
    def __init__(self, brand, color, model, type):
        self.brand = brand
        self.color = color
        self.model=model
        self.type=type
    def honk(self):
        display(f'Beep '*3, target='out')

car1=car('Koenigsegg', 'Dark green', 'Agera', 'hyper')
car2=car('Mitsubishi', 'Dark red', 'Montero', 'SUV')
car2.honk()
display(f'Dream car is a {car1.brand} {car1.model} colored {car1.color}', target='out')
display(f'Previous car was a {car2.brand} {car2.model} colored {car2.color}', target='out')

class lexus(car):
    pass
car1=lexus('lexus', 'gray', 'LM', 'Van')
car1.honk()
display(f'Law\'s car is a {car1.brand}. The color is {car1.color}', target='out')"""

def dog(s):
    class Dog:
        def __init__(self, name, age, color, breed):
            self.name = name
            self.age=age
            self.color=color
            self.breed=breed
        def bark(self):
            display(f'Bark! '*5, target='out')
    n3=document.getElementById('name').value
    a3=document.getElementById('age').value
    c3=document.getElementById('color').value
    b3=document.getElementById('breed').value
    dog1=Dog('Luna', 1, 'Black', 'German shepard')
    dog2=Dog('Ollie', 7, 'White', 'Maltese shih tzu')
    dog3=Dog({n3}, {a3}, {c3}, {b3})
    dog4=Dog('Bella', 7, 'Cream', 'Chow chow')
    dog5=Dog('Kulet', 4, 'Black & White', 'Siberian husky')
    dog3.bark
    display(f'The dog daycare consists of a: {dog1.breed}, {dog1.name}; {dog2.breed}, {dog2.name}; {dog3.breed}, {dog3.name}; {dog4.breed}, {dog4.name}; {dog5.breed}, {dog5.name}.', target='out')
#GH_ICT10_PA2_4thQtr_Dolor