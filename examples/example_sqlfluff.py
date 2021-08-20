from common.sqlfluff_wrapper import apply_sqlfluff

my_bad_query = "SeLEct  *, 1, blah as  fOO \n" "  from myTable"
my_good_query = """
SELECT
    blah AS foo,
    1 AS one
FROM myTable
"""


def test_sqlfluff_is_running_and_has_no_output_on_correct_sqls() -> None:
    # kind-of a test
    print(apply_sqlfluff(my_bad_query, "postgres"))
    print("=================================")
    apply_sqlfluff(my_good_query, "postgres", do_print=True)
    assert apply_sqlfluff(my_good_query, "postgres") == "", "no output"
