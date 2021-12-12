
# 画面の表示
def display(list,y): # 配列全部と縦の個数を手に入れる
    num_list = [str(i+1) for i in range(y)]
    print('\\',num_list)
    for i in range(y): # for文で縦の個数繰り返す
        print(i+1,list[i]) # 1列表示する

# 入力のチェック
def check_type(input,limit):
    try:
        input.isdigit()
        float(input)
    except ValueError:
        return False
    else:
        return int(input)<=int(limit)