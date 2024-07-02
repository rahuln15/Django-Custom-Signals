from django.dispatch import Signal , receiver

# creating signal
notification = Signal()

# Reciever Function
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")


# this will be use when we want user see any msg when he will log in his account or dashboard