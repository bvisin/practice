"""[summary]

Returns:
    [type] -- [description]
"""

class Tree():
    """[summary]

    Returns:
        [type] -- [description]
    """


    def __init__(self, root_node):
        self.root_node = root_node
        self.rtn_list = []
        self.queue = []

    def generate_list(self):
        """[summary]
        preorder traversal (root-left-right)

        Returns:
            [type] -- [description]
        """

        self.queue.append(self.root_node)

        while self.queue:
            node = self.queue.pop(0)

            self.rtn_list.append(node.data)

            if node.left:
                self.queue.append(node.left)

            if node.right:
                self.queue.append(node.right)

        return self.rtn_list
