import time



from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
        title="Please Drink Water Now",
        message="You have to drink one glass of water",
        # app_icon="C:\Users\vaibh\Downloads\Iconsmind-Outline-Glass-Water.ico",
        app_icon="Iconsmind-Outline-Glass-Water.ico",
        timeout=10
        )
    time.sleep(60*60)

