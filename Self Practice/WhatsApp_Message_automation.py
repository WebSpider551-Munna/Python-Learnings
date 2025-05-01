import pyautogui as pg
import time
import random


courses = ['python', 'sql', 'powerbi', 'SSIS', 'SSRS', 'excel', 'tableau', 'R', 'java', 'c++', 'javascript', 'html', 'css', 'php', 'ruby', 'swift']

print("You have 10 seconds to open WhatsApp or any text field...")
time.sleep(10)
'''
try:
    while True:
        if keyboard.is_pressed('esc'):
            print("Script stopped by user.")
            break

        a = random.choice(courses)
        pg.write(f"learn {a} online")

        pg.press('enter')
        time.sleep(60)  # Wait 2 seconds before sending next message

except KeyboardInterrupt:
    print("Script interrupted.") '''
pg.write(f'Software Courses:\n')
for i in range(20):
    #a = random.choice(courses)
    #pg.write(f"{i}:{a}")
    pg.write(f"{i+1}:{courses[i]}")
    pg.press('enter')
    time.sleep(3)
print("All messages sent.")