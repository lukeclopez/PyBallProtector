from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from win10toast import ToastNotifier
from datetime import datetime

interval = (20 * 60)
duration = 5
message_title = "Eye Break!"
message_body = "Look at something 20 feet away for 20 seconds."


class Status:
    is_running = False


def notify_for_break():
    toaster.show_toast(message_title, message_body, duration=duration, icon_path="icon.ico")
    print('Toasted at %s' % datetime.now())


toaster = ToastNotifier()
scheduler = BackgroundScheduler()
scheduler.add_job(notify_for_break, IntervalTrigger(seconds=interval))


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
