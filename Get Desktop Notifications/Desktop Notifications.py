from email import message
import imp


import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Alert!!!",
            message = "Take a break, it has been an hour!",
            timeout = 50
        )
        time.sleep(3600)