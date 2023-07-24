# ショッピングリストを作成する関数
def create_shopping_list():
    return []  # 新しい空のリストを返す

# アイテムをショッピングリストに追加する関数
def add_item(shopping_list, item):
    shopping_list.append(item)  # リストの末尾にアイテムを追加

# アイテムをショッピングリストから削除する関数
def remove_item(shopping_list, item):
    if item in shopping_list:  # アイテムがリストに存在する場合
        shopping_list.remove(item)  # リストからアイテムを削除

# ショッピングリストを表示する関数
def view_shopping_list(shopping_list):
    for item in shopping_list:  # リスト内の各アイテムについて
        print(item)  # アイテムを表示

# ショッピングリストアプリを制御する関数
def shopping_list_app():
    shopping_list = create_shopping_list()  # 新しいショッピングリストを作成
    while True:  # 無限ループ
        print("\nWhat would you like to do?")
        print("1. Add item to shopping list.")
        print("2. Remove item from shopping_list.")
        print("3. View shopping list.")
        print("4. Quit.")
        option = input("Choose an option: ")  # ユーザーにオプションを選択させる
        if option == "1":  # アイテムを追加する場合
            item = input("Enter an item to add: ")  # 追加するアイテムをユーザーに入力させる
            add_item(shopping_list, item)  # アイテムをリストに追加
        elif option == "2":  # アイテムを削除する場合
            item = input("Enter an item to remove: ")  # 削除するアイテムをユーザーに入力させる
            remove_item(shopping_list, item)  # アイテムをリストから削除
        elif option == "3":  # リストを表示する場合
            view_shopping_list(shopping_list)  # リストを表示
        elif option == "4":  # プログラムを終了する場合
            break  # ループを終了（プログラムを終了）
        else:  # ユーザーが無効なオプションを選択した場合
            print("Invalid option. Please try again.")  # エラーメッセージを表示

# アプリを起動
shopping_list_app()

