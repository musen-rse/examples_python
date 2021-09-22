import unittest

from src.EnvironmentController import EnvironmentController
from src.EnvironmentController import HVAC


class HVACSpy(HVAC):
    def __init__(self):
        self.blowing = True
        self.heating = True
        self.cooling = True

    def is_blowing(self):
        return self.blowing

    def is_heating(self):
        return self.heating

    def is_cooling(self):
        return self.cooling


    def set_blowing(self, blowing: bool) -> None:
        self.blowing = blowing

    def set_cooling(self, cooling: bool) -> None:
        self.cooling = cooling

    def set_heating(self, heating: bool) -> None:
        self.heating = heating

    def set_temperature(self, temperature: float) -> None:
        self.temperature = temperature

    def get_temperature(self) -> int:
        return self.temperature
    

class TestEnvironmentController(unittest.TestCase):

    def setUp(self):
        self.hvac = HVACSpy()
        self.sut = EnvironmentController(self.hvac)

    def test__upon_construction_everything_should_be_off(self):
        self.assert_is_idling()

    def test__when_its_too_hot_it_should_start_cooling(self):
        self.make_it_too_hot()
        self.sut.check_temperature()
        self.assert_is_cooling()

    def test__when_its_too_cold_it_should_start_heating(self):
        self.make_it_too_cold()
        self.sut.check_temperature()
        self.assert_is_heating()

    def test__given_it_is_too_cold_when_its_getting_comfortable_should_keep_blowing(self):
        self.transition_from_too_cold_to_comfortable()

        self.sut.check_temperature()

        self.assert_is_only_blowing()

    def test__given_it_is_too_hot_when_its_getting_comfortable_should_be_idling(self):
        self.transition_from_too_hot_to_comfortable()

        self.sut.check_temperature()

        self.assert_is_idling()

    def test__given_blowing_for_3_minutes_after_heating_should_be_idling(self):
        self.transition_from_too_cold_to_comfortable()
        self.sut.check_temperature()
        self.sut.check_temperature()

        self.sut.check_temperature()

        self.assert_is_idling()

    def test__given_it_is_too_hot_when_there_is_blitzeis_it_should_start_heating(self):
        self.directly_transition_from_too_hot_to_too_cold()

        self.sut.check_temperature()
        
        self.assert_is_heating()

    def test__given_it_is_too_cold_when_there_is_blitze_it_should_start_cooling(self):
        self.make_it_too_cold()
        self.sut.check_temperature()
        self.make_it_too_hot()

        self.sut.check_temperature()
        
        self.assert_is_cooling()

    def transition_from_too_cold_to_comfortable(self):
        self.make_it_too_cold()
        self.sut.check_temperature()
        self.make_it_comfortable_after_it_was_too_cold()

    def transition_from_too_hot_to_comfortable(self):
        self.make_it_too_hot()
        self.sut.check_temperature()
        self.make_it_comfortable_after_it_was_too_hot()

    def directly_transition_from_too_hot_to_too_cold(self):
        self.make_it_too_hot()
        self.sut.check_temperature()
        self.make_it_too_cold()

    def make_it_too_cold(self):
        self.sut.set_desired_temperature(23)
        self.sut.set_temperature_delta(3)
        self.hvac.set_temperature(19)

    def assert_is_idling(self):
        self.assertFalse(self.hvac.is_blowing())
        self.assertFalse(self.hvac.is_heating())
        self.assertFalse(self.hvac.is_cooling())

    def assert_is_only_blowing(self):
        self.assertTrue(self.hvac.is_blowing())
        self.assertFalse(self.hvac.is_cooling())
        self.assertFalse(self.hvac.is_heating())

    def assert_is_cooling(self):
        self.assertTrue(self.hvac.is_blowing())
        self.assertFalse(self.hvac.is_heating())
        self.assertTrue(self.hvac.is_cooling())

    def assert_is_heating(self):
        self.assertTrue(self.hvac.is_blowing())
        self.assertTrue(self.hvac.is_heating())
        self.assertFalse(self.hvac.is_cooling())

    def make_it_too_hot(self):
        self.sut.set_desired_temperature(23)
        self.sut.set_temperature_delta(3)
        self.hvac.set_temperature(27)

    def make_it_comfortable_after_it_was_too_cold(self):
        self.sut.set_desired_temperature(23)
        self.sut.set_temperature_delta(3)
        self.hvac.set_temperature(20)

    def make_it_comfortable_after_it_was_too_hot(self):
        self.sut.set_desired_temperature(23)
        self.sut.set_temperature_delta(3)
        self.hvac.set_temperature(26)