import pyautogui
import pyperclip
import time


def get_msg():
    contents = "测试消息1#测试消息2#测试消息3"
    return contents.split("#")


def send(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


def send_msg(friend):
    pyautogui.hotkey('ctrl', 'alt', 'w')
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy(friend)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    for msg in get_msg():
        send(msg)
        time.sleep(2)


if __name__ == '__main__':
    friend_name = "余健"
    send_msg(friend_name)
