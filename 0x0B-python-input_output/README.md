Python provides basic functions and methods necessary to manipulate files by default. 
Most file manipulation can be done using a file object.

To read or write a file, you have to open it using Python's built-in `open()` function.
This function creates a file object, which would be utilized to call other support methods associated with it.

Once all the operations are done on the file, we must close it through our Python script using the `close()` method.
Any unwritten information gets destroyed once the `close()` method is called on a file object.

This README decribes what each script/program is doing:

The file `0-read_file.py` is a program that reads a text file (`UTF8`) and prints it to stdout.

The file `1-write_file.py` is a program that writes a string to a text file (`UTF8`) and returns the number of characters written.

The file `2-append_write.py` is a program that appends a string at the end of a text file (`UTF8`) and returns the number of characters added.

The file `3-to_json_string.py` is a program that returns the JSON representation of an object (string).

The file `4-from_json_string.py` is a program that returns an object (Python data structure) represented by a JSON string.

The file `5-save_to_json_file.py` is a program that writes an Object to a text file, using a JSON representation.

The file `6-load_from_json_file.py` is a program that creates an Object from a “JSON file”.

The file `7-add_item.py` is a program that adds all arguments to a Python list, and then save them to a file.

The file `8-class_to_json.py` is a program that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

The file `9-student.py` is a program that defines a `Student` class.

The file `10-student.py` is a program that defines a student by: (based on `9-student.py`).

The file `11-student.py` is a program that defines a student by: (based on `10-student.py`).

The file `12-pascal_triangle.py` is a program that returns a list of lists of integers representing the Pascal’s triangle of `n`.

The file `100-append_after.py` is a program that inserts a line of text to a file, after each line containing a specific string.
