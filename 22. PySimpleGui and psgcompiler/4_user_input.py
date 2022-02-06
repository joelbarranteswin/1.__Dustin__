import PySimpleGUI as sg

# Add some color
# to the window
sg.theme('SandyBeach')

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
    [sg.Text('Please enter your Name, Age, Phone',
             text_color='green', background_color='#FF0000',
             size=50, pad=((0, 0), (10, 10)))],
    [sg.Text('Name', size=(15, 1), tooltip='Please enter your Name'),
     sg.InputText()],
    [sg.Text('Age', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone', size=(15, 1)), sg.InputText()],
    [sg.Submit(pad=((0, 15), (20, 10))), sg.Cancel(pad=((15, 0), (20, 10)))]
]

# El pad de cada commando tiene como refencia la justificacion del elemento
window = sg.Window('Simple data entry window', layout,
                   element_justification="center", size=(300, 200), margins=(0, 0))
event, values = window.read()
window.close()

# The input data looks like a simple list
# when automatic numbered
print(event, values[0], values[1], values[2])
