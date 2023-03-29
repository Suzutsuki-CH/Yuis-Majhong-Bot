from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld
import discord
import numpy as np
import os

# Convert user input to tenhou format
def TenhouGenerate(s):
    S = np.array(list(s))
    sig_index = [-1]+[i for i in range(len(S)) if ord(S[i]) in [115, 112, 109, 122]]

    # [man, sou, pin, honor]
    TenhouArr = [[],[],[],[]]
    man = []
    sou = []
    pin = []
    zi = []

    for i in range(1,len(sig_index)):
        if S[sig_index[i]] == 'm':
            m = S[sig_index[i-1]+1 : sig_index[i]]
            man += list(m)

        if S[sig_index[i]] == 'p':
            p = S[sig_index[i-1]+1 : sig_index[i]]
            pin += list(p)

        if S[sig_index[i]] == 's':
            s = S[sig_index[i-1]+1 : sig_index[i]]
            sou += list(s)

        if S[sig_index[i]] == 'z':
            z = S[sig_index[i-1]+1 : sig_index[i]]
            zi += list(z)

    man.sort()
    sou.sort()
    pin.sort()
    zi.sort()
            
    man = "".join(man)
    sou = "".join(sou)
    pin = "".join(pin)
    zi = "".join(zi)

    return [man, sou, pin, zi]


# Generate image using XeLaTeX
def LaTeX_Generate(s):
    with open('LaTeX/Mahjong.tex','w') as file:
            file.write(r'\documentclass{standalone}'+'\n')
            file.write(r'\usepackage{tikz}'+'\n')
            file.write(r'\usepackage{mahjong}'+'\n\n')

            file.write(r'\begin{document}'+'\n')
            file.write(r'\begin{tikzpicture}'+'\n')
            file.write(r'\draw (0,0) node {\mahjong[%s]{%s}};'%('3cm',s)+'\n')
            file.write(r'\end{tikzpicture}'+'\n')
            file.write(r'\end{document}')

    os.system('"/Users/suzutsuki-ch/bin/xelatex" -interaction=nonstopmode LaTeX/Mahjong.tex;')
    os.system('convert -density 300 Mahjong.pdf -quality 110 LaTeX/Tiles/temp.png;')

# Clean up the auxillary file from latex generation.
def CleanUp():
    os.remove('LaTeX/Tiles/temp.png')
    os.remove('Mahjong.pdf')
    os.remove('Mahjong.log')
    os.remove('Mahjong.aux')
     