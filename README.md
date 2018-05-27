# PyBrace
## A transpiler for PyBrace to vanilla Python language.

Tired of annoying python indentation errors? PyBrace comes to the rescue. PyBrace is an extension of Python that adds support for our beloved braces!
<br/>We feel that, as a developer, you should spend more time writing efficient code, rather than wasting time on frustrating indentation errors.
<br/>In PyBrace leading whitespace is irrelevant. You can give or forget as many whitespace characters as you want. PyBrace counts level of indentation based on number of braces entered.
<br/>PyBrace files are stored with `.pyb` extension. Once, your script is finished, you call the `pyb` interpreter to transpile to vanilla Python script with `.py` extension.
<br/>Your final python script won't have any braces and shall be replaced with correct indentations. Everytime.
<br/>PyBrace script for development and Python script for Python interpreter and everyone else. It's a win-win situation!
<br/><br/>PyBrace Syntax for Compound Statements that require indentation:
```
compound_statement:{  #Nothing after '{'. Not even comments.
  statements;
} #Nothing after '}'. Not even comments.
```
### Install:
<br/>Install using `python setup.py install`

### Usage:
```
usage: pyb [-h] target [indent]

Transpile PyBrace files to vanilla Python scripts

positional arguments:
  target      File to be transpiled
  indent      No of spaces to indent with. Default is 6.

optional arguments:
  -h, --help  show this help message and exit
```

### Example PyBrace script:
```
import os
 if(4<5):{
print 'Hello'
}
```
#### Output with default indentation of 6 spaces:
```
import os
if(4<5):
      print 'Hello'
```

