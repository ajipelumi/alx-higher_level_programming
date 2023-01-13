One of the core concepts in object-oriented programming (OOP) languages is **inheritance**.
It is a mechanism that allows us to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class.
**Inheritance** is the capability of one class to derive or inherit the properties from another class.

### Benefits of inheritance 
 - It represents real-world relationships well.
- It provides the **reusability** of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
- Inheritance offers a simple, understandable model structure. 
- Less development and maintenance expenses result from an inheritance.

### Python Inheritance Syntax
```python
class BaseClass:
    {Body}

class DerivedClass(BaseClass):
    {Body}
```

This README decribes what each script/program is doing:

All test files are inside the folder `tests`.

The file `0-lookup.py` is a program that returns the list of available attributes and methods of an object.

The file `1-my_list.py` is a program that defines a class `MyList` that inherits from `list`.

The file `2-is_same_class.py` is a program that returns `True` if the object is *exactly* an instance of the specified class; otherwise `False`.

The file `3-is_kind_of_class.py` is a program that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

The file `4-inherits_from.py` is a program that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

The file `5-base_geometry.py` is a program that defines an empty class `BaseGeometry`.

The file `6-base_geometry.py` is a program that defines a class `BaseGeometry` (based on `5-base_geometry.py`).

The file `7-base_geometry.py` is a program that defines a class `BaseGeometry` (based on `6-base_geometry.py`).

The file `8-rectangle.py` is a program that defines a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

The file `9-rectangle.py` is a program that defines a class `Rectangle` that inherits from `BaseGeometry` (`8-base_geometry.py`).

The file `10-square.py` is a program that defines a class `Square` that inherits from `Rectangle` (`9-rectangle.py`).

The file `11-square.py` is a program that defines a class `Square` that inherits from `Rectangle` (`10-rectangle.py`).

The file `100-my_int.py` is a program that defines a class `MyInt` that inherits from `int`.

The file `101-add_attribute.py` is a program that adds a new attribute to an object if it’s possible.
