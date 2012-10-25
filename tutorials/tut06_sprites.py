"""Tutorial 06: Displaying sprites.

This tutorial shows how to display sprites, e.g. a same texture at different
positions.

"""

# We import galry.
from galry import *

# We also importnumpy.random in order to generate random data.
import numpy as np
import numpy.random as rdn

def create_texture():
    """This function creates a cross-like texture."""
    
    # We use an alpha channel for transparency of the cross outside the cross
    # itself.
    texture = np.zeros((15, 15, 4))
    texture[7, :, :] = texture[:, 7, :] = 1
    return texture

class MyPaintManager(PaintManager):
    def initialize(self):
        
        # We create a small cross texture.
        texture = create_texture()
        
        # Number of sprites.
        n = 100000
        
        # Positions of the sprites.
        X, Y = .2 * rdn.randn(2, n)
        
        # Color of all sprites (with transparency).
        colors = rdn.rand(n, 4)
        
        # We add sprites.
        self.add_sprites(X, Y, color=colors, texture=texture)

show_basic_window(paint_manager=MyPaintManager)