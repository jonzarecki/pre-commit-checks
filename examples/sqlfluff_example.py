from common.sqlfluff_wrapper import apply_sqlfluff

my_bad_query = "SeLEct  *, 1, blah as  fOO \n" "  from myTable"
my_good_query = """
SELECT
    blah AS foo,
    1 AS one
FROM myTable
"""

if __name__ == "__main__":
    # kind-of a test
    print(apply_sqlfluff(my_bad_query, "postgres"))
    print("=================================")
    apply_sqlfluff(my_good_query, "postgres", do_print=True)
    assert apply_sqlfluff(my_good_query, "postgres") == "", "no output"
