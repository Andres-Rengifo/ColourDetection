import pyautogui as pag 

pag.FAILSAFE = True

def get_position (x, y):
    try:
       pag.moveTo(x, y)
    except OSError as e:
        raise Exception(e)
    
get_position(200, 300)