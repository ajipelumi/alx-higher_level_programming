#!/usr/bin/python3
""" Rectangle Class Test Module. """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import unittest
import io


class TestRectangleClass(unittest.TestCase):
    """ Tests all methods in Rectangle class. """

    def test_rectangle(self):
        """ Test that Rectangle values exist. """
        obj = Rectangle(1, 2)
        obj1 = Rectangle(1, 2, 3)
        obj2 = Rectangle(1, 2, 3, 4)
        obj3 = Rectangle(1, 2, 3, 4, 5)
        
        with self.assertRaises(TypeError):
            obj4 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            obj5 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            obj6 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            obj7 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            obj8 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            obj9 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            obj10 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            obj11 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            obj12 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            obj13 = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        """ Test the area of a rectangle. """
        obj = Rectangle(3, 2)
        obj1 = Rectangle(2, 10)
        self.assertEqual(obj.area(), 6)
        self.assertEqual(obj1.area(), 20)

    def test_rectangle_magic_str(self):
        """ Test that __str__ exists. """
        obj = Rectangle(4, 6, 2, 1, 12)
        expected_str = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(obj), expected_str)

    def test_display_without_x_y(self):
        """ Test the display method without x and y. """
        
        # Redirect stdout to a variable
        output = io.StringIO()
        sys.stdout = output

        obj = Rectangle(2, 2)
        obj.display()

        # Reset redirect
        sys.stdout = sys.__stdout__

        expected = ('#' * obj.width + '\n') * obj.height
        self.assertEqual(output.getvalue(), expected)

    def test_display_without_y(self):
        """ Test the display method without y. """
        
        # Redirect stdout to a variable
        output = io.StringIO()
        sys.stdout = output

        obj = Rectangle(2, 2, 3)
        obj.display()

        # Reset redirect
        sys.stdout = sys.__stdout__

        expected = (' ' * obj.x + '#' * obj.width + '\n') * obj.height

    def test_display(self):
        """ Test the display method. """
        
        # Redirect stdout to a variable
        output = io.StringIO()
        sys.stdout = output

        obj = Rectangle(2, 2, 3, 2)
        obj.display()

        # Reset redirect
        sys.stdout = sys.__stdout__

        expected = ('' * obj.y) + (' ' * obj.x + '#' * obj.width + '\n') * obj.height

    def test_to_dictionary(self):
        """ Test dictionary representation of a Rectangle. """
        obj = Rectangle(10, 2, 1, 9, 1)
        obj_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(obj.to_dictionary(), obj_dict)

    def test_update(self):
        """ Test that Rectangle class updates. """
        obj = Rectangle(10, 2, 1, 9, 1)
        self.assertTrue(hasattr(obj, 'update'))
        old_dict = obj.to_dictionary()
        obj.update(89)
        self.assertEqual(obj.id, 89)
        obj.update(89, 1)
        self.assertEqual(obj.width, 1)
        obj.update(89, 1, 2)
        self.assertEqual(obj.height, 2)
        obj.update(89, 1, 2, 3)
        self.assertEqual(obj.x, 3)
        obj.update(89, 1, 2, 3, 4)
        self.assertEqual(obj.y, 4)
        
        new_dict = {'x': 3, 'y': 4, 'id': 89, 'height': 2, 'width': 1}
        self.assertEqual(obj.to_dictionary(), new_dict)
        self.assertNotEqual(old_dict, new_dict)

        obj.update(**{ 'id': 89 })
        self.assertEqual(obj.id, 89)
        obj.update(**{ 'id': 89, 'width': 1 })
        self.assertEqual(obj.width, 1)
        obj.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(obj.height, 2)
        obj.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(obj.x, 3)
        obj.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(obj.y, 4)



if __name__ == '__main__':
    unittest.main()
