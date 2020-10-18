import wx
import os


ID_OTHER = 0


class MainWindows(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1024, 700))

        try:
            self.SetIcon(wx.Icon("EEM.png", wx.BITMAP_TYPE_PNG))
        finally:
            pass

        self.CreateStatusBar()

        file_menu = wx.Menu()
        prices_menu = wx.Menu()
        charts_menu = wx.Menu()

        menu_open = file_menu.Append(wx.ID_OPEN, "&Open file", "Open a CSV file with market datas")
        file_menu.AppendSeparator()
        menu_about = file_menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        file_menu.AppendSeparator()
        menu_exit = file_menu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")

        menu_prices_all = prices_menu.Append(ID_OTHER, "&All items prices", "Show price for all items")

        menu_charts = charts_menu.Append(ID_OTHER, "&Prices evolution", "Display evolution chart of an item")

        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&File")
        menuBar.Append(prices_menu, "&Prices")
        menuBar.Append(charts_menu, "&Charts")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnExit, menu_exit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)
        self.Bind(wx.EVT_MENU, self.OnOpen, menu_open)

        self.Show(True)

    def OnAbout(self):
        dlg = wx.MessageDialog(self, "A tool for getting prices from the market")
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self):
        self.Close(True)

    def OnOpen(self):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.csv", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    MainWindows(None, "Eve Echoes Market")
    app.MainLoop()
