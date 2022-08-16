import PySimpleGUI as sg


def CreateWindow(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 14', button_element_size=(6, 2))
    button_size = (6, 2)
    layout = [
        [sg.Text(
            '0',
            font='Franklin 26',
            justification='right',
            expand_x=True,
            pad=(10, 20),
            right_click_menu=theme_menu,
            key='-TEXT-')
         ],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(
            8, size=button_size), sg.Button(9, size=button_size), sg.Button('*', size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(
            6, size=button_size), sg.Button('/', size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(
            2, size=button_size), sg.Button(3, size=button_size), sg.Button('-', size=button_size)],
        [sg.Button(0, expand_x=True), sg.Button(
            '.', size=button_size), sg.Button('+', size=button_size)],
    ]
    return sg.Window('Calculator', icon=r'C:\Users\inico\Desktop\Proyectos\Programas\calculator\images\logo.ico').Layout(layout)


theme_menu = ['menu', ['BlueMono', 'Dark', 'LightGrey1',
                       'DarkGrey12', 'DarkGreen3', 'DarkGreen15', 'Random']]
window = CreateWindow('DarkGrey12')

current_num = []
all_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = CreateWindow(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)

    if event in ['+', '-', '/', '*']:
        all_operation.append(''.join(current_num))
        current_num = []
        all_operation.append(event)
        window['-TEXT-'].update('')

    if event == 'Enter':
        all_operation.append(''.join(current_num))
        result = eval(''.join(all_operation))
        window['-TEXT-'].update(result)
        all_operation = []

    if event == 'Clear':
        current_num = []
        all_operation = []
        window['-TEXT-'].update('')


window.close()
