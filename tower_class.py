# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:28:20 2018

@author: humbe
"""
#Author: Humberto Hernandez
#Last Updated: 5/17/2018 6:40pm

class tower(object):
    '''
    Produces a tower object.
    
    Attributes:
        - self.coord_xx = (x,y), where xx is the subscript corresponding to a corner
            of the tower's coverage area.
            - ll means lower left corner.
            - lr means lower right corner.
            - tl means top left corner.
            - tr means top right corner.
        - self.width = Width of coverage area.
        - self.height = Height of the coverage area.
        - self.area = Area of coverage area.

    Attribute Type:
        - self.coord_xx is a tuple of size two with integer arguments corresponding
            to the (x,y) location of that corner.
                e.g. self.coord_ll = (0,0)
        - self.width is type int.
        - self.height is type int.
        - self.area is type int.
        
    Methods:
        - coord_lr(),coord_tl(),coord_tr() give corresponding (x,y) coordingates
            for specified corner. These are methods that have property decorators
            so they can be referenced by the user as attributes.
        - __eq__: Checks whether two towers are equivalent to each other.
        - __repr__:  Returns the string representation of tower object.
        - contained(): Checks which corners of a tower are contained in another
                        tower's coverage area.
        - corner(): Checks which corners of a tower are contained in another
            tower's coverage area.
        - overlap(): Returns sub-tower with largest overlap with other.
        - truncate(): Takes in a tower and a list of towers and truncates the
                        tower versus that list. 
        - borders(): Checks which walls of a tower overlap another tower's
                        coverage area.
        - subtowers(): Returns a list of a possible sub-towers for a given tower.
        
    '''
    
    def __init__(self,coord,width,height):
        assert isinstance(coord,tuple), 'Warning! (x,y) must be a tuple.'
        assert width > 0, 'Warning! tower width must be greater than zero!'
        assert height > 0, 'Warning! tower height must be greater than zero!'
        assert (coord[0] >= 0) and (coord[1] >= 0), 'Warning! Lower left coordinate must be >= to 0!'
        assert isinstance(width,int), 'Warning! Must be int!'
        assert isinstance(height, int), 'Warning! Must be int!'

        self.width = width
        self.height = height
        self.coord_ll = coord                           #Lower left corner
 
    #In the event that something gets updated, these will always
    #update with the most recent values.    
    @property
    def coord_lr(self): #Lower Right Corner
        '''
        Returns lower right corner of tower's coverage area as an (x,y) tuple
        '''
        return (self.coord_ll[0] + self.width, self.coord_ll[1])
        
    @property #Top Left Corner
    def coord_tl(self):
        '''
        Returns top left corner of tower's coverage area as an (x,y) tuple
        '''
        return (self.coord_ll[0], self.coord_ll[1] + self.height)
    
    @property
    def coord_tr(self): #Top Right Corner
        '''
        Returns top right corner of tower's coverage area as an (x,y) tuple
        '''
        return (self.coord_ll[0] + self.width, self.coord_ll[1] + self.height)

    @property
    def area(self): #Coverage area of tower
        '''
        Returns the area of the tower's coverage area.
        '''
        return self.width * self.height
    
    def __repr__(self):
        '''
        Returns tower object in string format so as to easily reproduce the tower object.
        '''
        return 'tower(%s,%d,%d)' % (self.coord_ll,self.width,self.height)
            
    def contained(self,other):
        '''
        Checks which corners of a tower are contained in another tower's coverage area.
        
        Returns: A list of True or False. Where each item in the list is represented as
        
        checker = [LowerLeftCorner,TopLeftCorner,LowerRightCorner,TopRightCorner]
        
        If the whole list is True, then that means the tower is contained.
        Any Falses mean that that specific corner lies outside the domain of the towers
        coverage area.
        '''
        assert isinstance(other,tower),'Warning! Argument is not of class tower!'
        assert isinstance(self,tower), 'Warning! Argument is not of class tower!'
        checker = [False,False,False,False] #Corners = [lowerleft,TopLeft,lowerRight,TopRight]
        if (self.coord_ll[0] >= other.coord_ll[0]) and (self.coord_ll[1] >= other.coord_ll[1]):
            checker[0] = True
        if (self.coord_tl[0] >= other.coord_tl[0]) and (self.coord_tl[1] <= other.coord_tl[1]):
            checker[1] = True
        if (self.coord_lr[0] <= other.coord_lr[0]) and (self.coord_lr[1] >= other.coord_lr[1]):
            checker[2] = True
        if (self.coord_tr[0] <= other.coord_tr[0]) and (self.coord_tr[1] <= other.coord_tr[1]):
            checker[3] = True
            
        return checker
    
    def __eq__(self,other):
        '''
        Checks if one tower is equivalent to another.
        
        Returns: True or False.
        '''
        assert isinstance(self,tower)
        assert isinstance(other,tower)
        if(self.coord_ll == other.coord_ll) and (self.width == other.width) and (self.height == other.height):
            return True
        else: 
            return False
    
    def corner(self,other):
        '''
        Checks which corners of a tower are contained in another tower's coverage area.
        Ignores the bounds of the other tower's coverage area.
        
        Returns a list of boolean values, each refering to a corner of self
        corners, checkers, results = [lowerleftcorner,TopLeftcorner,lowerRightcorner,TopRightcorner]
        
        If True means the corner is indeed inside another tower.
        '''
        isinstance(other,tower)
        corners = [self.coord_ll,self.coord_tl,self.coord_lr,self.coord_tr]
        results = [] #The result of a corner.
        for corner in corners:
            checkers = [False,False,False,False]
            if (corner[0] > other.coord_ll[0]) and (corner[1] > other.coord_ll[1]):
                checkers[0] = True
            if (corner[0] > other.coord_tl[0]) and (corner[1] < other.coord_tl[1]):
                checkers[1] = True
            if (corner[0] < other.coord_lr[0]) and (corner[1] > other.coord_lr[1]):
                checkers[2] = True
            if (corner[0] < other.coord_tr[0]) and (corner[1] < other.coord_tr[1]):
                checkers[3] = True

            if all(checkers):
                results.append(True)
            else:
                results.append(False)
                
        return results
    
    def subtowers(self):
        '''
        Returns a list of all possible sub-towers in a tower's coverage area.
        '''
        print '\tAt subtowers'
        #Range of coordinate values possible within the current towers coverage area.
        coord_x_list = range(self.width)
        coord_y_list = range(self.height)
#        print 'coord_x_list: ', coord_x_list
#        print 'coord_y_list: ', coord_y_list
        
        #Possible x-values and y-values inside the tower's coverage area.
        tower_xs = [i+self.coord_ll[0] for i in coord_x_list]
        tower_ys = [i+self.coord_ll[1] for i in coord_y_list]
#        print 'tower_xs: ', tower_xs
#        print 'tower_ys: ', tower_ys
        #Range of possible tower widths and heights possible within tower's coverage area.
        w = range(self.width)
        h = range(self.height)
        tower_ws = [i+1 for i in w]
        tower_hs = [i+1 for i in h]
#        print 'tower_ws: ', tower_ws
#        print 'tower_hs: ', tower_hs
        
        tower_list = []
        for x in tower_xs:
            for y in tower_ys:
                for width in tower_ws:
                    for height in tower_hs:
                        t = tower((x,y),width,height)
                        tower_list.append(t)
                        
#        print 'tower_list: ', len(tower_list)
        #Since the above nested for-loops produce every possible variation
        #I need to make sure that these sub-towers are still within the tower
        #we started with.
        
        sub_towers = []
        for t in tower_list:
            valid = True
            checker = t.contained(self)
            for check in checker:
                if check == False:
                    valid = False
            if valid == True:
                sub_towers.append(t)    
        
#        print len(sub_towers)
        return sub_towers
        
    def overlap(self,other):
        '''
        Returns the overlap of one tower with another tower as a tower
        object. If no overlap is possible, returns None.
        '''
        isinstance(other,tower)
        sub_towers = self.subtowers()                

        #Now of the possible sub-towers, I want to check which ones overlap
        #with other.
        overlap_sub_towers = []
        for t in sub_towers:
            valid = True 
            checker = t.contained(other)
            for check in checker:
                if check == False:
                    valid = False
            if valid == True:
                overlap_sub_towers.append(t)
         
        best_area = 0
        best_overlap_coverage = None
        for t in overlap_sub_towers:
            if t.area > best_area:
                best_area = t.area
                best_overlap_coverage = t
                
        return best_overlap_coverage                                 
    
    def borders(self,other):
        '''
        Returns whether the left, right, top, or bottom wall of a tower overlaps with anothers in a list.
        
        The a boolean list with the list format is [Left Wall, Right Wall, Top Wall, Bottom Wall]
        
        True means that the wall is inside another tower's coverage area.
        '''
        wall = [False, False, False, False] #[left wall, right wall, top wall, bottom wall]
        #Start with left wall.
        if (self.coord_ll[0] < other.coord_lr[0]) and (self.coord_ll[0] >= other.coord_ll[0]):
            if (self.coord_ll[1] < other.coord_tl[1]) and (self.coord_ll[1] >= other.coord_ll[1]):
                wall[0] = True
            elif (self.coord_ll[1] < other.coord_ll[1]) and (self.coord_tl[1] > other.coord_ll[1]):
                wall[0] = True
        #Check right wall.
        if (self.coord_lr[0] > other.coord_ll[0]) and (self.coord_lr[0] <= other.coord_lr[0]):
            if (self.coord_lr[1] < other.coord_tr[1]) and (self.coord_lr[1] >= other.coord_lr[1]):
                wall[1] = True
            elif (self.coord_lr[1] < other.coord_lr[1]) and (self.coord_tr[1] > other.coord_lr[1]):
                wall[1] = True  
        #Checking top wall.
        if(self.coord_tl[1] > other.coord_ll[1]) and (self.coord_tl[1] <= other.coord_tl[1]):
            if (self.coord_tl[0] < other.coord_lr[0]) and (self.coord_ll[0] >= other.coord_ll[0]):
                wall[2] = True
            elif (self.coord_tl[0] < other.coord_ll[0]) and (self.coord_tr[0] > other.coord_ll[0]):
                wall[2] = True
        #Checking lower wall        
        if(self.coord_ll[1] < other.coord_tl[1]) and (self.coord_ll[1] >= other.coord_ll[1]):
            if (self.coord_ll[0] < other.coord_tr[0]) and (self.coord_ll[0] >= other.coord_ll[0]):
                wall[3] = True
            elif (self.coord_ll[0] < other.coord_ll[0]) and (self.coord_lr[0] > other.coord_ll[0]):
                wall[3] = True
        return wall

    def truncate(self,other):
        '''
        Takes in a list of towers to truncate against and returns a single tower
        object.
        
        Assertions:
            - Can only be used with tower objects.
            - List argument must be a list.
            - Arguments inside of list must be of class tower.
            
        Return: A tower object which is a truncated version of the tower you started with. If
                tower doesn't overlap with any others, truncate method returns the original
                tower. Returns None if no valid truncated version exists.
        '''
        print 'At truncate'
        assert isinstance(self,tower), 'Warning! Argument %s must be of class tower!' % (self)
        assert isinstance(other,list), 'Warning! Argument must be type list!'
        for t in other:
            assert isinstance(t,tower), 'Warning! Items in the list must be of class tower!' 
            
        sub_towers = self.subtowers()
        
        print'\t\tlen(sub_towers): ', len(sub_towers)

        the_list = []
        for t in other:   
            print '\tComputing corner filter!'
            valid_sub_towers = []
            for sub_tower in sub_towers:
                checkers = sub_tower.corner(t)
               # print checkers
                if any(checkers) == False:
                    valid_sub_towers.append(sub_tower)     

            print '\tComputing border filter!'
            final_sub_towers = []   
            for sub_tower in valid_sub_towers:
                checkers = sub_tower.borders(t)
                #print checkers
                if any(checkers) == False:
                    final_sub_towers.append(sub_tower)

            the_list = the_list + final_sub_towers

                   
        common = []
        amount_needed = len(other)

        print '\tlen(the_list): ',len(the_list)
        print '\tComputing common sub_towers!'
        for sub_tower in the_list:
            seen = 0
            for t in the_list:
                if t == sub_tower:
                    seen = seen + 1
            if seen == amount_needed:
                common.append(sub_tower)    
        
        print '\tComputing best coverage!'
        best_valid_coverage = None
        best_area = 0
        for t in common:
            if t.area > best_area:
                best_area = t.area
                best_valid_coverage = t
        
        return best_valid_coverage          
        
