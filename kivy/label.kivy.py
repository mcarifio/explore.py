#!/usr/bin/env python
import os

# logging
import icecream as ic
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
_debug_method = logger.debug
logger.debug = lambda *args, **kwargs: _debug_method(ic.argumentToString(' '.join(map(str, args))), **kwargs)
logger.debug("here")

import kivy
kivy.require('2.3.0')
logger.debug(kivy)

import kivy.app
import kivy.uix.button


# Inherit Kivy's App class which represents the window for our widgets
# HelloKivy inherits all the fields and methods from Kivy

class App(kivy.app.App):
    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        logger.debug("build")
        result = kivy.uix.button.Label(text = f"[color=3333ff][b]{os.path.realpath(__file__)}[/b][/color]", markup = True, font_size='20sp')
        logger.debug(type(result))
        return result

if __name__ == '__main__':
    app = App()
    app.run()
