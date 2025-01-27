# OneCompiler
### Compilation of many languages in Python!

- [Project on PyPi](https://pypi.org/project/onecompiler/)

<br>
<details open>
<summary> Mini documentation </summary> <br>

Installing the library
```shell
pip install onecompiler
```
<hr>

Import
```python
from onecompiler import Compiler	# Sync
from onecompiler import AsyncCompiler	# Async
```
<br>

Initialization
```python
compiler = Compiler()
```
<br>

Get a list of available languages
```python
print(compiler.all_languages)
```


<br>
Languages are compiled through the Compiler attribute or using <code>compiler.to.lang</code> <br>
» For query languages <code>compiler.query.lang</code>
<br>
<br>

<b>Example:</b>
```python
# Sample JavaScript code
res = compiler.to.js('console.log("Hello");')
print(res.stdout)
# Hello

# Sample MySQL code
res2 = compiler.query.mysql('SELECT 10')
print(res2.stdout)
# 10
```	
Or
```python
res = compiler.compile(lang='js', code='console.log("Hello");')
print(res.stdout)
# Hello

res2 = compiler.compile(lang='mysql', code='SELECT 10')
print(res2.stdout)
# 10
```



