import PySimpleGUI as sg

sg.theme('SandyBeach')

layout = [[sg.Text('Stopwatch', size=(20, 2), justification='center')],
          [sg.Text(size=(10, 2), font=('Arial', 20),
                   justification='center', key='-OUTPUT-')],
          [sg.T(' ' * 5), sg.Button('Start / Stop', focus=True), sg.Quit()]]  # sg.TIMEOUT_KEY

window = sg.Window('Stopwatch Timer', layout)

timer_running, counter = True, 0

# Event Loop
while True:

    # Please try and use as high of a timeout value as you can
    event, values = window.read(timeout=10)

    # if user closed the window using X or clicked Quit button
    if event in (None, 'Quit'):
        break
    elif event == 'Start / Stop':
        timer_running = not timer_running
    if timer_running:
        window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60,
                                                                (counter // 100) % 60, counter % 100))
        counter += 1
window.close()
