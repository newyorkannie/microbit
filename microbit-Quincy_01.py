def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.show_leds("""
        # # # # .
        # . . # .
        # . . # .
        # . # # .
        # # # # #
        """)
    basic.show_leds("""
        # . . # .
        # . . # .
        # . . # .
        # . . # .
        . # # . .
        """)
    basic.show_leds("""
        . # # # .
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        """)
    basic.show_leds("""
        # . . # .
        # # . # .
        # # # # .
        # . # # .
        # . . # .
        """)
    basic.show_leds("""
        # # # # .
        # . . . .
        # . . . .
        # . . . .
        # # # # .
        """)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        # # # . .
        # . . # .
        # . . # .
        # . . # .
        # # # . .
        """)
    basic.show_leds("""
        . . # . .
        . # . # .
        # # # # #
        # . . . #
        # . . . #
        """)
    basic.show_leds("""
        # # # . .
        # . . # .
        # . . # .
        # . . # .
        # # # . .
        """)
basic.forever(on_forever)
