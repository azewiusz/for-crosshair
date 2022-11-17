# Summary

Generating tests for program logic from `main.py` -> ``candidate_rule`` gives unit tests (looks to be without error)
. When these test are executed with python ``coverage.py`` we see failing assertions:

Test generation command:

````shell
crosshair cover --example_output_format=pytest --coverage_type opcode --per_condition_timeout=240 main.candidate_rule > ./tests/tests.py
````

**Remark**:
This run parameters were generating 2 unit tests within 240 seconds on AMD Ryzen 9 CPU workstation.
Once test are generated we need to import InputClass from ``main.py`` manually.

Test coverage measured using this command:

```shell
coverage run -m pytest .\tests\tests.py
coverage html --show-contexts
```

Error from coverage execution:

```python
  def test_candidate_rule_2():
>       assert candidate_rule(InputClass(table=[0.0], type='TYPE', param1=2.25, param2=0.03205128205128205, param3=0.967948717948718, param4=3.1307692307692307, param5=0.0, param6=0.4597069597069597)) == ('YES', 'TYPE')
E       AssertionError: assert ('NOTHING', 'NOTHING') == ('YES', 'TYPE')
E         At index 0 diff: 'NOTHING' != 'YES'
E         Use -v to get more diff

```