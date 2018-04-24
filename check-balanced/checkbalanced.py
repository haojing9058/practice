"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""

        if not self:
            return True

        # depth first search
        # false if two leaf depths are more than 1 apart
        # false if more than two leaf depths
        # (node, depth)
        lengths = []
        nodes_stack = []
        nodes_stack.append((self, 0))

        if ((self.left) and (not self.right)) or ((self.right) and (not self.left)):
            lengths.append(0)

        while nodes_stack:
            node, length = nodes_stack.pop()

            if (not node.left) and (not node.right):
                if length not in lengths:
                    lengths.append(length)

            else:
                if node.left:
                    nodes_stack.append((node.left, length + 1))

                if node.right:
                    nodes_stack.append((node.right, length + 1))

            if (len(lengths) == 2 and abs(lengths[0] - lengths[1]) > 1) or len(lengths) > 2:
                return False

        return True




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
