# -*- coding: utf-8 -*-


class UartDevice(object):

    def __init__(self, address, tx_char_uuid, rx_char_uuid, **kwargs):
        self.address = address
        self.tx_char_uuid = tx_char_uuid
        self.rx_char_uuid = rx_char_uuid

    def __repr__(self):
        return str(self)


class BgmDevice(object):
    def __init__(self, name: str, address: str, uuids: list, **kwargs):
        self.name = name
        self.address = address
        self.uuids = uuids

    def __dict__(self):
        return {"name": self.name, "address": self.address, "uuids": self.uuids}


class BleDevice(object):
    def __init__(self, name: str, address: str, meta_data: object, **kwargs):
        self.name = name
        self.address = address
        self.meta_data = meta_data

    def __dict__(self):
        return {"name": self.name, "address": self.address, "meta_data": self.meta_data}
