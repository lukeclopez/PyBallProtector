from apscheduler.schedulers.background import BlockingScheduler
from win10toast import ToastNotifier
from datetime import datetime
import os

interval = (20 * 60)
message_title = "Eye Break!"
message_body = "Look at something 20 feet away for 20 seconds."


def notify_for_break():
    toaster.show_toast(message_title, message_body, duration=5)
    print('Toasted at %s' % datetime.now())


toaster = ToastNotifier()
scheduler = BlockingScheduler()
scheduler.add_job(notify_for_break, 'interval', seconds=interval)


def enable():
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


def disable():
    scheduler.shutdown()
