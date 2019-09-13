from tkinter import *
import apier
from tkinter import messagebox

class apiergui:
	
	def getdata(o, e):
		messagebox.showinfo("Request content:", o.apier.res)

	def startreq(o, e):
		o.apier.seturl(o.root.URL_E.get())
		o.apier.setmethod(o.root.METHOD_E.get())
		o.apier.execute()
		o.root.DATA_B["text"]=str(o.apier.status)
		o.root.DATA_B.grid(column=1, row=5)
		

	def addh_parser(o, e):
		pk=o.ahead.ke.get()
		pv=o.ahead.ve.get()
		if pk in o.apier.heads:
			o.root.HEADS_X.delete(o.root.HEADS_X.get(0, END).index(pk+": "+o.apier.heads[pk]))
		o.root.HEADS_X.insert(0, pk+": "+pv)
		o.apier.addheads({pk: pv})

	def addhead(o, e):
		o.ahead=Tk()
		o.ahead.title("Add header")
		o.ahead.kl=Label(o.ahead, text="Key:")
		o.ahead.ke=Entry(o.ahead)
		o.ahead.vl=Label(o.ahead, text="Value:")
		o.ahead.ve=Entry(o.ahead)
		o.ahead.ab=Button(o.ahead, text="+")
		o.ahead.kl.grid(column=0, row=0)
		o.ahead.ke.grid(column=1, row=0)
		o.ahead.vl.grid(column=0, row=1)
		o.ahead.ve.grid(column=1, row=1)
		o.ahead.ab.grid(column=1, row=2)
		o.ahead.ab.bind("<Button-1>", o.addh_parser)
		o.ahead.mainloop()


	def addp_parser(o, e):
		pk=o.aparam.ke.get()
		pv=o.aparam.ve.get()
		if pk in o.apier.params:
			o.root.PARAMS_X.delete(o.root.PARAMS_X.get(0, END).index(pk+": "+o.apier.params[pk]))
		o.root.PARAMS_X.insert(0, pk+": "+pv)
		o.apier.addparams({pk: pv})

	def addparam(o, e):
		o.aparam=Tk()
		o.aparam.title("Add parameter")
		o.aparam.kl=Label(o.aparam, text="Key:")
		o.aparam.ke=Entry(o.aparam)
		o.aparam.vl=Label(o.aparam, text="Value:")
		o.aparam.ve=Entry(o.aparam)
		o.aparam.ab=Button(o.aparam, text="+")
		o.aparam.kl.grid(column=0, row=0)
		o.aparam.ke.grid(column=1, row=0)
		o.aparam.vl.grid(column=0, row=1)
		o.aparam.ve.grid(column=1, row=1)
		o.aparam.ab.grid(column=1, row=2)
		o.aparam.ab.bind("<Button-1>", o.addp_parser)
		o.aparam.mainloop()

	def __init__(o):
		o.root=Tk()
		o.root.title("APIer")
		o.apier=apier.apier()
		
		#URL & METHOD
		o.root.URL_L=Label(o.root, text="URL:")
		o.root.URL_L.grid(column=0, row=0)

		o.root.URL_E=Entry(o.root)
		o.root.URL_E.grid(column=1, row=0)
	
		o.root.METHOD_L=Label(o.root, text="Method:")
		o.root.METHOD_L.grid(column=2, row=0)
		
		o.root.METHOD_E=Entry(o.root)
		o.root.METHOD_E.grid(column=3, row=0)
		o.root.METHOD_E.insert(0, "GET")

		#PARAMS
		o.root.PARAMS_L=Label(o.root, text="Parameters:")
		o.root.PARAMS_L.grid(column=0, row=1)

		o.root.ADDP_B=Button(o.root, text="+")
		o.root.ADDP_B.grid(column=0, row=2)
		o.root.ADDP_B.bind("<Button-1>", o.addparam)
	
		o.root.PARAMS_X=Listbox(o.root)
		o.root.PARAMS_X.grid(column=1, row=2)

		#HEADERS
		o.root.HEADS_L=Label(o.root, text="Headers:")
		o.root.HEADS_L.grid(column=0, row=3)
		
		o.root.ADDH_B=Button(o.root, text="+")
		o.root.ADDH_B.grid(column=0, row=4)
		o.root.ADDH_B.bind("<Button-1>", o.addhead)

		o.root.HEADS_X=Listbox(o.root)
		o.root.HEADS_X.grid(column=1, row=4)	

		#BUTTONS
		o.root.DOIT_B=Button(o.root, text="Start request")
		o.root.DOIT_B.grid(column=0, row=5)
		o.root.DOIT_B.bind("<Button-1>", o.startreq)

		o.root.DATA_B=Button(o.root)
		o.root.DATA_B.bind("<Button-1>", o.getdata)

		o.root.mainloop()
		

a=apiergui()
