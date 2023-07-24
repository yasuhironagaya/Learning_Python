# 1. タプルの作成とアクセス
tup1 = (1, 2, 3, 4)
print("タプル1: ", tup1)
print("タプル1の最初の要素: ", tup1[0])
print("タプル1の最後の要素: ", tup1[-1])

# 2. タプルのイテレーション
print("タプル1のイテレーション:")
for item in tup1:
    print(item)

# 3. タプルの結合
tup2 = (5, 6, 7, 8)
tup3 = tup1 + tup2
print("タプル3: ", tup3)

# 4. タプルのアンパック
a, b, c, d = tup1
print("タプル1のアンパック: ", a, b, c, d)
