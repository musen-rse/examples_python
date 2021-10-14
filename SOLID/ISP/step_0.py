from typing import Protocol


###############################################################################
# non volatile core of our application                                        #
###############################################################################


class CommunicationDevice(Protocol):

    def make_call(self, number: str) -> None:
        raise NotImplementedError

    def send_sms(self, number: str) -> None:
        raise NotImplementedError

    def send_email(self, address: str) -> None:
        raise NotImplementedError


def send_sms(device: CommunicationDevice) -> None:
    device.send_sms("+123456790")

def send_email(device: CommunicationDevice) -> None:
    device.send_email("+123456790")

def make_call(device: CommunicationDevice) -> None:
    device.make_call("+123456790")


###############################################################################
# volatile part of our application                                            #
###############################################################################


class LandLinePhone(CommunicationDevice):

    def make_call(self, number: str) -> None:
        print(f"Land line calling {number}")

    def send_sms(self, number: str) -> None:
        pass

    def send_email(self, address: str) -> None:
        pass


class SmartPhone(CommunicationDevice):

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
    send_sms(land_line_phone)
    send_email(land_line_phone)
    