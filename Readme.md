This is a repository for learning Python and its concepts

# Knowledge for me  
- for beginners Python is used as a scripting language  
- local porjects with main.py and then modules to be used
- Everything is an object in Python, even functions, classes, modules, numbers 
- functions allow multiple return values: return mean, median, std  
- string formatierung: f"Test {varible}"
- No access modifiers like in C# (public/private/protected)  
- Access is hinted via conventions but not enforced
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
- Creating a min.py should have a main function:  
```text
if __name__ == "__main__":
    doStuff()
```
- Passing arguments to script: python main.py [Command]  

# Naming conventions  
- Variables & functions => snake_case  
- Calses => PascalCase  
- Constants => BIG_SNAKE_CASE  
- Private => _private_func() / _private_variable  
- Dunder => \_\_main\_\_ => reserved for Python internal methods

# Extended topics
- DataFrames in memory DB integrated in Pandas Library  
- Queryable with filters based on dataframes: df[df['year'] == 2026]  
- Set values:  
-- mask = df['date'] == '2026-02-03'  
-- df.loc[mask, 'temp_c'] = 5.0  
- export Dataframes:  
-- excel  
-- csv  
- StreamLit: Web App ohne HTML/ CSS  
- based on DataFrames  