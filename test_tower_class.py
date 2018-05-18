# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:57:16 2018

@author: humbe
"""
#Author: Humberto Hernandez
#Last updated: 5/17/2018 6:53pm
import unittest
from tower_class import tower

class TestTowerClass(unittest.TestCase):
    '''
    Used to make sure that the tower class is working properly.
    '''
    
    def setUp(self):
        self.t1 = tower((2,2),4,6)
        self.t2 = tower((7,2),2,6)
        self.other = [self.t1,self.t2]
        
    def test___eq__(self):
        t_test = tower((2,2),4,6)
        result = t_test == self.t1
        self.assertEqual(result,True)
        
    def contained(self):
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
        self.assertEqual(result_3,[False,False,True,True])                
        self.assertEqual(result_4,[True,False,False,False])
        self.assertEqual(result_1,[True,True,True,True])
        
    
    def test_corner(self):
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
        
    def test_truncate(self):
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
        
        
        
