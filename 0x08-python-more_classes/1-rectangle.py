#!/usr/bin/python3
"""This is a class rectangle
"""
class Retangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width:retrieves the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width and its value
        """
        if not instance(widt,int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        height:retrievs the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height and its value
        """
        if not instance(height,int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        self.__heigt = height




