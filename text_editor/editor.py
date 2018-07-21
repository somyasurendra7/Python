from tkinter.messagebox import *
from tkinter.filedialog import *


class Editor:
	root = Tk()
	# default settings
	thisWidth = 300
	thisHeight = 300
	thisTextArea = Text(root)
	thisMenuBar = Menu(root)
	thisFileMenu = Menu(thisMenuBar, tearoff=0)
	thisEditMenu = Menu(thisMenuBar, tearoff=0)
	thisHelpMenu = Menu(thisMenuBar, tearoff=0)
	thisScrollBar = Scrollbar(thisTextArea)
	file = None

	def __init__(self, **kwargs):
		# Setting window size and icon
		try:
			self.root.wm_iconbitmap("Editor.ico")
		except:
			pass

		try:
			self.thisWidth = kwargs['weight']
		except KeyError:
			pass

		try:
			self.thisHeight = kwargs['height']
		except KeyError:
			pass

		# Window text
		self.root.title("Untitled Document")

		# aligning the window
		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()
		left = (screenWidth / 2) - (self.thisWidth / 2)
		top = (screenHeight / 2) - (self.thisHeight / 2)

		self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))

		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)

		# Adding menu controls
		self.thisTextArea.grid(sticky=N + E + S + W)
		# 'New' menu option
		self.thisFileMenu.add_command(label="New", command=self.newFile)
		# 'Open' menu option
		self.thisFileMenu.add_command(label="Open", command=self.openFile)
		# 'Save' menu option
		self.thisFileMenu.add_command(label="Save", command=self.saveFile)
		# create a line separator in the dialog
		self.thisFileMenu.add_separator()
		# 'Exit' the editor
		self.thisFileMenu.add_command(label="Exit", command=self.quitApplication)
		self.thisMenuBar.add_cascade(label="File", menu=self.thisFileMenu)
		# 'Cut' menu option
		self.thisEditMenu.add_command(label="Cut", command=self.cut)
		# 'Copy' menu option
		self.thisEditMenu.add_command(label="Copy", command=self.copy)
		# 'Paste' menu option
		self.thisEditMenu.add_command(label="Paste", command=self.paste)
		# Editing feature
		self.thisMenuBar.add_cascade(label="Edit", menu=self.thisEditMenu)
		# 'About' menu option
		self.thisHelpMenu.add_command(label="About Editor", command=self.showAbout)
		self.thisMenuBar.add_cascade(label="Help", menu=self.thisHelpMenu)

		self.root.config(menu=self.thisMenuBar)
		self.thisScrollBar.pack(side=RIGHT, fill=Y)

		# adjusting scrolling
		self.thisScrollBar.config(command=self.thisTextArea.yview)
		self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

	# Functions
	def quitApplication(self):
		self.root.destroy()

	def showAbout(self):
		showinfo("Text Editor", "S.S")

	def openFile(self):
		self.file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

		if self.file == "":
			# no file available to open
			self.file = None
		else:
			# open the file and set the window title
			self.root.title(os.path.basename(self.file) + " - TextPad")
			self.thisTextArea.delete(1.0, END)

			file = open(self.file, "r")

			self.thisTextArea.insert(1.0, file.read())

			file.close()

	def newFile(self):
		self.root.title("Untitled Document")
		self.file = None
		self.thisTextArea.delete(1.0, END)

	def saveFile(self):
		if self.file == None:
			# save as new file
			self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
										  filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])

			if self.file == "":
				self.file = None
			else:
				# save the file
				file = open(self.file, "w")
				file.write(self.thisTextArea.get(1.0, END))
				file.close()
				# Change the title of the document
				self.root.title(os.path.basename(self.file) + " - Document")
		else:
			file = open(self.file, "w")
			file.write(self.thisTextArea.get(1.0, END))
			file.close()

	def cut(self):
		self.thisTextArea.event_generate("<<Cut>>")

	def copy(self):
		self.thisTextArea.event_generate("<<Copy>>")

	def paste(self):
		self.thisTextArea.event_generate("<<Paste>>")

	# Run
	def run(self):
		self.root.mainloop()


# Running the main application
textpad = Editor(width=600, height=400)
textpad.run()
