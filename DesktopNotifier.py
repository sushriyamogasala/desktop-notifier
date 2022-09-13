import time

from plyer import notification

if __name__ == "__main__":

    while True:

        notification.notify(

            title = " 💝 HONEY 💝 !!!",

            message = "Time for break😘!!Drink some water🐼 !! It has been half-an-hour⏱️⏲️ !!",

            app_icon='desktop notifier icon.ico',

            app_name='With Love 🐼',

            timeout = 30
        )

        time.sleep(1800)                                