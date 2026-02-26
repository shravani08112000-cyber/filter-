#......parent class.....
class car:
    def __init__(self, brand ,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def speed(self):
        print(f"{self.brand} {self.model} has a speed of 200km/h")
    def color(self):
        print(f"{self.brand} {self.model} is red")
    def fuel(self):
        print(f"{self.brand} {self.model} uses petrol")
    def seating(self):
        print(f"{self.brand} {self.model} has a seating capacity of 5")
    def cost(self):
        print(f"{self.brand} {self.model} costs $20,000")
        
    # child class
class Toyota(car):
    def __init__(self, brand, model, price, country):
        super().__init__(brand, model, price)
        self.country = country
    def country_of_origin(self):
        print(f"{self.brand} {self.model} is manufactured in {self.country}")
class Honda(car):
    def __init__(self, brand, model, price, country):
        super().__init__(brand, model, price)
        self.country = country
    def country_of_origin(self):
        print(f"{self.brand} {self.model} is manufactured in {self.country}")
class Ford(car):
    def __init__(self, brand, model, price, country):
        super().__init__(brand, model, price)
        self.country = country
    def country_of_origin(self):
        print(f"{self.brand} {self.model} is manufactured in {self.country}")
        
car1 = Toyota("Toyota", "Camry", 24000, "Japan")
car2 = Honda("Honda", "Civic", 22000, "Japan")
car3 = Ford("Ford", "Mustang", 30000, "USA")

car1.speed()
car1.color()    
car1.fuel()
car1.seating()
car1.cost()
car1.country_of_origin()
car2.speed()
car2.color()    
car2.fuel()
car2.seating()
car2.cost()
car2.country_of_origin()
car3.speed()
car3.color()
car3.fuel()
car3.seating()
car3.cost()
car3.country_of_origin()

#Tree
#...parent class....
class Tree:
    def __init__(self, name, fruit, height, age):
        self.name = name
        self.fruit = fruit
        self.height = height
        self.age = age
    def grow(self):
        print(f"{self.name} is growing taller")
    def shed_leaves(self):
        print(f"{self.name} is shedding its leaves")  
    def bear_fruit(self):
        print(f"{self.name} bears {self.fruit}")
    def age_tree(self):
        print(f"{self.name} is {self.age} years old")
    def tree_height(self):
        print(f"{self.name} is {self.height} meters tall")
  # child class
class MangoTree(Tree):
    def __init__(self, name, fruit, height, age, country):
        super().__init__(name, fruit, height, age)
        self.country = country
    def country_of_origin(self):
        print(f"{self.name} is commonly found in {self.country}")
class AppleTree(Tree):
    def __init__(self, name, fruit, height, age, country):
        super().__init__(name, fruit, height, age)
        self.country = country
    def country_of_origin(self):
        print(f"{self.name} is commonly found in {self.country}")
class OrangeTree(Tree):
    def __init__(self, name, fruit, height, age, country):
        super().__init__(name, fruit, height, age)
        self.country = country
    def country_of_origin(self):
        print(f"{self.name} is commonly found in {self.country}")
        
tree1 = MangoTree("Mango Tree", "Mangoes", 10, 5, "India")
tree2 = AppleTree("Apple Tree", "Apples", 8, 3, "USA")
tree3 = OrangeTree("Orange Tree", "Oranges", 6, 4, "Spain")
tree1.grow()
tree1.shed_leaves()
tree1.bear_fruit()
tree1.age_tree()
tree1.tree_height()
tree1.country_of_origin()
tree2.grow()
tree2.shed_leaves()
tree2.bear_fruit()
tree2.age_tree()
tree2.tree_height()
tree2.country_of_origin()
tree3.grow()
tree3.shed_leaves()
tree3.bear_fruit()
tree3.age_tree()
tree3.tree_height()
tree3.country_of_origin()