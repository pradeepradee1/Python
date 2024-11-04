import sys
import os

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(SCRIPT_DIR)
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# print(SCRIPT_DIR)

# Add the module's directory to the path
# sys.path.append(os.path.abspath('../../Parent1'))

# print(SCRIPT_DIR)
# print(sys.path)

# Now you can import your module
# import my_module

# from Parent1.SubParnet1.module1 import first

# # Use your module
# first()


module_path = os.path.abspath(os.path.join('..', '..', 'Parent1', 'SubParnet1', 'module1.py'))
print("Module path:", module_path)


import importlib.util
spec = importlib.util.spec_from_file_location("my_module", module_path)
my_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_module)

# from module1 import first
my_module.first()
