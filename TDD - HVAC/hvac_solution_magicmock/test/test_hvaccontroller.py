import pytest

from unittest.mock import MagicMock, patch
from src.hvaccontroller import HVACController


@pytest.fixture
def hvac_spy():
    patcher = patch("src.hvaccontroller.HVAC")
    yield patcher.start()

    patcher.stop()


def test__given_fresh_instance__then_everything_should_be_off(hvac_spy: MagicMock):
    hvac_spy.configure_mock(
        is_blowing=True,
        is_cooling=True,
        is_heating=True
    )

    sut = HVACController(hvac_spy)

    assert_hvac_is_idling(hvac_spy)


def test__given_temperature_it_is_too_hot__when_regulating__should_be_cooling_and_blowing(hvac_spy: MagicMock):
    hvac_spy.configure_mock(
        is_blowing=False,
        is_cooling=False,
        is_heating=False
    )

    sut = HVACController(hvac_spy)
    sut.desired_temperature = 22
    sut.allowed_temperature_delta = 2

    actual_temperature = 25
    sut.regulate(actual_temperature)

    assert_hvac_is_cooling(hvac_spy)


def test__given_temperature_it_is_too_cold__when_regulating__should_be_heating_and_blowing(hvac_spy: MagicMock):
    hvac_spy.configure_mock(
        is_blowing=False,
        is_cooling=False,
        is_heating=False
    )

    sut = HVACController(hvac_spy)
    sut.desired_temperature = 22
    sut.allowed_temperature_delta = 2

    actual_temperature = 19
    sut.regulate(actual_temperature)

    assert_is_heating(hvac_spy)


def test__given_at_max_allowed_temperature__when_regulating__should_be_idling(hvac_spy: MagicMock):
    hvac_spy.configure_mock(
        is_blowing=False,
        is_cooling=False,
        is_heating=False
    )

    sut = HVACController(hvac_spy)
    hvac_spy.configure_mock(
        is_blowing=True,
        is_cooling=True,
        is_heating=True
    )

    sut.desired_temperature = 22
    sut.allowed_temperature_delta = 3

    actual_temperature = 25
    sut.regulate(actual_temperature)

    assert_hvac_is_idling(hvac_spy)


def test__given_at_min_allowed_temperature__when_regulating__should_be_idling(hvac_spy: MagicMock):
    hvac_spy.configure_mock(
        is_blowing=False,
        is_cooling=False,
        is_heating=False
    )

    sut = HVACController(hvac_spy)
    hvac_spy.configure_mock(
        is_blowing=True,
        is_cooling=True,
        is_heating=True
    )

    sut.desired_temperature = 22
    sut.allowed_temperature_delta = 3

    actual_temperature = 19
    sut.regulate(actual_temperature)

    assert_hvac_is_idling(hvac_spy)


def assert_hvac_is_idling(hvac_spy: MagicMock):
    assert hvac_spy.is_blowing == False
    assert hvac_spy.is_cooling == False
    assert hvac_spy.is_heating == False


def assert_hvac_is_cooling(hvac_spy: MagicMock):
    assert hvac_spy.is_blowing == True
    assert hvac_spy.is_cooling == True
    assert hvac_spy.is_heating == False


def assert_is_heating(hvac_spy):
    assert hvac_spy.is_blowing == True
    assert hvac_spy.is_cooling == False
    assert hvac_spy.is_heating == True
