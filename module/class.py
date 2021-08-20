"""Example class for nice things."""


class SimpleClass:
    a = 1
    b = 2
    c = 3


def func1(a: bool) -> int:
    if a:
        return 1
    return 2  # mypy fails without it


def func2(sql: str) -> str:
    """asdasdasdsa.

    Args:
        sql:  asdasdas

    Returns:
        sql. asdasd.
    """
    sql = """
    select max(b) from test_table

    where 1=1 and 2=2 group by a


    """
    sql = """
    select max(b) from test_table

    where 1=1 and 2=2 group by a


    """
    sql = """
    select max(b) from test_table

    where 1=1 and 2=2 group by a


    """
    return sql
