from typing import List, Protocol


###############################################################################
# non volatile core of our application                                        #
###############################################################################


class ButtonServer(Protocol):
    
    def turn_on(self) -> None:
        raise NotImplementedError()

    def turn_off(self) -> None:
        raise NotImplementedError()


class Botton:

    def __init__(self, device: ButtonServer) -> None:
        self._device = device

    def toggle_on(self) -> None:
        self._device.turn_on()

    def toggle_off(self) -> None:
        self._device.turn_off()


###############################################################################
# volatile part of our application                                            #
###############################################################################


class Lamp(ButtonServer):
  
      def turn_on(self) -> None:
          print("Light is on.")

      def turn_off(self) -> None:
          print("Light is off.")


class TV(ButtonServer):
  
      def turn_on(self) -> None:
          print("TV is on.")

      def turn_off(self) -> None:
          print("TV is off.")


class Radio(ButtonServer):
  
      def turn_on(self) -> None:
          print("Radio is on.")

      def turn_off(self) -> None:
          print("Radio is off.")


if __name__ == '__main__':
    lamp = Lamp()
    lamp_btn = Botton(lamp)
    lamp_btn.toggle_on()
    lamp_btn.toggle_off()

    tv = TV()
    tv_btn = Botton(tv)
    tv_btn.toggle_on()
    tv_btn.toggle_off()

    radio = Radio()
    radio_btn = Botton(radio)
    radio_btn.toggle_on()
    radio_btn.toggle_off()
    

