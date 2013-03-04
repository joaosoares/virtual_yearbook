import wx

class Example(wx.Frame):

	def __init__(self, *args, **kw):
		super(Example, self).__init__(*args, **kw)
		self.InitUI()
		
	def InitUI(self):
		# Outer panel
		pnl = wx.Panel(self)

		# Box Sizer to keep all controls
		sizer = wx.BoxSizer(wx.VERTICAL)
		# Horizontal centering
		sizer.AddStretchSpacer( prop=1 )


		# CONTROLS
		# PASB logo
		logo = wx.StaticBitmap(pnl, bitmap=wx.Bitmap('logo.png'))
		sizer.Add(logo, 0, wx.ALIGN_CENTER)
		# Title
		title = wx.StaticBitmap(pnl, bitmap=wx.Bitmap('title.png'))
		sizer.Add(title, 0, wx.ALIGN_CENTER)
		# Button to open yearbook
		startbook = wx.Button(pnl, wx.ID_NEW, 'Open the Yearbook!', size=((-1,60))) 
		startbook.Bind(wx.EVT_BUTTON, self.OpenBook)
		sizer.Add(startbook, 0, wx.ALIGN_CENTER)
		
		# Horizontal centering
		sizer.AddStretchSpacer( prop=1 )

		pnl.SetSizer( sizer )
		#self.Layout()

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
		qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('logo.png'))

		self.Bind(wx.EVT_MENU, self.OnQuit, fitem)


		#self.ShowFullScreen(True)
		self.Maximize()
		self.Centre()
		self.Show(True)

	def OnQuit(self, e):
		self.Close()


if __name__ == '__main__':
	app = wx.App()
	Book(None)
	app.MainLoop()