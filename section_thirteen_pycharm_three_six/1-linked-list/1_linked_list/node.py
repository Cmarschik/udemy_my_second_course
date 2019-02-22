class Node:
    """
    This Node class has been created for you.
    It contains the necessary properties for the solution, which are:
    - name
    - matric
    - year
    - next
    """

    def __init__(self, name, matric, year):
        self.name = name
        self.matric = matric
        self.year = year
        self.__next = None # __ is so that nothing can change the .next

    def set_next(self, node):
        if isinstance(node, Node) or node is None: # check to see if it is of Node type or is type None
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type Node or None.")

    def get_next(self):
        return self.__next

    def print_details(self):
        print("{}: {} (year {})".format(self.matric, self.name, self.year))
