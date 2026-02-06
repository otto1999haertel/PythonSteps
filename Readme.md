This is a repository for learning Python an its concepts

# Knowledge for me
- Everything is an object in Python even functions, classes, modules, numbers  
- No Access modifier like in C# (public/private/protected)  
- Access is hinted via conventions but not enforced  
-- _name => protected  
-- __name => private  
- No return codes but execptions  
- functions and modules are more important than classes  
- classes are only used for states, identity, polymorphism  
- files and its functions are modules to be used  
- modules contain functions, classes, constants, variables  
- Package = Module tree:  
```text
my_project/
└─ services/
    ├─ __init__.py
    ├─ email.py
    └─ payment.py

from services.email import send_mail
```
