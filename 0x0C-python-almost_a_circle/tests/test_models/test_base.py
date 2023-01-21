#!/usr/bin/python3
""" Base Class Test Module. """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import unittest


class TestBaseClass(unittest.TestCase):
    """ Tests all methods in Base class. """

    def test_create_instance(self):
        """ Test that Base instance is created. """
        obj = Base()
        obj1 = Base(12)
        self.assertTrue(obj)
        self.assertTrue(obj1)

    def test_base_id(self):
        """ Test Base id. """
        obj = Base()
        obj1 = Base(12)
        obj2 = Base()
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj1.id, 12)
        self.assertEqual(obj2.id, 2)

    def test_base_instance(self):
        """ Test instance of Base. """
        obj = Base()
        obj1 = Base(12)
        self.assertIsInstance(obj, Base)
        self.assertIsInstance(obj1, Base)
        self.assertNotIsInstance(obj, int)
        self.assertNotIsInstance(obj, float)

    def test_to_json_string(self):
        """ Test JSON string representation. """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertIsNotNone(Base.to_json_string(None))
        obj = Rectangle(6, 7, 0, 0, 5)
        obj_json = Base.to_json_string([obj.to_dictionary()])
        self.assertIsInstance(obj_json, str)
        json_str = '[{"id": 5, "width": 6, "height": 7, "x": 0, "y": 0}]'
        self.assertEqual(obj_json, json_str)

    def test_from_json_string(self):
        """ Test JSON string to dictionary. """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        obj = Rectangle(6, 7, 0, 0, 6)
        obj_json = Base.to_json_string([obj.to_dictionary()])
        obj_json_list = Base.from_json_string(obj_json)
        self.assertIsInstance(obj_json_list, list)
        json_list = [{"id": 6, "width": 6, "height": 7, "x": 0, "y": 0}]
        self.assertEqual(obj_json_list, json_list)


if __name__ == '__main__':
    unittest.main()
