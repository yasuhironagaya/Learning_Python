# 1. 集合の作成と要素の追加
my_set = {1, 2, 3}
print("Initial set: ", my_set)

# 要素の追加
my_set.add(4)
print("Set after adding an element: ", my_set)

# 2. 集合から要素の削除
my_set.remove(1)
print("Set after removing an element: ", my_set)

# 3. 集合の間の操作
my_other_set = {3, 4, 5, 6}

# 和集合 (union)
print("Union: ", my_set.union(my_other_set))

# 積集合 (intersection)
print("Intersection: ", my_set.intersection(my_other_set))

# 差集合 (difference)
print("Difference: ", my_set.difference(my_other_set))

# 4. 集合の要素の存在確認
print("Is 2 in the set? ", 2 in my_set)

# 5. 集合の要素数の取得
print("Size of set: ", len(my_set))
