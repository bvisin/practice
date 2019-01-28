"""[summary]
"""
class Node:
    """[summary]
    """


    def __init__(self, data):
        """[summary]

        Arguments:
            data {[type]} -- [description]
        """

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """left

        Arguments:
            data {[type]} -- [description]
        """

        if data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print(self):
        """[summary]
        """

        print(self.data)
