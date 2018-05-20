from appJar import gui

class MyApplication():
     
     
    def Prepare(self, app):
            # Form GUI
            app.starSubWindow("LOGIN",modal=True)
            # Add labels & entries
            # in the correct row & column
            app.addLabel("userLab", "Username:", 0, 0)
            app.addEntry("username", 0, 1)
            app.addLabel("passLab", "Password:", 1, 0)
            app.addSecretEntry("password", 1, 1)
            app.addButtons( ["Submit", "Cancel"] ,self.Submit, "app.hidesubWindows",colspan=2)

            return app

    def Start(self):
            # Creates a UI
            app = gui()

            # Run the prebuild method that adds items to the UI
            app = self.Prepare(app)

            # Make the app class-accesible
            self.app = app

        # Start appJar
            app.go()

    def Submit(self, btnName):
            if btnName == "Submit":
                username = self.app.getEntry("username")
                password = self.app.getEntry("password")

                # Very stupid login system (both strings equal to ourcodeworld)
                if username and password == "ourcodeworld":
                    self.app.infoBox("Logged in", "You are now logged in !")
                    
                else:
                    self.app.errorBox("Error", "Your credentials are invalid !")


# def login(btn):
#     app.hideSubWindow("Login")
#     app.show()

# app.startSubWindow("Login")
# app.addLabel("l2", "Login Window")
# app.addButton("SUBMIT", login)
# app.stopSubWindow()

# app.go(startWindow="Login")


if __name__ == '__main__':
    # Create an instance of your application
    App = MyApplication()
    # Start your app !
    App.Start()