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


class Person:
    def __init__(self, communication_device: CommunicationDevice) -> None:
        self._communication_device = communication_device

    def send_sms(self, number: str) -> None:
        self._communication_device.send_sms(number)

    def send_email(self, address: str) -> None:
        self._communication_device.send_email(address)

    def make_call(self, number: str) -> None:
        self._communication_device.make_call(number)


###############################################################################
# volatile part of our application                                            #
###############################################################################


class LandLinePhone(CommunicationDevice):

    def make_call(self, number: str) -> None:
        print(f"Land line calling {number}")

    def send_sms(self, number: str) -> None:
        print("Land line can not send sms.")

    def send_email(self, address: str) -> None:
        print("Land line can not send email.")


class SmartPhone(CommunicationDevice):

    def make_call(self, number: str) -> None:
        print(f"Smartphone calling {number}")

    def send_sms(self, number: str) -> None:
        print(f"Smartphone sending sms to {number}")

    def send_email(self, address: str) -> None:
        print(f"Smartphone sending email to {address}")


if __name__ == "__main__":
    
    person1 = Person(LandLinePhone())
    person1.make_call("+123456789")
    person1.send_sms("+123456789")
    person1.send_email("+123456789")

    person2 = Person(SmartPhone())
    person2.make_call("+123456789")
    person2.send_sms("+123456789")
    person2.send_email("+123456789")
    