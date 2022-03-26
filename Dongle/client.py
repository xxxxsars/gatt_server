import asyncio
from bleak import BleakClient
from bleak import BleakScanner
import sys
from services.struct import UartDevice

def interact_uart(uart_device: UartDevice):
    def handle_rx(_: int, data: bytearray):
        print("received:", data)

    async def main(ble_address):
        device = await BleakScanner.find_device_by_address(ble_address, timeout=5.0)
        if not device:
            raise Exception(f"A device with address {ble_address} could not be found.")

        async with BleakClient(ble_address) as client:
            await client.start_notify(uart_device.tx_char_uuid, handle_rx)
            print("Connected, start typing and press ENTER...")
            loop = asyncio.get_running_loop()
            while True:
                data = await loop.run_in_executor(None, sys.stdin.buffer.readline)
                if data == b'\r\n':
                    break
                await client.write_gatt_char(uart_device.rx_char_uuid, data)
                print("sent:", data)

    asyncio.run(main(uart_device.address))

