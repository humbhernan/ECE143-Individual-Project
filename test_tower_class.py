#Author: Humberto Hernandez
#Last updated: 5/19/2018 7:44pm
import unittest
from tower_class import tower

class TestTowerClass(unittest.TestCase):
    '''
    Used to make sure that the tower class is working properly.
    Please run in the same directory containing the following files. 
    Please run as main file!
    
    - plotting_code_proj.py
    - tower_class.py
    - tower_coverage.py
    
    This code tests the following methods from the tower class.
    - __eq__
    - contained()
    - corner()
    - borders()
    - overlap()
    - subtowers()
    - truncate()
    
    '''
    
    def setUp(self):
        '''
        Sets up typical towers.
        
        t1 = tower((2,2),4,6)
        t2 = tower((7,2),2,6)
        other = [t1,t2]
        '''
        self.t1 = tower((2,2),4,6)
        self.t2 = tower((7,2),2,6)
        self.other = [self.t1,self.t2]
        
    def test___eq__(self):
        '''
        Tests the __eq__ method from the tower class.
        
        Test is, given two identical towers, does it recognize that they are
        equivalent?
        '''
        t_test = tower((2,2),4,6)
        result = t_test == self.t1
        self.assertEqual(result,True)
        
    def test_contained(self):
        '''
        Tests the contained method from the tower class.
        
        Tests typical situations seen by the contained method. This test case
        can be found in the Juypter Notebook section discussing the contained method.
        
        Consists of:
            - Can identify specific corners.
            - Can recognize when one tower is contained in another.
        '''
        grey_box = tower((2,2),5,5)
        dashed_box = tower((1,1),2,2)
        star_box = tower((6,1),2,2)
        dot_box = tower((1,6),2,2)
        slash_box = tower((6,6),2,2)
        backslash_box = tower((4,3),1,1)
        
        result_1 = dashed_box.contained(grey_box)
        result_2 = star_box.contained(grey_box)
        result_3 = dot_box.contained(grey_box)
        result_4 = slash_box.contained(grey_box)
        result_5 = backslash_box.contained(grey_box)
        
        self.assertEqual(result_1,[False,False,False,True])
        self.assertEqual(result_2,[False,True,False,False])
        self.assertEqual(result_3,[False,False,True,False])                
        self.assertEqual(result_4,[True,False,False,False])
        self.assertEqual(result_5,[True,True,True,True])
        
    
    def test_corner(self):
        '''
        Tests the corner method from the tower class.
        
        Tests typical situations seen by the corner method. This test case
        can be found in the Juypter Notebook section discussing the corner method.
        
        Consists of:
            - Can identify specific corners.
            - Can recognize when one tower is contained in another.
        '''
        grey_box = tower((1,1),1,2) #gray box
        blue_box = tower((2,1),1,2) #blue box
        result_1 = grey_box.corner(blue_box)
        
        self.assertEqual(result_1,[False, False, False, False])
        
        grey_box = tower((2,2),5,5)
        dashed_box = tower((1,1),2,2)
        star_box = tower((6,1),2,2)
        dot_box = tower((1,6),2,2)
        slash_box = tower((6,6),2,2)
        backslash_box = tower((4,3),1,1)
        
        result_1 = dashed_box.corner(grey_box)
        result_2 = star_box.corner(grey_box)
        result_3 = dot_box.corner(grey_box)
        result_4 = slash_box.corner(grey_box)
        result_5 = backslash_box.corner(grey_box)
        
        self.assertEqual(result_1,[False,False,False,True])
        self.assertEqual(result_2,[False,True,False,False])
        self.assertEqual(result_3,[False,False,True,False])                
        self.assertEqual(result_4,[True,False,False,False])
        self.assertEqual(result_5,[True,True,True,True])

       
    def test_borders(self):
        '''
        Tests the border method from the tower class.
        
        Tests typical cases seen by the borders method. The cases this tests can
        be found in the Juypter Notebook section discussing the borders method.
        
        Consists of:
            - Can it tell which wall(s) is inside a region of another tower's
                coverage.
        '''
        grey_box = tower((2,2),4,4)
        t_test =[tower((1,3),1,2),tower((3,1),2,1),tower((6,3),1,2),tower((3,6),2,1)]

        for t in t_test:
            result = t.borders(grey_box)
            self.assertEqual(result,[False,False,False,False])
          
        slash_box = tower((1,1),2,6)
        star_box = tower((5,1),2,6)
         
        result_1 = slash_box.borders(grey_box)
        result_2 = star_box.borders(grey_box)
         
        self.assertEqual(result_1,[False,True,False,False])
        self.assertEqual(result_2,[True,False,False,False])
        
        slash_box = tower((1,5),6,2)
        star_box = tower((1,1),6,2)
        
        result_3 = slash_box.borders(grey_box)
        result_4 = star_box.borders(grey_box)
         
        self.assertEqual(result_3,[False,False,False,True])
        self.assertEqual(result_4,[False,False,True,False])
        
        slash_box = tower((1,3),6,2)
        star_box = tower((3,1),2,6)
        
        result_3 = slash_box.borders(grey_box)
        result_4 = star_box.borders(grey_box)
         
        self.assertEqual(result_3,[False,False,True,True])
        self.assertEqual(result_4,[True,True,False,False])

    def test_overlap(self):
        '''
        Tests the overlap method found in the tower class.
        
        Tests typical cases that overlap is used for. The various
        cases can be found in the Juypter Notebook dicsussing the overlap
        method.
        
        Consists of
        - Can it return the right tower object for the case in question.
        '''
        grey_box = tower((2,2),4,4)
        slash_box = tower((1,1),2,6)
        
        result = slash_box.overlap(grey_box)
        self.assertEqual(result.area,4)
        self.assertEqual(result.coord_ll,(2,2))
        self.assertEqual(result.width,1)
        self.assertEqual(result.height,4)
        
        slash_box = tower((1,5),6,2)
        star_box = tower((1,1),6,2)
        
        overlap_1 = slash_box.overlap(grey_box)
        overlap_2 = star_box.overlap(grey_box)

        self.assertEqual(overlap_1.coord_ll,(2,5))
        self.assertEqual(overlap_1.width,4)
        self.assertEqual(overlap_1.height,1)
        
        self.assertEqual(overlap_2.coord_ll,(2,2))
        self.assertEqual(overlap_2.width,4)
        self.assertEqual(overlap_2.height,1)
        
        grey_box = tower((4,1),2,6)
        slash_box = tower((1,1),2,6)
        dash_box = slash_box.overlap(grey_box)
        
        self.assertEqual(dash_box,None)
        
    def test_subtowers(self):
        '''
        Tests for the subtowers() method found in the tower class.
        
        Test a typical case used for subtower. We create a tower and check the
        resulting list against the list that it should generate.
        '''
        t = tower((0,0),5,5)
        test = [tower((0, 0),1,1),
                 tower((0, 0),1,2),
                 tower((0, 0),1,3),
                 tower((0, 0),1,4),
                 tower((0, 0),1,5),
                 tower((0, 0),2,1),
                 tower((0, 0),2,2),
                 tower((0, 0),2,3),
                 tower((0, 0),2,4),
                 tower((0, 0),2,5),
                 tower((0, 0),3,1),
                 tower((0, 0),3,2),
                 tower((0, 0),3,3),
                 tower((0, 0),3,4),
                 tower((0, 0),3,5),
                 tower((0, 0),4,1),
                 tower((0, 0),4,2),
                 tower((0, 0),4,3),
                 tower((0, 0),4,4),
                 tower((0, 0),4,5),
                 tower((0, 0),5,1),
                 tower((0, 0),5,2),
                 tower((0, 0),5,3),
                 tower((0, 0),5,4),
                 tower((0, 0),5,5),
                 tower((0, 1),1,1),
                 tower((0, 1),1,2),
                 tower((0, 1),1,3),
                 tower((0, 1),1,4),
                 tower((0, 1),2,1),
                 tower((0, 1),2,2),
                 tower((0, 1),2,3),
                 tower((0, 1),2,4),
                 tower((0, 1),3,1),
                 tower((0, 1),3,2),
                 tower((0, 1),3,3),
                 tower((0, 1),3,4),
                 tower((0, 1),4,1),
                 tower((0, 1),4,2),
                 tower((0, 1),4,3),
                 tower((0, 1),4,4),
                 tower((0, 1),5,1),
                 tower((0, 1),5,2),
                 tower((0, 1),5,3),
                 tower((0, 1),5,4),
                 tower((0, 2),1,1),
                 tower((0, 2),1,2),
                 tower((0, 2),1,3),
                 tower((0, 2),2,1),
                 tower((0, 2),2,2),
                 tower((0, 2),2,3),
                 tower((0, 2),3,1),
                 tower((0, 2),3,2),
                 tower((0, 2),3,3),
                 tower((0, 2),4,1),
                 tower((0, 2),4,2),
                 tower((0, 2),4,3),
                 tower((0, 2),5,1),
                 tower((0, 2),5,2),
                 tower((0, 2),5,3),
                 tower((0, 3),1,1),
                 tower((0, 3),1,2),
                 tower((0, 3),2,1),
                 tower((0, 3),2,2),
                 tower((0, 3),3,1),
                 tower((0, 3),3,2),
                 tower((0, 3),4,1),
                 tower((0, 3),4,2),
                 tower((0, 3),5,1),
                 tower((0, 3),5,2),
                 tower((0, 4),1,1),
                 tower((0, 4),2,1),
                 tower((0, 4),3,1),
                 tower((0, 4),4,1),
                 tower((0, 4),5,1),
                 tower((1, 0),1,1),
                 tower((1, 0),1,2),
                 tower((1, 0),1,3),
                 tower((1, 0),1,4),
                 tower((1, 0),1,5),
                 tower((1, 0),2,1),
                 tower((1, 0),2,2),
                 tower((1, 0),2,3),
                 tower((1, 0),2,4),
                 tower((1, 0),2,5),
                 tower((1, 0),3,1),
                 tower((1, 0),3,2),
                 tower((1, 0),3,3),
                 tower((1, 0),3,4),
                 tower((1, 0),3,5),
                 tower((1, 0),4,1),
                 tower((1, 0),4,2),
                 tower((1, 0),4,3),
                 tower((1, 0),4,4),
                 tower((1, 0),4,5),
                 tower((1, 1),1,1),
                 tower((1, 1),1,2),
                 tower((1, 1),1,3),
                 tower((1, 1),1,4),
                 tower((1, 1),2,1),
                 tower((1, 1),2,2),
                 tower((1, 1),2,3),
                 tower((1, 1),2,4),
                 tower((1, 1),3,1),
                 tower((1, 1),3,2),
                 tower((1, 1),3,3),
                 tower((1, 1),3,4),
                 tower((1, 1),4,1),
                 tower((1, 1),4,2),
                 tower((1, 1),4,3),
                 tower((1, 1),4,4),
                 tower((1, 2),1,1),
                 tower((1, 2),1,2),
                 tower((1, 2),1,3),
                 tower((1, 2),2,1),
                 tower((1, 2),2,2),
                 tower((1, 2),2,3),
                 tower((1, 2),3,1),
                 tower((1, 2),3,2),
                 tower((1, 2),3,3),
                 tower((1, 2),4,1),
                 tower((1, 2),4,2),
                 tower((1, 2),4,3),
                 tower((1, 3),1,1),
                 tower((1, 3),1,2),
                 tower((1, 3),2,1),
                 tower((1, 3),2,2),
                 tower((1, 3),3,1),
                 tower((1, 3),3,2),
                 tower((1, 3),4,1),
                 tower((1, 3),4,2),
                 tower((1, 4),1,1),
                 tower((1, 4),2,1),
                 tower((1, 4),3,1),
                 tower((1, 4),4,1),
                 tower((2, 0),1,1),
                 tower((2, 0),1,2),
                 tower((2, 0),1,3),
                 tower((2, 0),1,4),
                 tower((2, 0),1,5),
                 tower((2, 0),2,1),
                 tower((2, 0),2,2),
                 tower((2, 0),2,3),
                 tower((2, 0),2,4),
                 tower((2, 0),2,5),
                 tower((2, 0),3,1),
                 tower((2, 0),3,2),
                 tower((2, 0),3,3),
                 tower((2, 0),3,4),
                 tower((2, 0),3,5),
                 tower((2, 1),1,1),
                 tower((2, 1),1,2),
                 tower((2, 1),1,3),
                 tower((2, 1),1,4),
                 tower((2, 1),2,1),
                 tower((2, 1),2,2),
                 tower((2, 1),2,3),
                 tower((2, 1),2,4),
                 tower((2, 1),3,1),
                 tower((2, 1),3,2),
                 tower((2, 1),3,3),
                 tower((2, 1),3,4),
                 tower((2, 2),1,1),
                 tower((2, 2),1,2),
                 tower((2, 2),1,3),
                 tower((2, 2),2,1),
                 tower((2, 2),2,2),
                 tower((2, 2),2,3),
                 tower((2, 2),3,1),
                 tower((2, 2),3,2),
                 tower((2, 2),3,3),
                 tower((2, 3),1,1),
                 tower((2, 3),1,2),
                 tower((2, 3),2,1),
                 tower((2, 3),2,2),
                 tower((2, 3),3,1),
                 tower((2, 3),3,2),
                 tower((2, 4),1,1),
                 tower((2, 4),2,1),
                 tower((2, 4),3,1),
                 tower((3, 0),1,1),
                 tower((3, 0),1,2),
                 tower((3, 0),1,3),
                 tower((3, 0),1,4),
                 tower((3, 0),1,5),
                 tower((3, 0),2,1),
                 tower((3, 0),2,2),
                 tower((3, 0),2,3),
                 tower((3, 0),2,4),
                 tower((3, 0),2,5),
                 tower((3, 1),1,1),
                 tower((3, 1),1,2),
                 tower((3, 1),1,3),
                 tower((3, 1),1,4),
                 tower((3, 1),2,1),
                 tower((3, 1),2,2),
                 tower((3, 1),2,3),
                 tower((3, 1),2,4),
                 tower((3, 2),1,1),
                 tower((3, 2),1,2),
                 tower((3, 2),1,3),
                 tower((3, 2),2,1),
                 tower((3, 2),2,2),
                 tower((3, 2),2,3),
                 tower((3, 3),1,1),
                 tower((3, 3),1,2),
                 tower((3, 3),2,1),
                 tower((3, 3),2,2),
                 tower((3, 4),1,1),
                 tower((3, 4),2,1),
                 tower((4, 0),1,1),
                 tower((4, 0),1,2),
                 tower((4, 0),1,3),
                 tower((4, 0),1,4),
                 tower((4, 0),1,5),
                 tower((4, 1),1,1),
                 tower((4, 1),1,2),
                 tower((4, 1),1,3),
                 tower((4, 1),1,4),
                 tower((4, 2),1,1),
                 tower((4, 2),1,2),
                 tower((4, 2),1,3),
                 tower((4, 3),1,1),
                 tower((4, 3),1,2),
                 tower((4, 4),1,1)]
        subtowers = t.subtowers()
        generated = list(subtowers)
        
        self.assertEqual(len(test), len(generated))
        
        for subtower in test:
            saw_it = 0
            for t in generated:
                if t == subtower:
                    saw_it = 1
            self.assertEqual(saw_it, 1)
            
        
        
    def test_truncate(self):
        '''
        Tests the truncate method from the tower class.
        
        Tests typical cases that the truncate method would be used for. The
        cases can be found in the Juypter Notebook section discussing the
        truncate method.
        
        Tests the result against the truncated tower it should generate if
        working properly.
        '''
        grey_box = tower((2,2),4,4)
        slash_box = tower((1,1),2,6)

        dash_box = slash_box.truncate([grey_box])

        self.assertEqual(dash_box.coord_ll,(1,1))
        self.assertEqual(dash_box.width,1)
        self.assertEqual(dash_box.height,6)

        grey_box = tower((2,2),4,4)
        slash_box = tower((1,5),6,2)
        star_box = tower((1,1),6,2)
        
        truncate_1 = slash_box.truncate([grey_box])
        truncate_2 = star_box.truncate([grey_box])
        
        self.assertEqual(truncate_1.coord_ll,(1,6))
        self.assertEqual(truncate_1.width,6)
        self.assertEqual(truncate_1.height,1)

        self.assertEqual(truncate_2.coord_ll,(1,1))
        self.assertEqual(truncate_2.width,6)
        self.assertEqual(truncate_2.height,1)
        
        slash_box = tower((2,1),4,6)
        grey_box = tower((1,2),2,4)
        blue_box = tower((5,2),2,4)
        
        t = [grey_box,blue_box]
        
        dash_box = slash_box.truncate(t)
        
        self.assertEqual(dash_box.coord_ll,(3,1))
        self.assertEqual(dash_box.width,2)
        self.assertEqual(dash_box.height,6)
        
        grey_box = tower((1,2),2,4)
        blue_box = tower((5,2),2,4)
        
        dash_box = grey_box.truncate([blue_box])
        
        self.assertEqual(dash_box.coord_ll,(1,2))
        self.assertEqual(dash_box.width,2)
        self.assertEqual(dash_box.height,4)
        

if __name__ == '__main__':
    unittest.main()
        
        
        
