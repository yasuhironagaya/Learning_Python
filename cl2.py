# クラスの定義
class Dog:
    # 初期化メソッド
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # メソッドの定義
    def bark(self):
        return f"{self.name} says woof!"

    # 他のメソッドの定義
    def get_age(self):
        return self.age

# クラスのインスタンス化
dog = Dog("Fido", 5)

# メソッドの使用
print(dog.bark())  # -> "Fido says woof!"
print(dog.get_age())  # -> 5
