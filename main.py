import pygame, mido, os
from colorama import init
init()

pygame.mixer.init()

def col(ft, s):
    """For printing text with colors.
    
    Uses ansi escape sequences. (ft is "first two", s is "string")"""
    # black-30, red-31, green-32, yellow-33, blue-34, magenta-35, cyan-36, white-37
    u = '\u001b'
    numbers = dict([(string,30+n) for n, string in enumerate(('bl','re','gr','ye','blu','ma','cy','wh'))])
    n = numbers[ft]
    return f'{u}[{n}m{s}{u}[0m'

def play_music(path ):
  '''Stream music_file in a blocking manner'''
  clock = pygame.time.Clock()
  pygame.mixer.music.load(path)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    clock.tick(30) # check if playback has finished

def clichoose(options, color='ye'):
    while True:
        print('\n'.join([f'{col("ye", str(n)+".")} {o}' for n, o in enumerate(options)]))
        print('-'*10)
        i = input('> ')
        try:
            options[int(i)]
        except:
            print(col('re', 'invalid'))
        else:
            c = options[int(i)]
            print(col('gr', c))
            return c

while True:
    c = clichoose([f for f in os.listdir() if f.endswith('.mid')])
    play_music(c)
