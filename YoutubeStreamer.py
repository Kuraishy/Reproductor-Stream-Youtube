import mpv
#from Main import actualizarDuracion



class StreamPlayer:
    player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True,video=False)

    audio_pausado=True
    volumen=100
    player.volume=volumen
    player.__setattr__('pause', audio_pausado)
    player.loop_playlist = 'inf'

   # print(player.playlist)
    def __init__(self):

        self.player.playlist_pos = 0



    #pausar o reproducir-----------------------------------------------------------------
    def pausar_reproducir(self):
       self.player.pause=False
       if (self.audio_pausado):
           self.audio_pausado = False
           self.player.__setattr__('pause', False)
       else:
           self.audio_pausado = True
           self.player.__setattr__('pause', True)




    def volumenReproducto(self,vol):
        self.player.__setattr__('volume',vol)

    def tiempoActual(self):
        @self.player.property_observer('time-pos')
        def time_observer(_name, value):
            pass
            #print(round(value, 1))


    def crearPlaylist(self,list):
        self.player.playlist_append(list)







    def tocarSiguiente(self):
        self.player.playlist_next()
    def tocarAnterior(self):
        self.player.playlist_prev()
    def modoDeReproduccion(self,modo):
        self.player.loop_playlist='inf'
    def setVolumen(self,vol):
        self.player.volume=vol
    def getPlaylistPos(self):
        return self.player._get_property("playlist-pos")



#while True:
    # To modify the playlist, use player.playlist_{append,clear,move,remove}. player.playlist is read-only
    # print(player.playlist)
    # player.wait_for_playback()