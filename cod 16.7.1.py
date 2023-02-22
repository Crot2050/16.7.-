class Cat :

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGander(self):
        return self.gender

    def getAge(self):
        return self.age

cat_1 = Cat("Barsik", ",boy", 1)
cat_2 = Cat("Masya", "girl", 0)
print(f"Имя: {cat_1.name}, Пол: {cat_1.gender}, Возраст: {cat_1.age}")
print(f"Имя: {cat_2.name}, Пол: {cat_2.gender}, Возраст: {cat_2.age}")
