from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

toaster.show_toast("Notification!","Hello There! Hope You are having a Great day", threaded=True, icon_path=None, duration=3)

while toaster.notification_active():
    time.sleep(0.1)
