This is a repository for learning Python and its concepts

# Knowledge for me
- Everything is an object in Python, even functions, classes, modules, numbers  
- No access modifiers like in C# (public/private/protected)  
- Access is hinted via conventions but not enforced:
  - _name => internal / protected by convention
  - __name => private-ish (Name Mangling for inheritance, no real access restriction)
- No return codes but exceptions
- Functions and modules are more important than classes
- Classes are only used for state, identity, or polymorphism
- Files and their functions are modules to be used  
- Classes are optional to encapsulate komplex structures
- Folders with __init__.py file are modules
- Modules contain functions, classes, constants, variables  
- creating projects via 'uv init'
- running projects then via 'uv run' 
- Package = module tree:

```text
my_project/
└─ services/
    ├─ __init__.py
    ├─ email.py
    └─ payment.py  

from services.email import send_mail
```
The interpreter acts as a simple calculator
```text
(50 - 5*6) / 4
5.0

5 ** 2  # 5 squared
25

2 ** 7  # 2 to the power of 7
128
```