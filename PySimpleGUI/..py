import wx
import wx.adv

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial", size=(500,500))

        bitmap = wx.Bitmap('C:/Users/advik/Documents/splash.gif')
        splash = wx.adv.SplashScreen(
                     bitmap, 
                     wx.adv.SPLASH_CENTER_ON_SCREEN|wx.adv.SPLASH_TIMEOUT, 
                     5000, self)
        splash.Show()

        self.Show()


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()