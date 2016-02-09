from bintree import BinTree, BinNode


class TreeVerifier:
    """
    Tests if a given BinTree is structurally sound.
    In a structurally sound BinTree the root element has no parent and all the
    other nodes link to their correct parent.
    Subclasses should override doVerify() to do their own verifications.
    """

    @staticmethod
    def get_verifier(bt):
        """
        Factory method to create the correct TreeVerifier for given tree.

        :param bt: The tree to create a TreeVerifier for.
        :type bt : BinTree
        :return: A new TreeVerifier or RBTreeVerifier, depending on bt.
        """
        return TreeVerifier(bt)

    def __init__(self, bt):
        """
        Constructs a new TreeVerifier for the given tree.

        :type bt : BinTree
        """
        self.bt = bt

    def verify(self, message):
        """
        Verifies the tree.

        :param message : A message explaining what type of operation may have
        caused the potential error.
        :type message : str
        :raises VerificationException : An exception explaining what is wrong with the tree.
        """
        try:
            self.do_verify()
        except VerificationException as e:
            raise VerificationException("{}: {}".format(message, e), e)

    def do_verify(self):
        """
        Does all the verifications for this class.
        Override this.

        :raises ParentChildLinkException : This tree has a node with the wrong parent-link.
        :raises VerificationException : There is something else wrong with this tree.
        """
        self.verify_tree(self.bt.root, None, None, None)

    def verify_tree(self, node, true_parent, min_element, max_element):
        """
        Verifies the structure of the tree.

        :param node : The node to check recursively.
        :type node : BinNode
        :param true_parent : What the parent of this node should be.
        :type true_parent : BinNode | None
        :param min_element : The value of its closest left ancestor.
        :type min_element : object | None
        :param max_element : The value of its closest right ancestor.
        :type max_element : object | None
        :raises ParentChildLinkException : This node has the wrong parent-link.
        :raises NodeOrderException : This node isn't where it should be.
        """
        if not node:
            return

        parent = node.parent
        left = node.left
        right = node.right

        if parent != true_parent:
            raise ParentChildLinkException(node, true_parent, parent)

        if node.value == min_element or node.value == max_element:
            raise DuplicateNodeException(node)

        if min_element and node.value <= min_element:
            raise NodeOrderException(node, min_element, False)

        if max_element and node.value >= max_element:
            raise NodeOrderException(node, max_element, True)

        self.verify_tree(left, node, min_element, node.value)
        self.verify_tree(right, node, node.value, max_element)


class VerificationException(Exception):
    """
    An Exception noting that something is wrong with the tree.
    """

    def __init__(self, error_node_or_message, cause=None):
        """
        Creates a new VerificationException for given node.
        ** or **
        Creates a new VerificationException from another
        VerificationException and a message explaining what was done to get
        to this error.

        :type error_node_or_message : BinNode | str
        :type cause : VerificationException | None
        """
        if isinstance(error_node_or_message, BinNode):
            self._node = error_node_or_message
        else:
            super().__init__(error_node_or_message)
            self._node = cause.node

    @property
    def node(self):
        """
        Returns the node which is in error.

        :rtype: BinNode
        """
        return self._node

    @staticmethod
    def node_value_str(node):
        """
        Returns the String value of given node or "None" if node is None.

        :type node : BinNode
        """
        return str(node.value) if node else "None"


class ParentChildLinkException(VerificationException):
    """
    Thrown when the parent-link of a child does not link to its actual parent.
    """

    def __init__(self, node, true_parent, supposed_parent):
        """
        Creates a new ParentChildLinkException.

        :param node : The node with the wrong parent.
        :type node : BinNode
        :param true_parent : The actual parent of the node.
        :type true_parent: BinNode
        :param supposed_parent : The node which this node thinks is is parent.
        :type supposed_parent : BinNode
        """
        super().__init__(node)
        self.true_parent = true_parent
        self.supposed_parent = supposed_parent

    def __str__(self):
        """
        Returning a message describing what is wrong.
        """
        if not self.true_parent:
            return "node {} has a parent-link to {}, however it is the root node".format(self.node.value,
                                                                                         self.supposed_parent.value)
        elif not self.supposed_parent:
            return "node {} thinks it is the root node, however it is the child of {}".format(self.node.value,
                                                                                              self.true_parent.value)
        else:
            return "node {} has a parent-link to {}, however it is the child of {}".format(self.node.value,
                                                                                           self.supposed_parent.value,
                                                                                           self.true_parent.value)


class DuplicateNodeException(VerificationException):
    """
    Thrown when the parent-link of a child does not link to its actual parent.
    """

    def __init__(self, node):
        """
        Creates a new DuplicateNodeException.

        :param node : The node which is a duplicate.
        :type node : BinNode
        """
        super().__init__(node)

    def __str__(self):
        """
        Returning a message describing what is wrong.
        """
        return "node {} is already in the tree".format(self.node.value)


class NodeOrderException(VerificationException):
    """
    Thrown when a node is bigger than or equal to its right ancestor or smaller than its left ancestor.
    """

    def __init__(self, node, ancestor, left_sub_tree):
        """
        Creates a new NodeOrderException.

        :param node : The node which is too big or too small.
        :type node : BinNode
        :param ancestor : The ancestor which should be bigger or smaller than the errorNode.
        :type ancestor : object
        :param left_sub_tree : Whether the node is in the left subtree of the ancestor.
        :type left_sub_tree : bool
        """
        super().__init__(node)
        self.ancestor = ancestor
        self.left_sub_tree = left_sub_tree

    def __str__(self):
        """
        Returning a message describing what is wrong.
        """
        if self.left_sub_tree:
            return "node {} is in the left subtree of {}, should be in the right subtree".format(self.node.value,
                                                                                                 self.ancestor)
        else:
            return "node {} is in the right subtree of {}, should be in the left subtree".format(self.node.value,
                                                                                                 self.ancestor)
