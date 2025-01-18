import pyautogui as pa 
import random
import time

time.sleep(5)

mensagens = ['Oi', 'eae', 'Cade',
             'Me paga', 'faz o pix', 'bora', 'cade meu dinheiro', 'cade ??', 'me passa meu dinheiro mano', 'trava zap']

for i in range(50):
    msg = random.choice(mensagens)
    pa.write(msg)
    pa.press('enter')
