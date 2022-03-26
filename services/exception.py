
class NotBgmDeviceException(Exception):
    def __init__(self, msg="Your provide address was not  bgm device.", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)