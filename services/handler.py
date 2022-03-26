import asyncio
import re
from bleak import BleakScanner
from services.struct import BleDevice


def get_ble_devices(search_dev: str = "") -> list[BleDevice]:
    devices_data: list[BleDevice] = []

    async def main():
        devices = await BleakScanner.discover()
        if devices:
            for d in devices:
                if search_dev:
                    if re.search(search_dev, d.name):
                        devices_data.append(BleDevice(address=d.address, name=d.name, meta_data=d.metadata))
                        break
                else:
                    devices_data.append(BleDevice(address=d.address, name=d.name, meta_data=d.metadata))
    asyncio.run(main())

    return devices_data

