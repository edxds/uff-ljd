from vendor.pplay.window import *


def center_x_in_window(element, window: Window):
    element.set_position(window.width / 2 - element.width / 2, element.y)


def center_y_in_window(element, window: Window):
    element.set_position(element.x, window.height / 2 - element.height / 2)


def center_in_window(element, window: Window):
    center_x_in_window(element, window)
    center_y_in_window(element, window)


def center_elements(element_a, element_b):
    element_b.set_position(
        element_a.x - (element_a.width / 2 - element_b.width / 2),
        element_a.y - (element_a.height / 2 - element_b.height / 2),
    )
