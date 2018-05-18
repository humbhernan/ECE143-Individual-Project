# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:54:59 2018

@author: humbe
"""
from tower_class import tower
import random

color = lambda: random.randint(0,255)
color_rect = '#%02X%02X%02X' % (color(),color(),color())

def plot_towers(towers,width,height):
    '''
    Takes in a list of towers describing there facecolor and hatch type and returns
    a single plot with them on it.
    
    Parameters:
        - towers is a lists of lists, where each sub list contains a tower object,
            facecolor in RGB-hexadecimal format, and hatch type, and fill.
            
            e.g. [tower((1,1),2,3), #0000ff, '-', True]
            
        - width and height describe the bounds of the plotting area. In reference
            to this project, it describes the individual plotting area.
        - rgb color must be in the following format 
            #xxxxxx, where x is a number ranging from 0-9 or a letter ranging from
            a-f.
        - fill determines whether a towers box has color or is transparent. Can be
            True or False. True for color, False for transparent.
        
    Type: 
        - towers: list
        - width:  int
        - height: int
    
    Note: - Imports the matplotlib module as well as the patches module. Makes use
            of the Rectangle class to create the coverage area of each tower.
          - Requires the tower class.  
    
    Example:
        t2_top = tower((2,6),4,3)
        t1 = tower((2,2),4,6)
        t3 = t2_top.truncate([t1]) 
        towers = [[t2_top, '#0000ff', None],[t1,None, None],[t3, None, '-']]    
        plot_towers(towers,10,10)
        
    RGB color examples:
        Silver - #C0C0C0
        Gray   - #808080
        Black  - #000000
        Red    - #FF0000
        Maroon - #800000
        Yellow - #FFFF00
        Olive  - #808000
        Lime   - #00FF00
        Green  - #008000
        Aqua   - #00FFFF
        Teal   - #008080
        Blue   - #0000FF
        Navy   - #000080
        Fuchsia- #FF00FF
        Purple - #800080
        
    Hatch types:
        '/'  - diagonal hatching
        '\\' - back diagonal
        '-'  - horizontal
        '+'  - crossed
        'x'  - crossed diagonal
        'o'  - small circle
        'O'  - large circle
        '.'  - dots
        '*'  - stars
        
    Assertions:
        - width and height must be greater than zero.
        - width and height must be integer type.
        - Argument towers must be type list.
        - Argument towers must be a non-empty list.
        - sub-lists in towers must be a list.
        - First item in sublist must be a tower object.
        - Second item in sublist must be a rgb-hex color
        - color must be in rgb-hex format: #xxxxxx, where x is a number from
            0-9 or a letter ranging from a - f.
        - Third item must be a hatch type from the hatch types in the function
            documentation.        
        - Fourth item is the fill, must be True or False.
        
    '''
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    
    assert (isinstance(width,int)) and width > 0,'plot_towers: Width must be an integer greater than zero!'
    assert (isinstance(height,int)) and height > 0,'plot_towers: Height must be an integer greater than zero!'
    assert isinstance(towers,list),'plot_towers: Must submit tower list!'
    assert len(towers) > 0, 'plot_towers: towers list must be greater than 0!'
    
    for tower_packet in towers:
        assert len(tower_packet) == 4, 'plot_towers: Sub_lists can only be length of three.'
 
    acceptable_characters = ['0','1','2','3','4','5','6','7','8','9',
                             'A','B','C','D','E','F','a','b','c','d','e','f','#']
    
    acceptable_hatch = ['/','\\','-', '+','x','o','O','.','*']
    
    #Checking to make sure sublist is valid.
    for t,color,hatch,fill in towers:
        assert isinstance(t,tower), 'plot_towers: Warning! First item in the list must be of class tower!'
        assert isinstance(fill,bool), 'plot_towers: fill must be True or False.'
        
        if color != None:
            characters = list(color)
            assert len(characters) == 7,'plot_towers: Warning! Hexadecimal number must be in the #XXXXXX format' 
            assert characters[0] == '#', 'plot_towers: Warning! Not a Hexadecimal number! Format must be #XXXXXX.'
            #Checking that the string is an actual hexadecimal number.
            valid = 0
            for char in characters:
                for ac_char in acceptable_characters:
                    if(ac_char == char):
                        valid = 1
                assert valid > 0, 'plot_towers: Warning! Not a valid hexadecimal number!, %s' % char
                valid = 0
        else:
            assert color == None,'plot_towers: color must be either None or RGB-hexadecimal number!'
        
        if hatch != None:
            valid = 0
            for h in acceptable_hatch:
                if h == hatch:
                    valid = 1
            assert valid == 1,'plot_towers: Hatch must be from acceptable list in documentation.'
        else:
            assert hatch == None, 'plot_towers: hatch must be either from acceptable list in documentation or None'

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0,width)
    ax.set_ylim(0,height)
    plt.grid()
    plt.show()
    
    for t,color,hatch,fill in towers:        
        ax.add_patch(patches.Rectangle(t.coord_ll,t.width,t.height,facecolor = color, hatch = hatch, Fill = fill))

             
