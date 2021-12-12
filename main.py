import random
import components

field_x = 10
field_y = 10
bombs = 10
open_x = 0
open_y= 0

field_list = [['['+str(i)+']['+str(j)+']' for i in range(field_x+2)] for j in range(field_y+2)] # 配列を作成
field_show = [['■' for i in range(field_x)] for j in range(field_y)] # 配列を作成


def count_bomb(x,y):
    bomb_exist = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if (x+i)>1 and (y+j)>1 and (x+i)<field_x and (y+j)<field_y:
                print(field_list[x+i][y+j])
                if field_list[x+i][y+j] == 'bbbb':
                    bomb_exist = bomb_exist + 1
    field_list[x][y] = bomb_exist
    print("bombexist",bomb_exist)
    if bomb_exist == 0:
        field_show[x-1][y-1] = '□'
        for i in range(-1,2):
            for j in range(-1,2):
                if (x+i)>=1 and (y+j)>=1 and (x+i)<=field_x and (y+j)<=field_y:
                    if field_show[x+i-1][y+j-1] == '■':
                        count_bomb(x+i,y+j)
    else:
        field_show[x-1][y-1] = bomb_exist
    

def check_input():
    badinput = True
    while badinput:
        x = input("field[?][]")
        if components.check_type(x):
                badinput = False        
    badinput = True
    while badinput:
        y = input("field["+x+"][?]")
        if components.check_type(y):
                badinput = False
    open_x = int(x)
    open_y= int(y)
    return open_x, open_y
    
def check_bomb(open_x,open_y):
    if field_list[open_x][open_y]=='bbbb':
        print("ゲームオーバー")
    else:
        count_bomb(open_x,open_y)


print("💣マインスイーパー💣")
components.display(field_list,field_y+2)
components.display(field_show,field_y)

open_x, open_y = check_input()
# 盤面のセット
for i in range(1,field_x):
    for j in range(1,field_y):
        if bombs < 0:
            break
        field_list[i][j]= 'bbbb'
        bombs = bombs-1
        x = 1
        y = 1
        while x==1 and y==1:
            x = random.randint(1,field_x)
            y = random.randint(1,field_y)
        tmp = field_list[x][y]
        field_list[x][y]= field_list[i][j]
        field_list[i][j] = tmp
field_list[1][1] = field_list[open_x][open_y]

field_list[open_x][open_y] = '0000'

# ゲームの開始
while True:
    components.display(field_list,field_y+2)
    print(open_x)
    print(open_y)
    check_bomb(open_x,open_y)
    components.display(field_show,field_y)
    open_x, open_y = check_input()
    
    

    

