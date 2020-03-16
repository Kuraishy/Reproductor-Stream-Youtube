import PySimpleGUI as Sg

class GUI:
    # theme
    Sg.theme('DarkBlue')
    # table elements
    headings = ['duracion', ' titulo']
    window=Sg.Window("temp")

    # TODO: -play selected song
    # TODO: -play next song
    # TODO: -play previous song
    # TODO: repeat one, repeat list, none, random
    costumBlue='#355166'
    costumColor='#D8E5F7'

    statusColor='Red'


# actual/duracion       reproducciendo: fdsf        modo:random
    def __init__(self,data):
        layout = [[Sg.Text(text='100',key='_VOL_'),Sg.Text(text='actal',key='-ACTUAL-'),Sg.Text(text='/'),Sg.Text(text='duracion',key='-DURACION-'),
                   Sg.Text(text='reproducciendo',key='-REPRODUCCIENDO-',auto_size_text=True,size=(40,1)),Sg.Text(text='Aleatorio',key='-MODO-')],

                  [Sg.Slider((1, 200), key='_SLIDER_', orientation='v', enable_events=True, disable_number_display=True, size=(15, 10), default_value=100),
                   Sg.Table(values=data[:][:], headings=self.headings, max_col_width=50,enable_events=True, hide_vertical_scroll=True,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='left',
                            num_rows=20,
                            # alternating_row_color='lightyellow',
                            key='-TABLE-',
                            tooltip='This is a table')],
                  [Sg.Button(button_text='Play/Pause',button_color=[self.costumColor,self.statusColor],key='-BOTONPAUSA-'), Sg.Button(button_text='Aleatorio',button_color=[self.costumColor,self.costumBlue]),Sg.Button(button_text='Anterior',button_color=[self.costumColor,self.costumBlue]),Sg.Button(button_text='Siguiente',button_color=[self.costumColor,self.costumBlue]), Sg.Button(button_text='Inf',button_color=[self.costumColor,self.costumBlue]) ],
                  [Sg.InputText(''), Sg.Button(button_text='Agregar',button_color=[self.costumColor,self.costumBlue]),Sg.Button(button_text='Borrar',button_color=[self.costumColor,self.costumBlue])]]

        # ------ Create Window ------
        self.window = Sg.Window('The Table Element', layout, size=(600, 570))


        # ------ BINDS ------
