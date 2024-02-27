name = "Alan"
print(name)

x = 3
y = 4
z = 5

# print(x if not x + y * z else y)
# using auto-docstring generator
def a_function(a, b) -> int:
    """_summary_

    Args:
        a (_int_): _num1_
        b (_type_): _description_

    Returns:
        int: _description_
    """
    pass
print("carrying on...")
    # floating point innacurracy
# IEEE 754
print(0.3-0.1)  # 0.19999999999999998
print(0.1 + 0.1 + 0.1)  # 0.30000000000000004