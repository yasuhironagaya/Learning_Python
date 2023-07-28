print("リストの要素を順に出力するサンプル")
my_list = [1, 2, 3, 4, 5]  # リストの作成
for item in my_list:  # リストの各要素に対してループを行う
    print(item)  # 要素を出力する

print("0から9までの数字を順に出力するサンプル")
i = 0  # 初期値の設定
while i < 10:  # iが10未満である間ループを行う
    print(i)  # iの値を出力する
    i += 1  # iの値に1を加える

print("basicのfor とは違うからね")
for i in  [0, 1, 2, 3, 4]:
    print(i)

print("listの部分はrange()でも指定可")
for i in range(10):
    print(i)

print("途中で処理を終了させる場合は、breakを使い抜け出す")
for i in range(10):
    if i == 3:
        break
    print(i)

print("continueで要素をスキップ、例では３をスキップ")
for i in range(10):
    if i == 3:
        continue
    print(i)

print("for分のネスト")
for i in range(10):
    for j in range(10):
        answer = i * j
        print(i, j, answer, sep="-")


for i in range(10):
    for j in range(10):
        answer = i * j
        print(f"{i} * {j} = {answer}")

print('for分のサンプル')

arr = [2, 4 ,6, 8, 10]
sum = 0
for i in arr:
    sum += i
print(sum)

print('while文の無限ループ。少なくとも１回は処理を行う事が出来る')

i = 200
while i < 100:
    i *= 2
    print(i)
print("Finish!!")

print('1回も実行されないので以下のように書き換えます')

i = 200
while True:
    print(i)
    i *= 2
    if i >= 100:
        break
print("Finish!!")
