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

    def generate_list(self):
        """[summary]

        Returns:
            [type] -- [description]
        """

        self.dfs(self.root_node)
        return self.rtn_list

    def dfs(self, node):
        """[summary]

        Returns:
            [type] -- [description]
        """
        if not node:
            return

        #preorder search (Data, Left, Right)
        self.rtn_list.append(node.data)
        print(node.data)

        self.dfs(node.left)
        self.dfs(node.right)
