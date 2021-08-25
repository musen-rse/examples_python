from abc import ABC, abstractmethod


class HVAC(ABC):
    """
    An abstract class representing the HVAC hardware
    """

    @property
    @abstractmethod
    def temperature_in_c(self) -> float:
        pass

    @property
    @abstractmethod
    def is_blowing(self) -> bool:
        pass

    @property
    @abstractmethod
    def is_cooling(self) -> bool:
        pass

    @property
    @abstractmethod
    def is_heating(self) -> bool:
        pass

    @is_blowing.setter
    @abstractmethod
    def is_blowing(self, value: bool) -> None:
        pass

    @is_cooling.setter
    @abstractmethod
    def is_cooling(self, value: bool) -> None:
        pass

    @is_heating.setter
    @abstractmethod
    def is_heating(self, value: bool) -> None:
        pass


class HVACController:

    def __init__(self, hvac: HVAC) -> None:
        self._hvac = hvac
        self.desired_temperature: int = 0
        self.allowed_temperature_delta: int = 0

        self.turn_off()

    def regulate(self, temperature) -> None:
        if self.should_start_cooling(temperature):
            self.start_cooling()
        elif self.should_start_heating(temperature):
            self.start_heating()
        else:
            self.turn_off()

    def should_start_cooling(self, temperature):
        return temperature > self.desired_temperature + self.allowed_temperature_delta

    def should_start_heating(self, temperature):
        return temperature < self.desired_temperature - self.allowed_temperature_delta

    def turn_off(self):
        self._hvac.is_blowing = False
        self._hvac.is_cooling = False
        self._hvac.is_heating = False

    def start_heating(self):
        self._hvac.is_blowing = True
        self._hvac.is_heating = True

    def start_cooling(self):
        self._hvac.is_blowing = True
        self._hvac.is_cooling = True
