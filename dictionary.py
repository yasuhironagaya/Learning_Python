# 辞書の作成
dictionary = {"apple": "red", "banana": "yellow", "cherry": "red"}

# 値の取得
apple_color = dictionary["apple"]
print(f"The color of an apple is {apple_color}.")

# 値の更新
dictionary["apple"] = "green"
print(f"After ripening, the color of an apple is {dictionary['apple']}.")

# 新たなキーと値の追加
dictionary["grape"] = "purple"
print(f"We have added a grape with color {dictionary['grape']}.")

# キーと値の削除
del dictionary["cherry"]
print(f"After removing cherry, we have {dictionary}.")
