import pyautogui
import time

base_url = "https://dlp.hashtagtreinamentos.com/python/intensivao"
pyautogui.PAUSE = 0.5

# abertura de navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# acesso de site
pyautogui.write(f"{base_url}/login")
pyautogui.press("enter")
time.sleep(2)

# logar na conta
pyautogui.click(x=753, y=384)
# pyautogui.write("deu certo")


print(pyautogui.position())
