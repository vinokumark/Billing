from texttable import Texttable
from appJar import gui
import sqlite3, csv
con = sqlite3.connect('billing.db')
outp = [ str(row[0]) for row in con.execute('select item_list from list')]
count = 0

def billing():
    global count
    test = app.getEntry("item")
    tests = app.getEntry("price")
    if(tests == ""):
        tests == 0
        app.addFlashLabel("Enter the item")
    else:
        app.addTableRow("g1",[test,tests])

app = gui()
app.addLabel("Dash Board")
app.addAutoEntry("item",outp)
app.addEntry("price")
app.addButton("select",billing)
# app.addScrolledTextArea("output")
app.addTable("g1",[["item","Price"]])
app.go()

