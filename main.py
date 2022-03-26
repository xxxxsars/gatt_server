from services.handler import get_ble_devices

if __name__ == "__main__":
    for d in (get_ble_devices()):
        print(d.__dict__())


