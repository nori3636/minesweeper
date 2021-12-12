
# 画面の表示
def display(list,y): # 配列全部と縦の個数を手に入れる
    print("Fieldの表示")
    for i in range(y): # for文で縦の個数繰り返す
        print(list[i]) # 1列表示する

# 入力のチェック
def check_type(input):
    try:
        input.isdigit()
        float(input)
    except ValueError:
        return False
    else:
        return True