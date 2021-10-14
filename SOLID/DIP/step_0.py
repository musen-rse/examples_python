###############################################################################
# non volatile core of our application                                        #
###############################################################################


class Botton:

    def __init__(self, lamp) -> None:
        self._lamp = lamp

    def toggle_on(self) -> None:
        self._lamp.light_on()

    def toggle_off(self) -> None:
        self._lamp.light_off()

###############################################################################
# volatile part of our application                                            #
###############################################################################


class Lamp():
  
      def light_on(self) -> None:
          print("Light is on.")

      def light_off(self) -> None:
          print("Light is off.")


if __name__ == '__main__':
    lamp = Lamp()
    button = Botton(lamp)
    button.toggle_on()
    button.toggle_off()
