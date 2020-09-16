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
        self.assertEqual(classifyTriangle(201, 200, 200), 'InvalidInput', '201,200,200 is invalid input')

    def testZeroInput(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'Equilateral', '0,0,0 is an Equilateral triangle')

    def testEdgeInput(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 is an Equilateral triangle')

    def testNotIntegerInput(self):
        self.assertEqual(classifyTriangle(1.5, 1.5, 1.5), 'InvalidInput', '1.5, 1.5, 1.5 is invalid input')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 3, 1), 'NotATriangle', '1,3,1 is not a triangle')

    def testNotATriangleC(self):
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
        self.assertEqual(classifyTriangle(15, 15, 15), 'Equilateral', '15, 15, 15 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 1), 'Isoceles', '1,2,1 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(2, 1, 1), 'Isoceles', '2,1,1 should be isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'Isoceles', '1,1,2 should be isosceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2, 3, 4 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene', '4, 2, 3 should be scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(3, 4, 2), 'Scalene', '3, 4, 2 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
