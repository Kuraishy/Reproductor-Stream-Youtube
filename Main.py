from GUI import GUI
import pickle
from youtubeAnalizer import youtubeAnalizer
import random


#lista de reproduccion data-------------------------

# TODO: -play selected song
# TODO: -play next song
# TODO: -play previous song
# TODO: repeat one, repeat list, none, random


#intentar encotrar la lista de reproduccion si no hay hacer una nueva--------------------------------

#streamer----------------
tempvar=False
#
#----------------------------------
#INICIACION-------------------------------------------------------------------------------------
try:
    data = pickle.load(open("listaReproduccion.dat", "rb"))  # trata de cargar la lista de reproduccion
    try:
        data.remove(["", ""])  # eliminar la fila temporal
    except:
        pass
except:
    data = [["", ""]]

#construir la G:UI------------------------------------------------------------------------------------
g=GUI(data)

#crear el analizador-------------------------------------------------------------------------------
analizador=youtubeAnalizer()

from YoutubeStreamer import StreamPlayer
stream=StreamPlayer()

#crear list para la playlist

#------------------------------------------------------
def crearPlaylistLocal():
#usando la longitud de la lista saca los url de cada elemento
#y los agrega a la play list
    stream.player.playlist_clear()
    try:
        stream.player.playlist_remove(0)
    except:
        pass
    for x in range(len(data)):
        stream.crearPlaylist(data[x][2])


try:
    crearPlaylistLocal()
except:
    pass

#------------------------------------------------------

def currentPlaying():
    print("PLAYLIST Y LA POSICION")
    print(stream.player.playlist_filenames)
    print(stream.player.playlist_pos)

#----------------------------------------------------
def tableListUpdate():
    g.window['-TABLE-'].update(values=data[:][:])
    pickle.dump(data, open("listaReproduccion.dat", "wb"))
    crearPlaylistLocal()

stream.player.__setattr__('pause',True)

def checarpausa():
    #print(stream.player.__getattr__('pause'))
    if (stream.player.__getattr__('pause')==True):
        g.statusColor = 'Red'
        g.window['-BOTONPAUSA-'].update(button_color=[g.costumColor, g.statusColor])
    else:
        g.statusColor = g.costumBlue
        g.window['-BOTONPAUSA-'].update(button_color=[g.costumColor, g.statusColor])

#eventos de la GUI----------------------------------------------------------------------------------
inf=False

def escribirDatos():
    temp=stream.getPlaylistPos()
    if inf==False:
        try:
            g.window['-DURACION-'].update(data[temp][0])
            g.window['-REPRODUCCIENDO-'].update(data[temp][1])
        except:
            pass
        if temp>0:
            temp2=int(temp)
            g.window.FindElement('-TABLE-').Update(select_rows=(temp2,temp2))
        else:
            g.window.FindElement('-TABLE-').Update(select_rows=(0, 0))


@stream.player.property_observer('time-pos')
def time_observer(_name, value):
    #print(round(value, 1))
    #if value<0:
    try:
        escribirDatos()
    except:
        pass
    g.window['-ACTUAL-'].update((str(value)))






while True:
    event, values = g.window.read()
    if event is None:
        stream.player.terminate()
        raise SystemExit()

        break
    if event=='Agregar':
        data.append(analizador.obtenerdatos(values[0]))
        tableListUpdate()

    if event=='-BOTONPAUSA-':
        stream.pausar_reproducir()
        checarpausa()


    elif event=='Anterior':
        try:
            stream.player.playlist_prev()
        except:
           pass
    elif event=='Siguiente':
        try:
            stream.player.playlist_next()
        except:
            pass
    elif event=='Borrar':
        try:
            data.pop(values['-TABLE-'][0])
            tableListUpdate()
        except:
            pass #seleccion invalida
    elif event=='Aleatorio':
        inf=False
        g.window['-MODO-'].update('Aleatorio')
        random.shuffle(data)
        tableListUpdate()
        stream.player.plalist_pos=0
        stream.pausar_reproducir()
        #currentPlaying()
        try:
            time_observer()
        except:
            pass
    elif event=='_SLIDER_':
        g.window['_VOL_'].update(values['_SLIDER_'])
        stream.setVolumen(values['_SLIDER_'])

    elif event=='Inf':
        inf=True
        g.window['-MODO-'].update('Infinito')
        stream.player.playlist_clear()
        try:
            stream.player.playlist_remove(0)
        except:
            pass

        stream.player.play(data[values['-TABLE-'][0]][2])
        stream.player._loop = True
        g.window['-DURACION-'].update(data[values['-TABLE-'][0]][0])
        g.window['-REPRODUCCIENDO-'].update(data[values['-TABLE-'][0]][1])
        g.window.FindElement('-TABLE-').Update(select_rows=(values['-TABLE-'][0], values['-TABLE-'][0]))

