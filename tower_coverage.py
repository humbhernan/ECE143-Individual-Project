#Author: Humberto Hernandez
#Last updated:  5/19/2018 7:30pm
import numpy as np
from tower_class import tower

from plotting_code_proj import plot_towers
from plotting_code_proj import color

def coverage_up_to_n(n,width,height,plot = True, interval = 3):
    '''
    Takes in an amount of towers and a desired coverage area described by a
    height and width and returns a list of randomly generated towers
    to populate the desired coverage area.
    
    Parameter: n
    Type: int
    
    Parameter: width
    Type: int
    
    Parameter: height
    Type: int    
    
    Parameter: plot
    Type: bool
    
    Parameter: interval
    Type: int  
    
    Return:
        - list of towers that populate the coverage area.
        - list of towers that populate the coverage area in a format compatible
            with the function plot_towers().
        - Returns a tuple containing the desired coverage versus the resulting
            coverage given n towers. (desired_area,actual_area)
    e.g.
    >>> valid_towers, plot_list = coverage(10,100,100)
    >>> valid_towers
    [tower((30, 0),15,59),
     tower((7, 1),23,21),
     tower((45, 34),33,44),
     tower((49, 22),2,12),
     tower((15, 32),15,64),
     tower((19, 26),11,6),
     tower((2, 27),13,13),
     tower((53, 78),24,16),
     tower((30, 79),23,12),
     tower((15, 22),2,10)]
    >>> plot_list       
    [[tower((30, 0),15,59), '#56C8D0', None, True],
    [tower((7, 1),23,21), '#1968E5', None, True],
    [tower((45, 34),33,44), '#D23EEB', None, True],
    [tower((49, 22),2,12), '#DFA7A8', None, True],
    [tower((15, 32),15,64), '#A4011A', None, True],
    [tower((19, 26),11,6), '#D47484', None, True],
    [tower((2, 27),13,13), '#58D79F', None, True],
    [tower((53, 78),24,16), '#0E7345', None, True],
    [tower((30, 79),23,12), '#B8131C', None, True],
    [tower((15, 22),2,10), '#239036', None, True]]
    
    
    Assertions:
        - Number of towers (n) must be a positive number.
        - n must be an integer.
        - width must be a positive number
        - width must be an integer.
        - height must be a positive number
        - height must be an integer.   
        - plot must be a boolean, True or False
        - interval must be a positive number
        - interval must be an integer.          
        
    Takes an amount of towers and desired coverage region and randomly generates
    those towers to populate that region. You can opt to watch the attempts take
    place in real time by changing the plot value to True. It will then plot the values
    as time goes on. The variable interval designates the amount of time between plots.
    It starts by generating a random tower with random (x,y) coordinate of the lower
    left corner, a random height and random width. Once the tower is generated
    we check if it's a valid candidate for processing by making sure it is bound
    by the desired coverage region defined by the user. We do this by creating a
    tower that has the dimensions of the whole region. We can then run the contained
    method to see if the randomly generated tower is bound within the desired coverage
    area.
    
    If the current list of valid towers is empty, we add the randomly generated
    into the list.
    
    If it isn't, we makes sure that it isn't completely contained inside any of
    the already established towers, or that our new tower doesn't consume the 
    entirety of the established towers.
    
    Once we have gone through those steps than the tower is valid and we can proceed.
    
    To speed up processing, we only truncate the new tower against towers that it
    overlaps with, which we check with the contained and borders method. If it doesn't
    overlap with any, then we can just add it to the valid tower list.
    
    If there is no valid truncated version of the tower than we toss it out and try
    again. If there is one, we can add it to the valid tower list.
    
    It does this over and over until the confirmed amount of towers is equal to
    the amount of towers asked by the user.
    
    Once we have found all the towers we are finished.
    
    In the plotting mode, it will show the attempted new tower as a slash-box.
    Then it will get replaced with a colored truncated version.
    
    Assertions:
        - n must be a positive integer greater than zero.
        - width must be a positive integer greater than zero.
        - height must be a positive integer greater than zero.
        - plot must be a boolean, True or False
        - interval must be a positive integer greater than zero.
    '''
    assert n > 0, 'Warning! Number of towers must be greater than zero!'
    assert isinstance(n,int), 'Warning! Number of towers must be an integer!'
    assert width > 0, 'Warning! Width of coverage area must be greater than 0!'
    assert isinstance(width,int), 'Warning! Width must be an integer!'
    assert height > 0, 'Warning! Height of coverage area must be greater than 0!'
    assert isinstance(height,int),'Warning! Height must be an integer!'
    assert isinstance(plot,bool), 'Warning! plot must be True or False!'
    assert interval > 0, 'Warning! Interval must be greater than zero!'
    assert isinstance(interval,int), 'Warning! Interval must be an integer!'
    
    print 'Computing...'
    confirmed_towers = 0
    coverage_area = tower((0,0),width,height) #Taking advantage of my tower class method.
    
    valid_towers = []
    plot_list = []
    
    desired_area = width * height
    
    while confirmed_towers < n:
        
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
        if all(test) != True:
            valid = 0
                
        
        if len(valid_towers) != 0:
            #Checking to see if newly generated tower is inside any of the
            #already established towers.
            for t_i in valid_towers:
                checks = t.contained(t_i)
                if all(checks) == True:
                    valid = 0
            #Checking to see if any of my established towers are inside of mu
            #newly generated tower.
            for t_i in valid_towers:
                checks = t_i.contained(t)
                if all(checks) == True:
                    valid = 0
                    
        #Now that we have validated the new tower, we can proceed.
        if valid == 1:
            #Plotting newly generated tower.
            if plot:
                plot_t = [t,None,'/',False]
                plot_list.append(plot_t)
                plot_towers(plot_list,width,height)
                plt.pause(interval)
                plt.close()
            #If the tower generated is equal to the coverage area, then we are done.
            if (len(valid_towers) == 0) and (t == coverage_area):
                valid_towers.append(t)
                return list_of_towers, plot_list
            elif len(valid_towers) == 0:
                valid_towers.append(t)
                if plot:
                    plot_list.pop()
                    color_rect = '#%02X%02X%02X' % (color(),color(),color())
                    plot_list.append([t,color_rect,None,True])
                confirmed_towers += 1
            else:
                truncate_list = []
                for tow in valid_towers:
                    if any(t.corner(tow)) or any(t.borders(tow)):
                        truncate_list.append(tow)
                        
                if len(truncate_list) != 0:        
                    truncated = t.truncate(truncate_list) #Was valid towers
                    if truncated != None:   
                        if plot:
                            plot_list.pop()
                            color_rect = '#%02X%02X%02X' % (color(),color(),color())
                            plot_list.append([truncated,color_rect,None,True])
                        confirmed_towers += 1
                        valid_towers.append(truncated)
                    else:
                        if plot:
                            plot_list.pop()
                        
                else:
                    if plot:
                        plot_list.pop()
                        color_rect = '#%02X%02X%02X' % (color(),color(),color())
                        plot_list.append([t,color_rect,None,True])
                    confirmed_towers += 1
                    valid_towers.append(t)
                if plot: 
                    if confirmed_towers == n:
                        plot_towers(plot_list,width,height)    
                        
        actual_area = 0
        for coverage in valid_towers:
            actual_area = actual_area + coverage.area
        
        if (actual_area == desired_area):
            print "Coverage area has been filled!"
            break
        
    print 'Desired area: ', desired_area
    print 'Actual area: ', actual_area


    return valid_towers, (desired_area,actual_area), plot_list 

