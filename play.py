from getch import getch
from time import sleep
from enum import Enum
import yaml
import os

from yaml.constructor import sys
display_mode = Enum('display_mode',('INFO','INPUT','ERROR','DIALOGUE'))
def display(text: str,mode: Enum=display_mode.INFO,end='\n'):
    if mode == display_mode.INFO:
        print('\033[0m',end='')
    elif mode == display_mode.INPUT:
        print('\033[0;33m',end='')
    elif mode == display_mode.ERROR:
        print('\033[0;31m',end='')
    elif mode == display_mode.DIALOGUE:
        print('\033[0;32m',end='')
    for x in text:
        print(x,end='',flush=True)
        sleep(0.025)
    print('\033[0m',end=end)
def select(select_dict:dict,tip:str='') -> str:
    """
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
    """
    if tip != '':
        display(tip,mode=display_mode.INPUT)
    for x,y in select_dict.items():
        display(x.upper()+': '+y,mode=display_mode.INPUT)
    display('Please input: ',mode=display_mode.INPUT,end='')
    while True:
        ch = getch()
        print()
        if not ch.upper() in select_dict.keys():
            display('Illegal Input! Try again: ',mode=display_mode.INPUT,end='')
        else:
            return ch.upper()

def load_gamefile(path:str): 
    gamefile = yaml.load(open(path),Loader=yaml.FullLoader)
    current_step = gamefile['start']
    while True:
        step = gamefile[current_step]
        for x in step['text']:
            display(step['subject']+': '+x,mode=display_mode.DIALOGUE)
        if step['type'] == 'dialogue':
            ch = select({'N':'Next','Q':'Quit'})
            if ch == 'N':
                current_step = step['next']
            elif ch == 'Q':
                return
        elif step['type'] == 'branch':
            branches = step['branches'] # 一个字典

            tmp_dict = {} # 用于select的调用
            for i,j in branches.items():
                tmp_dict[i]=j['text']
            tmp_dict['Q'] = 'Quit'
            ch = select(tmp_dict)
            if ch != 'Q':
                current_step=step['branches'][ch]['next']
 
        if current_step == 'done':
            break
def load_config(path:str):
    if not os.path.exists(path+'/config.yml'):
        raise FileNotFoundError('No config.yml found in '+path)
    config = yaml.load(open(path+'/config.yml'),Loader=yaml.FullLoader)
    display(config['name'])
    display('Author: '+config['author'])
    display('Description: '+config['description'])

    chapters = config['chapters']
    for x in chapters:
        load_gamefile(path+'/'+x+'.yml')
