import PySimpleGUI as sg

sg.theme("DarkBlue")
sg.set_options(font=('Courier New', 12))

frame_1 = [[sg.Text('Day 1')], [sg.Checkbox('Time 1')],
           [sg.Checkbox('Time 2')], ]
frame_2 = [[sg.Text('Day 2', pad=(3, (12, 3)))], [
    sg.Checkbox('Time 1')], [sg.Checkbox('Time 2')], ]

layout = [
    [sg.Frame('Week 1', frame_1, pad=(0, 5)),
     sg.Frame('', frame_2, pad=(0, (14, 5)), key='Hide')],
    [sg.Submit(), sg.Cancel()],
]

window = sg.Window('Testing Window', layout, finalize=True)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event, values)

window.close()
