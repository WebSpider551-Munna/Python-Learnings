import pyautogui as pg
import webbrowser
import time
import os
import argparse
from datetime import datetime

# WAutoBot🤖 - WhatsApp Visual Automation Bot

def log(msg):
    with open("message_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")
    print(msg)

def load_messages(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_schedule(filepath):
    schedule = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if '-' in line:
                time_part, msg = line.strip().split(' - ', 1)
                try:
                    dt = datetime.strptime(time_part.strip(), "%Y-%m-%d %H:%M")
                    schedule.append((dt, msg.strip()))
                except ValueError:
                    log(f"Invalid datetime format: {line.strip()}")
    return schedule

def wait_for_image(image_path, description="", timeout=30, confidence=0.8):
    for _ in range(timeout):
        pos = pg.locateCenterOnScreen(image_path, confidence=confidence)
        if pos:
            log(f"{description} found.")
            return pos
        time.sleep(1)
    log(f"{description} not found within timeout.")
    return None

def click_image(image_path, description="", confidence=0.8):
    pos = wait_for_image(image_path, description, confidence=confidence)
    if pos:
        pg.click(pos)
        return True
    return False

def open_whatsapp(search_img):
    log("Opening WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com/")
    if not wait_for_image(search_img, "Search box", timeout=60):
        log("Failed to open WhatsApp. Exiting.")
        exit()

def select_contact(contact_name, search_img):
    if click_image(search_img, "Search box"):
        time.sleep(1)
        pg.write(contact_name)
        time.sleep(2)
        pg.press("enter")
        log(f"Opened chat with {contact_name}")
        return True
    return False

def send_message(text, send_img):
    pg.write(text)
    time.sleep(0.5)
    if click_image(send_img, "Send button"):
        log(f"Sent message: {text}")
    else:
        log("Send button not found — message may not have been sent.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WAutoBot🤖")
    parser.add_argument("--contact", required=True)
    parser.add_argument("--messages", required=True)
    parser.add_argument("--schedule", required=True)
    parser.add_argument("--search", required=True)
    parser.add_argument("--send", required=True)
    args = parser.parse_args()

    contact_name = args.contact
    messages_file = args.messages
    schedule_file = args.schedule
    search_img = args.search
    send_img = args.send

    messages = load_messages(messages_file)
    schedule = load_schedule(schedule_file)

    open_whatsapp(search_img)

    while schedule:
        now = datetime.now().replace(second=0, microsecond=0)
        for sched in schedule[:]:
            dt, msg = sched
            if now == dt:
                log(f"Scheduled time matched: {dt}")
                if select_contact(contact_name, search_img):
                    send_message(msg, send_img)
                    schedule.remove(sched)
                time.sleep(2)
        time.sleep(30)

    log("✅ All scheduled messages sent.")