import pytest
from GUI import App

def test_run():
    """This allows us to test out our app by running the GUI so we can see 
    if everything is working as it should.
    """
    root = App()
    root.mainloop()
