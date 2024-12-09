import PySimpleGUI as psgui

filters = {
    'sunglasses' : 'sunglasses.jpg',
    'mustache' : 'mustache.jpg',
    'hearts blush' : 'heartsBlush.jpg'
}

'''
### UNIMPLEMENTED UI -- click a button to apply a filter on webcam display ###
class filterButtons():
    def __init__(self, filterName, imgName):
        self.fname = filterName
        self.img = imgName

    def applyFilter(self):
        return self.img
'''

def requestEmail():
    initLayout = [ [psgui.Text("Please enter your email:")], [psgui.InputText()], [psgui.Button('Ok'), psgui.Button('Cancel')] ]
    window = psgui.Window('Welcome to Photobooth :D', initLayout)

    while True:
        event, values = window.read()

        if event == psgui.WIN_CLOSED or event == 'Cancel':
            break
        return values[0]

    window.close()