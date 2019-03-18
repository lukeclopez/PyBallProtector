from apscheduler.schedulers.background import BlockingScheduler
from win10toast import ToastNotifier
from datetime import datetime
import os


def notify_for_break():
    toaster.show_toast("Eye Break!", "Look at something 20 feet away for 20 seconds.", duration=5)
    print('Toasted at %s' % datetime.now())


if __name__ == '__main__':
    toaster = ToastNotifier()
    scheduler = BlockingScheduler()
    scheduler.add_job(notify_for_break, 'interval', seconds=(20 * 60))

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
