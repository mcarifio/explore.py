#!/usr/bin/env python

import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Label
# Inherit Kivy's App class which represents the window for our widgets
# HelloKivy inherits all the fields and methods from Kivy

class HelloKivy(App):
    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        return Label(text ="Hello Geeks")

if __name__ == '__main__':
    helloKivy = HelloKivy()
    helloKivy.run()
