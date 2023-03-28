def on_button_pressed_b():
    if led.point(0, 0):
        basic.show_leds("""
            . . . . .
                        . . . . #
                        . . . # .
                        # . # . .
                        . # . . .
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    basic.clear_screen()
    for index in range(5):
        led.plot(index, randint(0, 4))
loops.every_interval(100, on_every_interval)
input.on_button_pressed(Button.A, on_button_pressed_a)
