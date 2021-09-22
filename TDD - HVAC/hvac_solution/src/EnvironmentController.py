from abc import abstractmethod
from typing import Protocol


class HVAC(Protocol):
    """
    An abstract class representing the HVAC hardware
    """

    @abstractmethod
    def set_blowing(self, blowing: bool) -> None:
        pass

    @abstractmethod
    def set_cooling(self, cooling: bool) -> None:
        pass

    @abstractmethod
    def set_heating(self, heating: bool) -> None:
        pass

    @abstractmethod
    def is_heating(self) -> bool:
        pass

    @abstractmethod
    def get_temperature(self) -> int:
        pass


class EnvironmentController:

    class PostHeatingTimer:

        def __init__(self, amount: int = 3):
            self._amount = amount
            self._counter = 0
            self._started = False

        def start(self):
            self._started = True
            self._counter = 0

        def count(self):
            self._counter += 1

        def done(self):
            return self._counter > self._amount or not self._started

    def __init__(self, hvac: HVAC) -> None:
        self._hvac = hvac
        self._post_heating_timer = EnvironmentController.PostHeatingTimer()
        self.start_idling()

    def set_temperature_delta(self, temperature_delta: int):
        self._temperature_delta = temperature_delta
    
    def set_desired_temperature(self, temperature: int):
        self._desired_temperature = temperature

    def check_temperature(self):
        temperature = self._hvac.get_temperature()
        
        if self.its_too_cold(temperature):
            self.start_heating()
            self._post_heating_timer.start()
        elif self.its_too_hot(temperature):
            self.start_cooling()
        else:
            self.start_idling()
        
        self.control_post_heating_blower()

    def control_post_heating_blower(self):
        self._post_heating_timer.count()
        if not self._post_heating_timer.done():
            self._hvac.set_blowing(True)

    def its_too_cold(self, temperature: int):
        return temperature < self._desired_temperature - self._temperature_delta

    def its_too_hot(self, temperature: int):
        return temperature > self._desired_temperature + self._temperature_delta

    def start_cooling(self):
        self._hvac.set_blowing(True)
        self._hvac.set_cooling(True)
        self._hvac.set_heating(False)

    def start_heating(self):
        self._hvac.set_blowing(True)
        self._hvac.set_cooling(False)
        self._hvac.set_heating(True)

    def start_idling(self):
        self._hvac.set_blowing(False)
        self._hvac.set_cooling(False)
        self._hvac.set_heating(False)

