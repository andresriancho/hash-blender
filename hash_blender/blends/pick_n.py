from itertools import permutations, combinations

KEY_VALUE_SEPARATORS = '=:'


def pick_n(user_inputs):
    """
    Picks strings from the user_inputs and yields them as a list. There are
    various ways in which we'll pick the results:

        * Pick 1..len(user_inputs)
        * Pick them in different order
        * Pick only values
        * Pick keys and values

    :user_inputs: a dict with key/values to pick from

    :yield: N combinations of the different inputs provided by the user
            returned as a list of strings. The result is a list so we can

    Warning: This method returns duplicates!
    """
    for value_list in apply_key_value(user_inputs):
        for ordered_value_list in apply_orders(value_list):
            for ordered_sliced_value in apply_slices(ordered_value_list):
                yield ordered_sliced_value


def apply_key_value(user_inputs):
    """
    This will return:
     * Only the values
     * The keys and values separated with all KEY_VALUE_SEPARATORS

    :param user_inputs: The user configured user dict
    :yield: Yield the values
    """
    # Just the values
    yield user_inputs.values()

    # The keys and values, with different separators
    for separator in KEY_VALUE_SEPARATORS:
        result = []
        for key, value in user_inputs.items():
            result.append('%s%s%s' % (key, separator, value))
        yield result


def apply_orders(user_inputs):
    """
    :param user_inputs: User inputs as a list of strings
    :yield: The user inputs ordered in all the different ways they can
    """
    for perm in permutations(user_inputs):
        yield perm


def apply_slices(user_inputs):
    """
    :param user_inputs: User inputs as a list of strings
    :yield: The user inputs sliced in all the different ways they can be
    """
    for len_iter in xrange(len(user_inputs)):
        for comb in combinations(user_inputs, len_iter + 1):
            if comb:
                yield comb