def average_towers_for_coverage(iterations,width,height):
    '''
    Takes in an amount of iterations and a desired coverage area described by a
    height and width and returns the average amount of towers needed to fully
    populate the desired coverage area.
    
    Parameter: iterations
    Type: int
    
    Parameter: width
    Type: int
    
    Parameter: height
    Type: int    
    
    Return:
        - Returns the average for the number of iterations asked for by the user.
    e.g.
    
    Assertions:
        - iterations must be a positive number.
        - iterations must be an integer.
        - width must be a positive number
        - width must be an integer.
        - height must be a positive number
        - height must be an integer.            
        
    Takes an amount of iterations and desired coverage region and randomly generates
    those towers to populate that region. 

    It starts by generating a random tower with random (x,y) coordinate of the lower
    left corner, a random height and random width. Once the tower is generated
    we check if it's a valid candidate for processing by making sure it is bound
    by the desired coverage region defined by the user. We do this by creating a
    tower that has the dimensions of the whole region. We can then run the contained
    method to see if the randomly generated tower is bound within the desired coverage
    area.
    
    If the current list of valid towers is empty, we add the randomly generated
    into the list.
    
    If it isn't, we makes sure that it isn't completely contained inside any of
    the already established towers, or that our new tower doesn't consume the 
    entirety of the established towers.
    
    Once we have gone through those steps than the tower is valid and we can proceed.
    
    To speed up processing, we only truncate the new tower against towers that it
    overlaps with, which we check with the contained and borders method. If it doesn't
    overlap with any, then we can just add it to the valid tower list.
    
    If there is no valid truncated version of the tower than we toss it out and try
    again. If there is one, we can add it to the valid tower list.
    
    It does this over and over until the confirmed amount of towers is equal to
    the amount of towers asked by the user.
    
    Once we have found all the towers we are finished and we go to the next iteration.
    It does this until all the iterations are done.
    
    
    
    Assertions:
        - iterations must be a positive integer greater than zero.
        - width must be a positive integer greater than zero.
        - height must be a positive integer greater than zero.

    '''
    assert iterations > 0, 'Warning! Number of iterations must be greater than zero!'
    assert isinstance(iterations,int), 'Warning! Number of iterations must be an integer!'
    assert width > 0, 'Warning! Width of coverage area must be greater than 0!'
    assert isinstance(width,int), 'Warning! Width must be an integer!'
    assert height > 0, 'Warning! Height of coverage area must be greater than 0!'
    assert isinstance(height,int),'Warning! Height must be an integer!'
    
    print 'Computing...'
    confirmed_towers = 0
    coverage_area = tower((0,0),width,height) #Taking advantage of my tower class method.
    
    desired_area = width * height
    counter = 0
    number_of_towers = []
    
    while counter < iterations:
        actual_area = 0
        valid_towers = []
        while actual_area != desired_area:
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
            if all(test) != True:
                valid = 0
                    
            
            if len(valid_towers) != 0:
                #Checking to see if newly generated tower is inside any of the
                #already established towers.
                for t_i in valid_towers:
                    checks = t.contained(t_i)
                    if all(checks) == True:
                        valid = 0
                #Checking to see if any of my established towers are inside of mu
                #newly generated tower.
                for t_i in valid_towers:
                    checks = t_i.contained(t)
                    if all(checks) == True:
                        valid = 0
                        
            #Now that we have validated the new tower, we can proceed.
            if valid == 1:
                #If the tower generated is equal to the coverage area, then we are done.
                if (len(valid_towers) == 0) and (t == coverage_area):
                    valid_towers.append(t)
                    return list_of_towers, plot_list
                elif len(valid_towers) == 0:
                    valid_towers.append(t)
                    confirmed_towers += 1
                else:
                    truncate_list = []
                    for tow in valid_towers:
                        if any(t.corner(tow)) or any(t.borders(tow)):
                            truncate_list.append(tow)
                            
                    if len(truncate_list) != 0:        
                        truncated = t.truncate(truncate_list) #Was valid towers
                        if truncated != None:   
                            confirmed_towers += 1
                            valid_towers.append(truncated)                        
                    else:
                        confirmed_towers += 1
                        valid_towers.append(t)  
                            
            actual_area = 0
            for coverage in valid_towers:
                actual_area = actual_area + coverage.area
            
            if (actual_area == desired_area):
                print 'Iteration: %d. Desired coverage area has been filled!' % (counter+1)
                break
            
        number_of_towers.append(len(valid_towers))
        counter += 1
    
    summation = float(sum(number_of_towers))
    average = summation / len(number_of_towers)
    
    print "Number of iterations: ", iterations
    print "Average: ", average    
    
    return average
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
