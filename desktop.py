#import the neccesery module!
from plyer import notification

#specify the parameters
title = 'Hello Amazing people'

message = 'My Name is Prem sagar'

name = 'notifier'

notification.notify(title = title,
                    message = message,
                    app_icon = None,
                    app_name= name,
                    timeout = 5,
                    toast = False)