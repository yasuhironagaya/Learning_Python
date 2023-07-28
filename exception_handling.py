# def divide_by_two():
#     try:
#         num = int(input("整数を入力してください: "))
#         print(f"入力した数値を2で割ると: {num/2}")
#     except ValueError:
#         print("エラー: 整数を入力してください。")
#     except ZeroDivisionError:
#         print("エラー: 0では割ることはできません。")
#     except Exception as e:
#         print(f"未知のエラーが発生しました: {str(e)}")

# divide_by_two()

# ---------------------------------------------------------------------------------------

# a = 2
# b = 0

# print('start')
# print(a/b)
# print('finish')

# -----------------------------------------------------------------------------------------

# print('try except')

# a = 2
# b = 1

# try:
#     print(a/b)
# except:
#     print('0で割ってるよ！')
# else:
#     print('正しく計算出来ました！終了します')
# finally:
#     print('これでおしまいです')

# ----------------------------------------------------------------------------------------

# print('例外処理の場合分け')

# a = 2
# b = "2"

# try:
#     print(a/b)
# except:
#     print('0で割ってるよ！')

# --------------------------------------------------------------------------

# print('exceptの後にエラー名を記述して対処、エラー名は覚える必要があります')

# a = 2
# b = 0

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('0で割ってるよ！')
# except TypeError:
#     print('データ型エラーです')

# ----------------------------------------------------------------------------------

# print('エラー内容を出力')

# a = 2
# b = "0"

# try:
#     print(a/b)
# except Exception as e:
#     print(e)
# finally:
#     print('Finish')

# -----------------------------------------------------------------------------------

print('for文')
l1 = []
for i in range(5):
    l1.append(i)

print(l1)

print('リスト内包表記')
l2 = [i for i in range(5)]

print(f"l2 = [i for i in range(5)] = {l2}")

print('要素を柔軟に作成')

l3 = [i/2 for i in range(5)]

print(f"l2 = [i/2 for i in range(5)] = {l3}")



