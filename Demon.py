import time
import gi
import daemon
import os

def display_notification():
	while True:
		gi.require_version('Notify', '0.7')
		from gi.repository import Notify
		Notify.init('Notification')
		message = Notify.Notification.new("Notification", "Hello!!!", "dialog-information")
		message.show()
		time.sleep(10)
		os.system( " gnome-screensaver-command -l")
		time.sleep(2400)
def run():
	with daemon.DaemonContext():
		display_notification()	

if __name__ == '__main__':
	run()
