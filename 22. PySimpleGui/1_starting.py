import PySimpleGUI as sg

sg.theme('DarkTanBlue')

layout = [[sg.Text('Nombre completo:'), sg.Input(key="CLIENT", do_not_clear=False)],
          [sg.Text('Edad:'), sg.Input(key='AGE', do_not_clear=False)],
          [sg.Text('Correo:'), sg.Input(key='EMAIL', do_not_clear=False)],
          [sg.Text('Contraseña:'), sg.Input(
              key='PASSWORD', do_not_clear=False)],
          [sg.Button('Enviar'), sg.Exit('Cancelar')]
          ]

window = sg.Window('Registro de clientes', layout,
                   element_justification="right")

while True:
    event, values = window.read()
    if event == 'Enviar':
        client_name = values["CLIENT"]
        sg.popup("File saved",
                 f"File has been saved here: \nmi primer valor:{client_name}")

    elif event == 'Cancelar' or event == sg.WIN_CLOSED:
        print('el programa se cierra')
        break

window.close()
