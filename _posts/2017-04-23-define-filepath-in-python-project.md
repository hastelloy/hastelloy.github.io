---
layout: post
title: File path in Python project - Python项目中文件路径的设置
---

{{page.title}}
===============

There are a bunch of data files to be accessed from different modules or submodules within the project. Normally, we would like to save the data files under a seperate folder from the executing code.

Let's say, we have a structure as below.
```
project
 |-- __init__.py
 |-- mod_a
 |    |-- __init__.py
 |    |-- file_a1.py
 |    |-- ...
 |-- data_folder
      |-- data_a
      |-- ...
```

In `file_a1`, you need open `data_a`. Ok, it could be relative path. It would be something like:
```python
# under file_a1.py
def func_a1():
    fp = os.path.join(os.path.pardir, 
                        "data_folder", 
                        "data_a")
    with open(fp, 'r') as ff:
        pass
```

All looks fine. __Done...__

__Wait__, when it comes another function invoking `func_a1` under the root folder, things changed.

```
--
project
 |-- __init__.py
 |-- root.py
 |-- mod_a
 |    |-- __init__.py
 |    |-- file_a1.py
 |-- data_folder
      |-- data_a
      |-- ...
```

Under `root.py`, `func_a1` is invoked.

```python
# under root.py
from mod_a.file_a1 import func_a1

if __name__ == '__main__':
    func_a1()
```

See what happens:
`IOError: [Errno 2] No such file or directory: 'c:\\usr\\work\\data_folder\\data_a'` 
where `c:\usr\work` is the parent dir of the project in my example. 

As we can see, the relative path under `func_a` is now been applied to the working dir of `root.py`. Current working dir is `c:\usr\work\project`. When `func_a1` is executed, `os.path.pardir` is `c:\usr\work\`.

The __solution__ would be:
```python
# under file_a1.py
def func_a1():
    fp = os.path.abspath(
            os.path.join(
                        os.path.dirname(__file__),
                        os.path.pardir, 
                        "data_folder", 
                        "data_a"))
    with open(fp, 'r') as ff:
        pass
```
`os.path.dirname(__file__)` to get the dir of containing file `func_a1`. Note the sequence of dirs, `os.path.pardir` should be after current dir when join the dirs.
