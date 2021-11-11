import random

# 初期設定
field_x = 5
field_y = 5
bombnum = 6 

field = [["■" for j in range(field_x) ] for i in range(field_y)]
bomb_field = [[0 for j in range(field_x+1) ] for i in range(field_y+1)]

# フィールド表示
def showresult():
    for i in range(field_y):
        print(field[i])

# 入力のチェック
def check_type(input):
    try:
        input.isdigit()
        float(input)
    except ValueError:
        return False
    else:
        return float(input).is_integer()

# 数字の生成
def near_bomb(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if bomb_field[x+i][y+j] != "💣": 
                bomb_field[x+i][y+j] +=1 

# 💣の確認
def check_bomb(x,y):
    if bomb_field[x-1][y-1]=="💣":
        print("ゲームオーバー")
    else:
        for i in range(-1,2):
            for j in range(-1,2):
                field[x+i][y+j]=bomb_field[x+i-1][y+j-1]
                
print("💣マインスイーパー💣")

badinput = True
while badinput:
    open_x = input("field[?][]")
    if check_type(open_x):
            badinput = False
badinput = True
while badinput:
    open_y = input("field["+open_x+"][?]")
    if check_type(open_y):
            badinput = False


# 💣と安全地帯の準備
# field[0][0]="0"

# for i in range(bombnum):
#     bomb_field[i][0] = "💣"

bomb_field[3+1][1+1]="💣"
near_bomb(3,1)
bomb_field[2+1][1+1]="💣"
near_bomb(2,1)
bomb_field[4+1][3+1]="💣"
near_bomb(4,3)

        
bomb_field[int(open_x)][int(open_y)]

bomb_field[0][0] = bomb_field[int(open_x)][int(open_y)]



showresult()









