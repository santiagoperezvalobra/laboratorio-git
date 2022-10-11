from gtts import gTTS
from playsound import playsound

def voz(texto):

    audio = 'audio.mp3'
    language = 'es'
    sp = gTTS(texto, lang=language, slow=False)

    sp.save(audio)
    playsound(audio)
    

if __name__=='__main__':
    voz("hola")
