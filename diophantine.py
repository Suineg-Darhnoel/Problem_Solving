def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def solve(a, b):
    """
        This function is used to solve two-variable diophantine
        equation in the form of ax + by = gcd(a, b)
    """
    # indicate the starting point of execution
    print("-"*50)

    # create the empty list for storing necessary values
    # found at each euclid algorithm step
    div_list = []

    # local greatest common divisor function
    def _gcd(a, b):
        while b:
            div_list.append((a, b, a//b, a%b))
            a, b = b, a%b
        return a

    # print and call _gcd function at the same time
    print(f"Start solving equation {a}x + {b}y = {_gcd(a, b)}")

    # we need to recall the memory
    # in the reverse order of euclid algorithm
    # st stands for sorted
    st_div_list = sorted(div_list)

    # get the first element of st_div_list
    fst = st_div_list[1]

    # the gcd(a, b) = gcd_val = st_div_list[0][1]
    # here I should have used namedtuple for clarity
    gcd_val = st_div_list[0][1]

    # the curr_comps (current components) is used
    # to express the current computation in terms of
    # the result optained by euclid algorithm
    # ex: From equation: 1960x + 103y = 1
    # 1 = (103)(1) + (3)(-34)
    curr_comps = ((fst[0], 1), (fst[1], -fst[2]))

    _print_str = "{} = ({})({}) + ({})({})"
    # show the current equation
    print(_print_str.format(gcd_val, *curr_comps[0], *curr_comps[1]))

    for elem in st_div_list[2:]:
        # break down the element into details
        a, b, div, rmd = elem

        # unpack the components for computation
        f_prev_item, f_prev_coeff = curr_comps[0]
        s_prev_item, s_prev_coeff = curr_comps[1]

        # compute for new components
        fst_term = (a, s_prev_coeff)
        sec_term = (f_prev_item, (-div)*s_prev_coeff+f_prev_coeff)

        # store the new components
        curr_comps = (fst_term, sec_term)

        # show the current equation
        print(_print_str.format(gcd_val, *fst_term, *sec_term))

    # show the general roots of the equation ax + by = gcd(a, b)
    print(f"=> x = {curr_comps[0][1]} + {b}k")
    print(f"=> y = {curr_comps[1][1]} + ({-a})k")
