import asyncio
import re
import platform
from bleak import BleakClient
from bleak import BleakScanner
import sys
from services.struct import UartDevice, BgmDevice
from services.exception import NotBgmDeviceException


def conn_to_bgm(bgm_address: str):
    if not is_bgm_device(bgm_address):
        raise NotBgmDeviceException

    def callback(_, data):
        print(data.decode('utf8', 'ignore'))

    async def connect_to_device(address):
        print("starting", address, "loop")
        pcl_uuid = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0xFEE1) # Enable write permission
        notify_uuid = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0xFEE2)

        async with BleakClient(address, timeout=10.0) as client:
            # svcs = await client.get_services()
            # print("Services:")
            # for service in svcs:
            #     print(service)
            print("connect to", address)
            try:
                await client.write_gatt_char(pcl_uuid, bytearray("1", 'utf-8'), True)
                # await client.start_notify(notify_uuid, callback)
                # await asyncio.sleep(5.0)
                # await client.stop_notify(notify_uuid)
            except Exception as e:
                print(e)
        print("disconnect from", address)

    asyncio.run(connect_to_device(bgm_address))





def get_bgm_devices():
    bgm_service_uuid = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0xFEE0)
    bgm_devices: list[BgmDevice] = []

    async def main():
        devices = await BleakScanner.discover()
        if devices:
            for d in devices:
                if platform.system() == 'Linux':
                    uuids = d.details["props"]["UUIDs"]
                else:
                    uuids = d.metadata["uuids"]

                if bgm_service_uuid in uuids:
                    device = BgmDevice(address=d.address, name=d.name, uuids=uuids)
                    bgm_devices.append(device)

    asyncio.run(main())

    return bgm_devices


def is_bgm_device(address: str) -> bool:
    bgm_devices = get_bgm_devices()

    is_bgm = False
    for device in bgm_devices:
        if device.address == address:
            is_bgm = True
    return is_bgm



if __name__ == "__main__":
    # get all bgm devices information.
    # for device in get_bgm_devices():
    #     print(device.__dict__())

    ADDRESS = (
        'B0:C2:05:09:C1:C3'
        if platform.system() != "Darwin"
        else "96A274DD-FF4C-637C-74BF-DE276888FBF8"   #2772UAQ0214
        # else "F3E1207C-6D3A-E1D2-1C02-52FB35CC52AF"  # 2772UAQ0215
    )


    conn_to_bgm(ADDRESS)
