# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:56:14 2018

@author: humbe
"""
#Author: Humberto Hernandez
#Last updated:  5/14/2018
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from tower_class import tower

from plotting_code_proj import plot_towers
from plotting_code_proj import color
import random

color_rect = '#%02X%02X%02X' % (color(),color(),color())

def coverage(n,width,height,plot = True):
    '''
    
    '''
    assert n > 0, 'Warning! Number of towers must be greater than zero!'
    assert width > 0, 'Warning! Width of coverage area must be greater than 0!'
    assert height > 0, 'Warning! Height of coverage area must be greater than 0!'
#    assert isinstance(plot,bool), 'Warning! plot must be True or False!'
    
    confirmed_towers = 0
    coverage_area = tower((0,0),width,height) #Taking advantage of my tower class method.
    
    valid_towers = []
    plot_list = []
    
    attempt = 0
    print 'len(valid_towers): ', len(valid_towers)
    while confirmed_towers < n:
        
        print 'attempt: ', attempt
        x_rand = np.random.randint(width, size = 1)
        y_rand = np.random.randint(height, size = 1)
        x = x_rand[0]
        y = y_rand[0]
        
        width_rand = np.random.randint(1,width+1, size = 1) #Have to be careful about half-open interval
        height_rand = np.random.randint(1,height+1, size = 1)
        tower_width = width_rand[0]
        tower_height = height_rand[0]
        ###
        t = tower((x,y),tower_width,tower_height)
        
        #Check if newly generated tower is contained in main coverage area.
        test = t.contained(coverage_area)
        valid = 1
        for check in test:
            if check == False:
                valid = 0
                
        failed = 0        
        for t_i in valid_towers:
            checks = t.contained(t_i)
            for check in checks:
                if check == True:
                    failed += 1
            if failed == 4:
                print 'Failed!'
                valid = 0
            failed = 0
                
        failed = 0        
        for t_i in valid_towers:
            checks = t_i.contained(t)
            for check in checks:
                if check == True:
                    failed += 1
            if failed == 4:
                print 'Failed!'
                valid = 0
            failed = 0
                
                
                    
        #If it's in the coverage area, proceed.
        if valid == 1:
            #Plotting newly generated tower.
            if plot:
                plot_t = [t,None,'/',False]
                plot_list.append(plot_t)
                plot_towers(plot_list,width,height)
                plt.pause(3)
                plt.close()
            print 'Coming in: ',t
            #If the tower generated is equal to the coverage area, then we are done.
            if (len(valid_towers) == 0) and (t == coverage_area):
                valid_towers.append(t)
                print 'Valid_towers: ', valid_towers
                return list_of_towers
            elif len(valid_towers) == 0:
                valid_towers.append(t)
                if plot:
                    plot_list.pop()
                    color_rect = '#%02X%02X%02X' % (color(),color(),color())
                    plot_list.append([t,color_rect,None,True])
                confirmed_towers += 1
            else:
                truncate_list = []
                print truncate_list
                for tow in valid_towers:
                    if any(t.corner(tow)) or any(t.borders(tow)):
                        truncate_list.append(tow)
                        print truncate_list
                        
                #if len(truncate_list) != 0        
                truncated = t.truncate(valid_towers) #Was valid towers
                if truncated != None:   
                    print 'Going out: ', truncated
                    if plot:
                        plot_list.pop()
                        color_rect = '#%02X%02X%02X' % (color(),color(),color())
                        plot_list.append([truncated,color_rect,None,True])
                    confirmed_towers += 1
                    valid_towers.append(t)
                else:
                    if plot:
                        plot_list.pop()
                    print "Truncated is None!"
                if plot:    
                    plt.close()
                    
        attempt += 1

    return valid_towers, plot_list
            #print 'did you see me?'            
            
#        
#        #Now that we know it is within the bounds of the desired coverage area
#        #we can proceed.
#        if within_bounds:                         
#            
#            if len(list_of_towers) == 0:
#                list_of_towers.append
#            
#            confirmed_towers += 1
#        
valid_towers, plot_list = coverage(10,100,100)      

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
