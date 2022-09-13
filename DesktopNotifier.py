import time

from plyer import notification

if __name__ == "__main__":

    while True:

        notification.notify(

            title = " 💝 HONEY 💝 !!!", #Displays the title of the notification.

            message = "Time for break😘!!Drink some water🐼 !! It has been half-an-hour⏱️⏲️ !!",#Accepts message description of the notification.

            app_icon='desktop notifier icon.ico',#Displays the icon for the notification.

            app_name='With Love 🐼',#displays name of the app launching this notification

            ticker = "some text", # It will display the text provided in the status bar when a notification arrives.

            toast = "False", #This will display a toast message in Android instead of a full notification

            timeout = 30 #Provides how much time in seconds the notification is to be displayed.
        )

        time.sleep(1800) 
#NOTES:toast and ticker parameters can only be used on android devices they won't work on desktop                               