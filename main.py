import wx

class Example(wx.Frame):

	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw)
		self.InitUI()
		
	def InitUI(self):
		pnl = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)

		logo = wx.StaticBitmap(pnl, bitmap=wx.Bitmap('logo.png'))
		sizer.Add(logo, 1, wx.EXPAND)
		title = wx.StaticBitmap(pnl, bitmap=wx.Bitmap('title.png'))
		sizer.Add(title, 1, wx.EXPAND)
		startbook = wx.Button(pnl, label='Open the Yearbook!', pos=(20, 30))
		startbook.Bind(wx.EVT_BUTTON, self.OpenBook)
		
		# sizer.AddMany([(logo, 1, wx.EXPAND),(title,1,wx.EXPAND),(startbook,1,wx.EXPAND)])


		self.SetSize((600,400))
		self.SetTitle('Virtual Yearbook')
		self.Centre()
		self.Show(True)

	def OpenBook(self, e):
		Book(None)
 
class Book(wx.Frame):
	def __init__(self, *args, **kw):
		super(Book, self).__init__(*args, **kw)
		self.InitUI()

	def InitUI(self):

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')
		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)

		toolbar = self.CreateToolBar()
		quit_icon = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (8,8))
		qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', quit_icon)

		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)


		#self.ShowFullScreen(True)
		self.SetSize((300,200))
		self.Centre()
		self.Show(True)

	def OnQuit(self, e):
		self.Close()


if __name__ == '__main__':
	app = wx.App()
	Example(None)
	app.MainLoop()