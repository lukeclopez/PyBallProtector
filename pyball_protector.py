from apscheduler.schedulers.background import BackgroundScheduler
from win10toast import ToastNotifier
from datetime import datetime
import os

interval = 6
message_title = "Eye Break!"
message_body = "Look at something 20 feet away for 20 seconds."


class Status:
    is_running = False


def notify_for_break():
    toaster.show_toast(message_title, message_body, duration=5)
    print('Toasted at %s' % datetime.now())


toaster = ToastNotifier()
scheduler = BackgroundScheduler()
scheduler.add_job(notify_for_break, 'interval', seconds=interval)


def enable():
    Status.is_running = True
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


def disable():
    Status.is_running = False
    scheduler.shutdown(wait=False)


def toggle():
    if Status.is_running:
        disable()
    else:
        enable()
