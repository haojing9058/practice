"""Count employees in an org chart.

Our organization has the following org chart::

                    Jane
          Jessica          Janet
       Al  Bob  Jen     Nick  Nora
                                Henri

Let's make this chart::

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

And test our counting function::

    >>> henri.count_employees()
    0

    >>> nora.count_employees()
    1

    >>> jane.count_employees()
    8

We provide a non-recursive version, let's make sure that gives the same
answer::

    >>> jane.count_employees_nonrecursive()
    8

"""


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """
        count = 0

        if not self.children:
            return count

        for child in self.children:
            count = count + 1 + child.count_employees()

        return count

    def count_employees_nonrecursive(self):
        count = 0
        to_visit = [self]
        while to_visit:

            for child in to_visit.pop().children:
                to_visit.append(child)
                count += 1

        return count







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n"

