"""Allows us to view and test GUI.py. In order to test functionality fill
out entry boxes, choose radio buttons, adjust sliders, and click buttons.
Output should be visible in the middle section where the treeview results
table is present.

"""
import pytest
from GUI import App

def test_run():
    """This allows us to test out our app by running the GUI so we can see 
    if everything is working as it should.
    """
    root = App()
    root.mainloop()
