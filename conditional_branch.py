# 変数aを定義し、値を10に設定します。
a = 10

# if文は条件が真(True)の場合にブロック内のコードを実行します。
# ここではaが10より大きいかどうかを判断しています。
if a > 10:
    print("a is greater than 10.")
# elif文は前のif文またはelif文の条件が偽(False)である場合に、新たな条件を提供します。
# ここではaが10と等しいかどうかを判断しています。
elif a == 10:
    print("a is equal to 10.")
# else文は全てのif文とelif文の条件が偽(False)である場合に、
# ブロック内のコードを実行します。明示的な条件は必要ありません。
else:
    print("a is less than 10.")

# if文

number = 24

if number % 2 == 0 and number % 3 == 0:
    print("６の倍数です")
elif number % 2 == 0 and number % 3 != 0:
    print("２の倍数です")
elif number % 2 != 0 and number % 3 == 0:
    print("３の倍数です")
else:
    print("２と３の倍数ではありません")

# match文

fruit = "ora"

match fruit:
    case "apple":
        print('リンゴ')
    case "orange":
        print('ミカン')
    case "grape":
        print('ブドウ')
    case "peach":
        print('モモ')
    case _:
        print('その他の果物')

# 三項演算子

age = 18

if age >= 20:
    print('adult')
else:
    print('child')

age = 18

print("adult" if age >= 20 else "child")
