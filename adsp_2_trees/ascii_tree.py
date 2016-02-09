class AsciiTreeVisualizer:

    def __init__(self, bt):
        """
        Creates a new visualizer for the bt node.
        :param bt : Tree to visualize.
        :type bt : bintree.BinTree
        """
        self.bt = bt
        """
        :type : bintree.BinTree
        """
        self.lines = []
        """
        A list of all the rows to be printed.
        :type : list[str]
        """
        self.max_level = -1
        self.horpos = 0
    
    def create_lines(self, level, horpos):
        """
        Makes sure there are enough rows for the given level.
        :type level : int
        :type horpos : int
        """
        if level <= self.max_level:
            return

        base = ' ' * horpos

        while self.max_level < level:
            self.lines.append(base)
            self.lines.append(base)
            self.max_level += 1

    def add_item(self, item, level, direction):
        """
        Adds an item on the given level for the given direction.

        :param item: The node to add.
        :type item : bintree.BinNode
        :param level: The level of the item to add.
        :type level : int
        :param direction: The direction of the line to the parent. -1 if this is a left
        child, 1 if this is a right child or 0 if this is the root node.
        :type direction : int
        """

        if item:
            s = str(item.value)
        else:
            s = "*"

        # Make sure we have enough lines
        self.create_lines(level, self.horpos)

        # The line to add the string
        target = 2*level+1

        # The number of chars to add to all other lines
        n = len(s)

        # The base string to add to all other lines
        base = ' ' * n

        # Iterate over all lines
        for i in range(0, self.max_level*2+2):
            line = self.lines[i]
            if i == target-1:
                # Previous line must hold the connecting line to the parent
                if direction == -1:
                    line += base[:-1]
                    line += '/'
                elif direction == 0:
                    line += base[:-1]
                    line += '|'
                elif direction == 1:
                    line += '\\'
                    line += base[:-1]
                else:
                    raise ValueError('Invalid dir {}'.format(direction))
            elif i == target:
                # The current line holds the item
                line += s
            else:
                # The other lines hold spaces.
                line += base

            self.lines[i] = line

        self.horpos += n

    def construct_tree(self, node, level, direction):
        """
        Constructs a Tree at level 'level' on direction 'dir' rooted at 'node'.
        Dir = -1 for '/', 0 for '|', 1 for '\'.
        :type node : bintree.BinNode
        :type level : int
        :type direction : int
        """
        left = node.left
        right = node.right
        if left:
            self.construct_tree(left, level+1, -1)
        self.add_item(node, level, direction)
        if right:
            self.construct_tree(right, level+1, 1)

    def show_tree(self):
        """
        Shows an ascii visualization of the given tree on the standard output.
        """
        self.max_level = -1
        self.lines = []
        self.horpos = 0
        node = self.bt.root

        if not node:
            print("||")
            print("*|")
        else:
            self.construct_tree(node, 0, 0)
            for line in self.lines:
                print(line)
