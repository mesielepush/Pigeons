
import pygame
import os
import time
from psychopy.sound import Sound

pygame.init()

########################################################################
######################  SOUNDS
########################################################################

def note(value='e',secs=0.3,octave=3,vol=0.07):
    Sound(value=value,secs=secs,octave=octave,volume=vol).play()
def beep():
    note('c',secs=0.4,octave=3,vol=0.08)
    time.sleep(0.2)
    note('d',secs=0.3,octave=3,vol=0.05)
    time.sleep(0.2)
    note('g',secs=0.4,octave=3,vol=0.05)
    note('g',secs=0.3,octave=4,vol=0.05)
    note('d',secs=0.4,octave=3,vol=0.05)
    note('c',secs=0.3,octave=4,vol=0.05)
    time.sleep(1)
def boop():
    note('a',secs=0.4,octave=3,vol=0.08)
    note('f',secs=0.4,octave=4,vol=0.05)
    note('d',secs=0.4,octave=4,vol=0.05)
    note('c',secs=0.4,octave=3,vol=0.05)
    time.sleep(0.4)
    note('g',secs=0.4,octave=3,vol=0.08)
    note('g',secs=0.4,octave=4,vol=0.05)
    note('d',secs=0.4,octave=4,vol=0.05)
    note('f',secs=0.4,octave=3,vol=0.05)
    time.sleep(0.4)
    note('c',secs=0.4,octave=3,vol=0.08)
    note('e',secs=0.4,octave=4,vol=0.05)
    note('g',secs=0.4,octave=4,vol=0.05)
    note('b',secs=0.4,octave=3,vol=0.05)
    time.sleep(0.4)
    note('a',secs=0.6,octave=3,vol=0.08)
    note('f',secs=0.6,octave=4,vol=0.05)
    note('d',secs=0.6,octave=3,vol=0.05)
    note('c',secs=0.6,octave=4,vol=0.05)
    time.sleep(0.9)
    note('d',secs=0.6,octave=3,vol=0.08)
    time.sleep(0.6)
    note('a',secs=0.6,octave=3,vol=0.08)
    time.sleep(0.6)
    note('d',secs=0.6,octave=3,vol=0.08)
    time.sleep(0.6)
    note('a',secs=0.6,octave=4,vol=0.08)
    time.sleep(0.6)
    time.sleep(1)

pygame.mixer.init(channels=2)
cha1=pygame.mixer.Channel(0)
cha2=pygame.mixer.Channel(1)
cha3=pygame.mixer.Channel(2)

bg_noise  = pygame.mixer.Sound(r'.\sounds\VIENTO.ogg')
insound   = pygame.mixer.Sound(r'.\sounds\intro1_01.ogg')
ch_sound  = pygame.mixer.Sound(r'.\sounds\choose.ogg')
ONIN      = pygame.mixer.Sound(r'.\sounds\tonito.wav')
gases     = pygame.mixer.Sound(r'.\sounds\gases.ogg')
arr       = pygame.mixer.Sound(r'.\sounds\arr.ogg')
slip      = pygame.mixer.Sound(r'.\sounds\slip.ogg')
moneda    = pygame.mixer.Sound(r'.\sounds\moneda.ogg')
off       = pygame.mixer.Sound(r'.\sounds\turn_off.ogg')

bg_noise.set_volume(1.5)
insound.set_volume(0.25)
ONIN.set_volume(0.5)
gases.set_volume(0.2)
arr.set_volume(0.4)
slip.set_volume(0.4)

########################################################################
######################  IMAGES
########################################################################

white   = (255,255,255)
red     = (255,0,0)
apagado = pygame.image.load(r'.\img\apagado.png')
iconin  = pygame.image.load(r'.\img\ICONO.png')
intbg2  = pygame.image.load(r'.\img\Pigeonscorp.png')
bachoo  = pygame.image.load(r'.\img\CHOOSE.png')
niveles = pygame.image.load(r'.\img\CHOOSI.png')
botpig  = pygame.image.load(r'.\img\pichion.png')
botpen  = pygame.image.load(r'.\img\pensador.png')
bothum  = pygame.image.load(r'.\img\humano.png')
bothiper= pygame.image.load(r'.\img\hiper.png')
p1      = pygame.image.load(r'.\img\PINI.png')
p2      = pygame.image.load(r'.\img\PIZQ.png')
p3      = pygame.image.load(r'.\img\PDER.png')
p4      = pygame.image.load(r'.\img\P1Pellet.png')
p5      = pygame.image.load(r'.\img\P2Pellet.png')
bg      = pygame.image.load(r'.\img\back.png')
lab     = pygame.image.load(r'.\img\lab.png')
bizq    = pygame.image.load(r'.\img\bizq.png')
bder    = pygame.image.load(r'.\img\bder.png')
off_p   = pygame.image.load(r'.\img\off_p.png')
pygame.display.set_icon(iconin)
os.system('cls')
