import dataclasses
from typing import List, Tuple


@dataclasses.dataclass
class InputClass:
    # crosshair: on
    table: List[float]
    type: str
    param1: float
    param2: float
    param3: float
    param4: float
    param5: float
    param6: float


def rule19(param1: float) -> bool:
    # crosshair: on
    return param1 > 0.8


def rule21(param1: float) -> bool:
    # crosshair: on
    return param1 > 6.0


def rule22(param1: float, param2: float, param3: float):
    # crosshair: on
    return (param1 >= 0.7 and (param2 <= 2 or param3 <= 0.3))


def indicator1(param1: float, param2: float) -> float:
    # crosshair: on
    return param1 / (param1 + param2)


def indicator2(param1: List[float], param2: float, param3: float, param4: float):
    # crosshair: on
    p1 = sum(param1) + param2 + param3
    pp = param2 + param3
    return p1 / pp, p1, pp


def indicator3(param1: float, param2: float, param3: float, param4: float) -> float:
    # crosshair: on
    ad = param1 + param2 - param3 * 0.5
    ad1 = param4
    assert ad1 != 0.0
    return ad / ad1


def indicator4(param1: float, param2: float, param3: float, param4: float) -> float:
    # crosshair: on
    if param2 < 0.0:
        param5 = param1 + param2
    else:
        param5 = param1

    adl = param3 - (param5 * 0.5)
    ad1 = param4 + param3
    assert ad1 != 0.0
    return adl / ad1


def indicator5(param1: float, param2: float, param3: float) -> float:
    # crosshair: on
    d = param1 + param2
    ii = param3
    assert ii != 0.0
    return d / ii


def generate_constraints(io: InputClass):
    # crosshair: on
    result = 0.0 <= io.param1 <= 100_000_000.0 \
             and 100_000_000.0 >= io.param4 >= 100_000_000.0 >= io.param2 >= 0.0 <= io.param3 <= 100_000_000.0 <= io.param5 <= 100_000_000.0 \
             and 0.0 <= io.param6 <= 100_000_000.0 \
             and len(io.table) > 0 and min(io.table) >= 0.0
    return result


def candidate_rule(input_object: InputClass) -> Tuple[str, str]:
    # crosshair: on
    ind1 = indicator1(input_object.param1, input_object.param2)
    ind2a, ind2b, ind2c = indicator2(input_object.table, input_object.param2, input_object.param3,
                                     input_object.param1)
    ind3 = indicator3(input_object.param3, input_object.param1, input_object.param4, input_object.param6)
    ind4 = indicator4(input_object.param4, input_object.param5, input_object.param1, input_object.param2)
    ind5 = indicator5(input_object.param3, input_object.param1, input_object.param6)

    r19 = rule19(ind1)
    r21 = rule21(ind5)
    r22 = rule22(ind2a, ind3, ind4)

    if input_object.type == "TYPE":
        if r19 and r21 and r22 and generate_constraints(input_object):
            return "YES", "TYPE"
    return "NOTHING", "NOTHING"
