import pafy

#creacion de tabla de 2x2


#inicializador de clase
class youtubeAnalizer:

    #obtener los datos del video
    def obtenerdatos(self,url):
        temp=pafy.new(url)
        return [temp.duration,temp.title,url]

