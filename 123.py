import pygame
import pytest
from renders.button import Button


def test_button_is_on_mouse():
    button = Button(
        50, 50, 100, 50, "Test", (255, 255, 255), (0, 0, 0)
    )  # create a test button
    assert button.is_on_mouse(
        (75, 75)
    )  # check that the button is clicked when the mouse is inside its bounds
    assert not button.is_on_mouse(
        (200, 200)
    )  # check that the button is not clicked when the mouse is outside its bounds


def test_button_click():
    button = Button(
        50, 50, 100, 50, "Test", (255, 255, 255), (0, 0, 0)
    )  # create a test button
    button.click()  # simulate a button click
    assert True  # add your assertion for what should happen when the button is clicked
