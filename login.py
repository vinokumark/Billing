from appJar import gui
count = 0
# handle button events
def press():
    global count
    app.addEntry("b1" + str(count))
    app.addEntry("b2" + str(count))
    count += 1

def calculate():
    quantity = app.getEntry("b2")
    price = app.getEntry("price")
    y = (quantity + price)
    print(y)
    print(price)
    print(quantity)

with gui() as app:
    app.button("ADD ITEM", press,0,3)
    app.addLabel("l1","item",0,0)
    app.addLabel("l2","quantity",0,1)
    app.addEntry("b1")
    app.addEntry("b2")
    app.addEntry("price")
    app.button("Calculate",calculate)