import pyautogui 
import time 

# Pressionando o botao do windows
pyautogui.press('win')
# escrevendo google chrome
pyautogui.write('google chrome')
# pressionando enter
pyautogui.press('enter')
# esperando 2 segundos 
time.sleep(2)
# escrevendo a url do gmail 
pyautogui.write('https://gmail.com')
# pressioando enter
pyautogui.press('enter')
# Esperando 2 segundos
time.sleep(2)
# Movendo o mouse para o campo do email 
pyautogui.moveTo(x=1302, y=342)
pyautogui.write("teste123@gmail.com")
# Movendo o mouse para o campo da senha
pyautogui.moveTo(x=1576, y=365)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(x=1455, y=392)
pyautogui.write("senhateste2000")
