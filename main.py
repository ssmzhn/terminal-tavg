from play import display, select, display_mode, load_config
import os
import yaml
"""
display_mode = Enum('display_mode',('INFO','INPUT','ERROR'))
def display(text: str,mode: Enum=display_mode.INFO,end='\n'):
    if mode == display_mode.INFO:
        print('\033[0m',end='')
    elif mode == display_mode.INPUT:
        print('\033[0;33m',end='')
    elif mode == display_mode.ERROR:
        print('\033[0;31m',end='')
    for x in text:
        print(x,end='',flush=True)
        sleep(0.025)
    print('\033[0m',end=end)
"""
def select_list(ls:tuple) -> tuple:
    for index,element in enumerate(ls):
        print(index+1,element)
    select_num = input('Please select: ')
    while True:
        if select_num.isdigit() and 0<int(select_num)<=len(ls):
            return int(select_num)-1,ls[int(select_num)-1]
        else:
            select_num = input('Illegal input! Try again: ')
"""
def select(select_dict:dict,tip:str='') -> str:
    
    此处的 select_dict 为一个字典，格式如下
    {
        输入字符: 提示语
    }
    例：
    {
        'A': 'Abort'
        'R': 'Retry'
        'F': 'Fail'
    }
    注意：输入字符必须大写！
    
    if tip != '':
        display(tip,mode=display_mode.INPUT)
    for x,y in select_dict.items():
        display('Press '+x.upper()+' to '+y,mode=display_mode.INPUT)
    display('Please input: ',mode=display_mode.INPUT,end='')
    while True:
        ch = getch()
        print()
        if not ch.upper() in select_dict.keys():
            display('Illegal Input! Try again: ',mode=display_mode.INPUT,end='')
        else:
            return ch
"""
def main():
    display('Welcome to use Terminal TAVG Game!')
    display('Please select an item:')
    game_list = []
    for x in os.listdir('games'):
        if os.path.isdir('games/'+x):
            game_list.append(x)
    game_name = select_list(tuple(game_list))[1]
    load_config('games/'+game_name)

if __name__ == '__main__':
    main()
