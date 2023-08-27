import random

ADLUT_AGE = 20
NAME_LIST = ["田中", "山田", "佐藤", "鈴木", "高橋"]


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= ADLUT_AGE:
            print(f"{self.name}さんは{self.age}歳なので大人です。")
        else:
            print(f"{self.name}さんは{self.age}歳なので大人ではありません。")


humans = []
for name in NAME_LIST:
    humans.append(Human(name, random.randint(0, 100)))

for human in humans:
    human.check_adult()
