#Author: Humberto Hernandez
#Last Updated: 5/19/2018 5:46pm
import itertools as it

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
        '''
        Creates self.width, self.height, and coord_ll upon instance creation of
        tower.
        
        Parameter: self
        Type: Instance of tower class.
        
        Parameter: coord
        Type: tuple of length 2, items in tuple must be integer.
        
        Parameter: width
        Type: int
        
        Parameter: height
        Type: int 
        
        Returns:
            - self.width = width
            - self.height = height
            - self.coord_ll = coord
            
        Assertions:
            - (x,y) coordinate must be a tuple.
            - Length of tuple must be 2.
            - width, height, x, and y must be greater than zero.
            - x and y coordinates must be integers.
            - width and height must be integers.
        
        '''
        assert isinstance(coord,tuple), 'Warning! (x,y) must be a tuple.'
        assert len(coord) == 2, 'Warning! Only a tuple of length two!'
        assert width > 0, 'Warning! tower width must be greater than zero!'
        assert height > 0, 'Warning! tower height must be greater than zero!'
        assert (coord[0] >= 0) and (coord[1] >= 0), 'Warning! Coordinates must be positive.'
        assert isinstance(coord[0],int) and isinstance(coord[1],int),'Coordinates must be integers.'
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
        
        Parameter: The instance of the tower being used to call this method is
                    referred to as self.
        Type: Instance of class tower.
        
        Return: (x,y) tuple for the lower right corner of tower's coverage area.
        
        e.g. 
        >>> t = tower((1, 2),6,4)
        >>> t.coord_lr
        (7,2)
                    
        Returns the lower right corner of a tower's coverage area by taking
        the width and adding it to the x-value of the of the tower object's
        lower left corner (self.coord_ll[0]) attribute's x-coordinate.
        
        Assertions:
            - Can only be used on an instance of tower class.
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        return (self.coord_ll[0] + self.width, self.coord_ll[1])
        
    @property #Top Left Corner
    def coord_tl(self):
        '''
        Returns top left corner of tower's coverage area as an (x,y) tuple
        
        Parameter: The instance of the tower being used to call this method is
                    referred to as self.
                    
        Type: Instance of class tower.
        
        Return: (x,y) tuple for the top left corner of tower's coverage area.
        
        e.g. 
        >>> t = tower((1, 2),6,4)
        >>>> t.coord_lr
        (1,6)
                    
        Returns the top left corner of a tower's coverage area by taking
        the height and adding it to the y-value of the of the tower object's
        lower left corner (self.coord_ll[1]) attribute's y-coordinate.
        
        Assertions:
            - Can only be used on an instance of tower class.
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        return (self.coord_ll[0], self.coord_ll[1] + self.height)
    
    @property
    def coord_tr(self): #Top Right Corner
        '''
        Returns top right corner of tower's coverage area as an (x,y) tuple
        
        Parameter: The instance of the tower being used to call this method is
                    referred to as self.
                    
        Type: Instance of class tower.
        
        Return: (x,y) tuple for the top right corner of tower's coverage area.
        
        e.g. 
        >>> t = tower((1, 2),6,4)
        >>> t.coord_lr
        (7,6)
                    
        Returns the top right corner of a tower's coverage area by taking
        the height and adding it to the y-value of the of the tower object's
        lower left corner (self.coord_ll[1]) attribute's y-coordinate as well as
        taking the width and adding it to the tower object's lower left corner
        (self.coord_ll[0]) attribute's x-coordinate.
        
        Assertions:
            - Can only be used on an instance of tower class.
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        return (self.coord_ll[0] + self.width, self.coord_ll[1] + self.height)

    @property
    def area(self): #Coverage area of tower
        '''
        Returns the area of the tower's coverage area.
        
        Parameter: The instance of the tower being used to call this method is
                    referred to as self.
                    
        Type: Instance of class tower.
        
        Return: Returns an integer value for the area.
        
        e.g. 
        >>> t = tower((1, 2),6,4)
        >>> t.area
        24
        
        Returns the area for a given tower object by taking the tower's width 
        (self.width) and a tower's height (self.height) and taking the product.
        
        self.area = self.width * self.height
        
        Assertions: 
            - Can only be used on an instance of tower class.
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        return self.width * self.height
    
    def __repr__(self):
        '''
        Returns tower object in string format so as to easily reproduce the tower object.
        
        e.g.
        >>> t = tower((1, 2),6,4)
        >>> print t
        tower((1, 2),6,4)
        
        Assertions:
            - Can only be used on an instance of tower class.
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        return 'tower(%s,%d,%d)' % (self.coord_ll,self.width,self.height)
            
    def contained(self,other):
        '''
        Checks which corners of a tower (referred to as self) are contained in 
        another tower's (referred to as other) coverage area.
        
        Parameter: self
        Type: tower object
        
        Parameter: other
        Type: tower object
        
        Returns: A list of True or False boolean values. Where each item in the 
        list corresponds to a corner in the following manner.
        
                [LowerLeftCorner,TopLeftCorner,LowerRightCorner,TopRightCorner]
        
        A corner produces a True value if it is inside other's coverage area.
        If the whole list is True, then that means the tower is contained.
        Any Falses mean that the corresponding corner lies outside the bounds 
        of the other's coverage area.
        
        e.g.
        
        >>> t = tower((0,0),2,2)
        >>> z = tower((1,1),2,2)
        >>> z.contained(t) 
        [True, False, False, False]
        >>> #Tells us that the lower left corner is inside t's coverage.
        
        It does so by checking each corner of a tower's (referred to as self)
        coverage area. For each corner it checks it against the corners of
        the other tower's (referred to as other) coverage area. It does so by
        accessing the attributes (coord_ll,coord_tl,coord_lr,coord_tr) of other's
        coverage area and checking against the x-coordinate and y-coordinate of
        each of other's corner. If one of self's corners is bounded inside by
        other's corners, then that corner is indeed contained and produces 
        a value of True. Else it produces False.
        
        Note: The corner method INCLUDES the bounds created by other's four
                corners
        
        Assertions:
            - Method can only be used on instances of tower class.
            
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
        
        Parameter: self
        Type: tower object
        
        Parameter: other
        Type: tower object
        
        Returns: True or False.
        
        e.g.
        >>> t = tower((0,0),2,2)
        >>> z = tower((0,0),2,2)
        >>> t == z
        True
        
        Returns True or False if a tower is equivalent to another tower.
        It does so by checking if the lower left coordinate's, the heights,
        and the widths of both towers match.
        - self.coord_ll == other.coord_ll
        - self.width == other.width
        - self.height == other.height
        
        Assertions:
            - Method can only be used on instances of tower class.
            
        '''
        assert isinstance(self,tower)
        assert isinstance(other,tower)
        if(self.coord_ll == other.coord_ll) and (self.width == other.width) and (self.height == other.height):
            return True
        else: 
            return False
    
    def corner(self,other):
        '''
        Checks which corners of a tower are in another tower's coverage area.
        Ignores the bounds of the other tower's coverage area.
        
        Parameter: self
        Type: tower object
        
        Parameter: other
        Type: tower object
        
        Return: A list with four boolean values, each corresponding to a corner of
                the tower (referred to as self), that is inside the tower is is
                being compared to (referred to as other.)
                
                [lowerleftcorner,TopLeftcorner,lowerRightcorner,TopRightcorner]
        
        e.g.
        
        >>> t = tower((0,0),2,2)
        >>> z = tower((1,1),2,2)
        >>> z.corner(t) 
        [True, False, False, False]
        >>> #Tells us that the lower left corner is inside t's coverage.
        
        It does so by checking each corner of a tower's (referred to as self)
        coverage area. For each corner it checks it against the corners of
        the other tower's (referred to as other) coverage area. It does so by
        accessing the attributes (coord_ll,coord_tl,coord_lr,coord_tr) of other's
        coverage area and checking against the x-coordinate and y-coordinate of
        each of other's corner. If one of self's corners is bounded inside by
        other's corners, then that corner is indeed contained and produces 
        a value of True. Else it produces False.
        
        The following variables in the code all have the same list convention.
        
        corners, checkers, results = [lowerleftcorner,TopLeftcorner,lowerRightcorner,TopRightcorner]
        
        Note: The corner method EXCLUDES the bounds created by other's four
                corners
 
       Assertions:
            - Method can only be used on instances of tower class.
                            
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        assert isinstance(other,tower), 'Warning! Argument must be of class tower!'
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
        Returns a generator object that produces all possible subtowers for a 
        given tower. Starts with subtowers with the largest area and goes down 
        to the subtowers with the smallest area.
        
        Parameter: self
        Type: tower object
        
        Return: generator object that produces a tower's sub-towers.
        
        e.g.
        >>> t = tower((0,0),2,2)
        >>> x = t.subtowers()
        >>> x
        <generator object subtowers at 0x000000000D9B6870>
        >>> for i in x:
        ...    print i
        ...
        tower((0, 0),2,2)
        tower((0, 0),1,2)
        tower((1, 0),1,2)
        tower((0, 0),2,1)
        tower((0, 1),2,1)
        tower((0, 0),1,1)
        tower((1, 0),1,1)
        tower((0, 1),1,1)
        tower((1, 1),1,1)
        
        It starts by taking the tower's width, height, and lower left corner value
        and constructing lists of all possible widths,heights, x-coordinates,
        and y-coordinates. Then it concatenates the widths and heights in order
        to use the product function from the itertools module to produce all
        possible width and height pairs into a list of tuples. It removes the 
        duplicates in this list. We then sort the width and height pairs by
        ordering them from the largest area to the smallest area that a pair
        can produce by the use of the built-in sort function found in Python and
        the use of a lambda function in it's argument. This helps avoid having
        to compute a large list which can reach millions of subtowers long if the
        desired coverage area is large enough.
        
        Assertions:
            - Can only be used on an instance of tower class.        
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        #Range of coordinate values possible within the current towers coverage area.
        coord_x_list = range(self.width)
        coord_y_list = range(self.height)
        
        #Possible x-values and y-values inside the tower's coverage area.
        tower_xs = [i+self.coord_ll[0] for i in coord_x_list]
        tower_ys = [i+self.coord_ll[1] for i in coord_y_list]
        
        #Range of possible tower widths and heights possible within tower's coverage area.
        w = range(self.width)
        h = range(self.height)
        tower_ws = [i+1 for i in w]
        tower_hs = [i+1 for i in h]
        
        tower_width_height = tower_hs + tower_ws
        
        width_height_pairs = []
        for product in it.product(tower_width_height,repeat = 2):
            width_height_pairs.append(product)
            
        unique_pairs = list(set(width_height_pairs))
        
        #Ordering from largest area to smallest.
        unique_pairs.sort(key = lambda (a,b): a*b, reverse = True)
        
        for width,height in unique_pairs:
            for y in tower_ys:
                for x in tower_xs:
                    t = tower((x,y),width,height)
                    if all(t.contained(self)):
                        yield t
                    else:
                        break
                                     
        
    def overlap(self,other):
        '''
        Returns the overlap of one tower with another tower as a tower
        object. If no overlap is possible, returns None.
        
        Parameter: self
        Type: tower object
        
        Parameter: other
        Type: tower object
        
        Return: tower object representing the region of overlap.
                If no overlap is found, returns None.
                
        e.g.
        >>> t = tower((0,0),2,2)
        >>> z = tower((1,1),2,2)
        >>> z.overlap(t)
        tower((1, 1),1,1)
        
        Returns the region of overlap by looking for the largest subtower that
        can represent the region of overlap. Due to the fact that when using 
        the subtowers() method, it produces the subtowers with the largest area
        first, that means that the first subtower that, when run through the
        contained method, produces all true, then it would be equal to the region
        of overlap. The use of the generator makes the computation quick. It can
        find the overlap without having to generate all possible subtowers.

       Assertions:
            - Method can only be used on instances of tower class. 
            
       '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        assert isinstance(other,tower), 'Warning! Argument must be of class tower!'               

        subtowers = self.subtowers()

        for subtower in subtowers:
            contained_check = subtower.contained(other)
            if all(contained_check):
                return subtower
            
        return None
    
    def borders(self,other):
        '''
        Returns whether the left, right, top, or bottom wall of a tower (self) overlaps
        with another tower's (other).
        
        Parameter: self
        Type: tower object
        
        Paramater: other
        Type: tower object
        
        Return: A boolean list with values corresonding to a wall in the following 
                format. True means that the wall is inside another tower's coverage area.
                False means that is is not between the other tower's walls.
                
                [Left Wall, Right Wall, Top Wall, Bottom Wall]
                
        e.g.
        >>> t = tower((0,0),2,2)
        >>> z = tower((1,1),2,2)
        >>> z.borders(t)
        [True, False, False, True] #Left wall and bottom wall are inside.
        
        It does so by checking each wall individually. For the left and right walls,
        it checks whether the x-coordinates of those walls can be found inside
        the region bounded between other's left and right walls. If is found within
        this region of x-values, it then checks whether the y-values of self's left
        and right walls are found in the region bounded by other's y-values of
        the left and right walls. The top and bottom walls are computed in a similar
        fashion.
        
        Assertions:
            - Method can only be used on instances of tower class. 
            
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        assert isinstance(other,tower), 'Warning! Argument must be of class tower!'
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
        Takes in a list of towers (other) to truncate against and returns a single tower
        object, optimizing new tower for maximum possible area.
        
        Parameter: self
        Type: tower object
        
        Parameter: other
        Type: list, items in this list must be type tower object.
        
        Return: tower object representing truncated version of self maximized
                for largest possible area. If no valid truncated version exists
                against towers found in the list, returns None. If tower does not
                overlap with any found in the list, returns itself.
        
        e.g.
        >>> t = tower((0,0),2,2)
        >>> z = tower((1,1),2,2)
        >>> z.truncate([t])
        tower((2, 1),1,2)
        
        It starts by calling the subtowers() method on self. It starts checking
        subtowers (starting with the largest area) and checks them against all
        towers found in the list (other). It only returns a the best truncated
        version if it passes both the corner method and the border method with
        values of all Falses (meaning not found inside the tower's we are
        checking against) for all towers found in the list (other).
        
        Assertions:
            - Can only be used with tower objects.
            - List argument must be a list.
            - Arguments inside of list must be of class tower.
        '''
        assert isinstance (self,tower), 'Warning! Requires an instance of tower class!'
        assert isinstance(other,list), 'Warning! Argument must be type list!'
        for t in other:
            assert isinstance(t,tower), 'Warning! Items in the list must be of class tower!' 
            
        subtowers = self.subtowers()
        
        default = None
        
        for subtower in subtowers:
            valid = 1
            for tower in other:
                corner_check = subtower.corner(tower)
                border_check = subtower.borders(tower)
                if (any(corner_check)) or (any(border_check)):
                    valid = 0
                    break
            if valid == 1:
                #Only returns subtower if it's valid subtower for all towers it is checking against.
                return subtower
        
        return default             
