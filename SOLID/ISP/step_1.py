from typing import Protocol


###############################################################################
# non volatile core of our application                                        #
###############################################################################


class CallingDevice(Protocol):

    def make_call(self, number: str) -> None:
        raise NotImplementedError


class SmsDevice(Protocol):
    def send_sms(self, number: str) -> None:
        raise NotImplementedError


class EmailDevice(Protocol):
    def send_email(self, address: str) -> None:
        raise NotImplementedError


def send_sms(device: SmsDevice) -> None:
    device.send_sms("+123456790")


def send_email(device: EmailDevice) -> None:
    device.send_email("+123456790")


def make_call(device: CallingDevice) -> None:
    device.make_call("+123456790")


###############################################################################
# volatile part of our application                                            #
###############################################################################


class LandLinePhone(CallingDevice):

    def make_call(self, number: str) -> None:
        print(f"Land line calling {number}")


class SmartPhone(CallingDevice, SmsDevice, EmailDevice):

    def make_call(self, number: str) -> None:
        print(f"Smartphone calling {number}")

    def send_sms(self, number: str) -> None:
        print(f"Smartphone sending sms to {number}")

    def send_email(self, address: str) -> None:
        print(f"Smartphone sending email to {address}")


if __name__ == "__main__":
    smart_phone = SmartPhone()
    make_call(smart_phone)
    send_sms(smart_phone)
    send_email(smart_phone)

    land_line_phone = LandLinePhone()
    make_call(land_line_phone)
    