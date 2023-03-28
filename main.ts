input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (led.point(0, 0)) {
        basic.showLeds(`
            . . . . .
                        . . . . #
                        . . . # .
                        # . # . .
                        . # . . .
        `)
    } else {
        basic.showLeds(`
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        `)
    }
    
})
basic.forever(function on_forever() {
    
})
loops.everyInterval(100, function on_every_interval() {
    basic.clearScreen()
    for (let index = 0; index < 5; index++) {
        led.plot(index, randint(0, 4))
    }
})
input.onButtonPressed
