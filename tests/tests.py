from main import candidate_rule
from main import InputClass


def test_candidate_rule():
    assert candidate_rule(
        InputClass(table=[], type='TYPE', param1=-0.5, param2=0.1875, param3=-0.046875, param4=-0.8125, param5=0.0,
                   param6=-0.03515625)) == ('NOTHING', 'NOTHING')


def test_candidate_rule_2():
    assert candidate_rule(
        InputClass(table=[0.0], type='TYPE', param1=2.25, param2=0.03205128205128205, param3=0.967948717948718,
                   param4=3.1307692307692307, param5=0.0, param6=0.4597069597069597)) == ('YES', 'TYPE')
