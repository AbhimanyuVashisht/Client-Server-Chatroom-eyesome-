"""
**File:** rendezvous.py

A couple functions in a class just to facilitate communication between the
networking thread and the main thread which does the graphics.  Basically, the
only purpose of these functions is so that the code that does the networking
does not have to know anything about how the graphics are done (wx, TK, ...).
Having this in a separate file also helps with imports so that there is not an
import loop between the graphics and networking.

When used with wxPython, We just use the :func:`wx.CallAfter` function to send
data from the networking thread to the wxFrame in the main thread.

If used with TKinter graphics (a previous implementation), we have to use a
queue and generate new events on our own -- much more complicated.
"""

import wx

class Rendezvous(object):
    """
    Messages from the networking thread get left here and
    the appropriate wxPython events are generated to notify and pass
    data to the graphics thread.
    """
    def __init__(self, wxConnected, wxDisplay, wxLost):
        self.wxConnected = wxConnected
        self.wxDisplay = wxDisplay
        self.wxLost = wxLost

    def connected(self):
        "Notify the main tread that we are connected to the server"
        wx.CallAfter(self.wxConnected)

    def display(self, msg):
        "shuttle a message to be displayed in the chat read window"
        wx.CallAfter(self.wxDisplay, msg)

    def lost(self, msg):
        "Notify the main tread that the network connection dropped"
        wx.CallAfter(self.wxLost, msg)
