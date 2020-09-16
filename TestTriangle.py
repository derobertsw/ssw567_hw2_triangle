# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1,1,1 is invalid input')

    def testLargeInput(self):
        self.assertEqual(classifyTriangle(200.1, 200, 200), 'InvalidInput', '200.1,200,200 is invalid input')

    def testZeroInput(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'Equilateral', '0,0,0 is an Equilateral triangle')

    def testEdgeInput(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 is an Equilateral triangle')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 3, 1), 'NotATriangle', '1,1,1 is not a triangle')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(3, 1, 1), 'NotATriangle', '3,1,1 is not a triangle')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(1.5, 1.5, 1.5), 'Equilateral', '1.5, 1.5 ,1.5 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 1), 'Isosceles', '1,2,1 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(2, 1, 1), 'Isosceles', '2,1,1 should be isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'Isosceles', '1,1,2 should be isosceles')

    def testRightIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1.4142), 'Right', '1,1,1.4142 should be Right')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2.5, 3), 'Scalene', '1, 2.5 ,3 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(2.5, 3, 1), 'Scalene', '2.5, 3, 1 should be scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(3, 1, 2.5), 'Scalene', '3, 1, 2.5 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
