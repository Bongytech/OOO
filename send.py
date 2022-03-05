import notify2
notify2.init('online or offline')
n = notify2.Notification('Status Offline', 'Youre are offline')
n.show()
