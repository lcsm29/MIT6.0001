# Problem Set 4A
# Name: lcsm29
# Collaborators: None
# Time Spent: unknown
# version 0.11.210528 - cleaned it up a bit

def get_permutations(sequence):
    """ Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = []
        for i, fixed in enumerate(sequence):
            for perm in get_permutations(sequence[:i] + sequence[i + 1:]):
                permutations.append(fixed + perm)
        return list(dict.fromkeys(permutations))


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'foo'
    print('Input:', example_input)
    print('Expected Output:', ['foo', 'ofo', 'oof'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'ttt'
    print('Input:', example_input)
    print('Expected Output:', ['ttt'])
    print('Actual Output:', get_permutations(example_input))
