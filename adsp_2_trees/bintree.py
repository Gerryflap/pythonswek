class BinTree:
    """
    A Binary Search Tree.
    """

    def __init__(self, old_tree=None):
        """
        Creates a BinTree or copy a given BinTree.

        :param old_tree: Tree to copy.
        :type old_tree: BinTree
        """
        self.root = None
        """
        The root node or None if no root node exists.

        :type : BinNode | None
        """

        if old_tree:
            self.root = self.create_node(old_tree.root, None)

    def add(self, element):
        """
        Adds the element to this BinTree.

        None elements cannot be added.

        :param element: Element to be added.

        :return: True if the element is added, False if the element is None or the tree already contains the element.
        :rtype: bool
        """

        if element is None:
            return False

        node = self.add_node(element)

        if not node:
            return False

        if node.value != element:
            raise ValueError("BinNode.add({element}).getValue() returned {value} instead of {element}"
                             .format(element=element, value=node.value))

        return True

    def add_node(self, element):
        """
        Adds the element to this BinTree.

        :param element: Element to be added. Cannot be None.
        :return: The object added or null if this object is already contained in this tree.
        """

        if not self.root:
            self.root = self.create_node(element, None)
            return self.root
        else:
            return self.root.add(element)

    def remove(self, element):
        """
        Removes the element from the tree.

        :param element: The element to be removed.
        :return: Whether the element was found;
        :rtype: bool
        """
        if not self.root:
            return False

        node = self.root.search(element)

        if not node:
            return False
        else:
            node.remove()
            return True

    def create_node(self, node_or_value, parent):
        """
        Creates a new node given a parent and a value or copies a node including its children (used for cloning).

        Subclasses should override this method to create their own nodes.

        :param node_or_value: The node to copy or the value of this node.
        :type node_or_value: BinNode | object | None
        :param parent: The parent of this node.
        :type parent: BinNode | None
        :rtype: BinNode
        """
        return BinNode(self, node_or_value, parent)

    def rotate_left(self, element):
        """
        Rotates the tree left at specified element.

        :param element: The object to rotate at.
        :return: Whether the node was found.
        :rtype: bool
        """
        node = self.root.search(element)
        if not node:
            return False
        else:
            node.rotate_left()
            return True

    def rotate_right(self, element):
        """
        Rotates the tree right at specified element.

        :param element: The object to rotate at.
        :return: Whether the node was found.
        :rtype: bool
        """
        node = self.root.search(element)
        if not node:
            return False
        else:
            node.rotate_right()
            return True

    # ----------------------------------------------------------------------------------
    # The implementation of the following methods in this class is not that interesting.
    # Please refer to the javadoc for information about the methods.
    # ----------------------------------------------------------------------------------

    #
    # Series of static functions which work ok with null-values. All these
    # functions are chainable, so you can do colorOf(leftOf(leftOf(node)))
    # even if node has no left child.
    #

    @staticmethod
    def left_of(node):
        """
        Returns the left child of n. Returns ``None`` if ``node`` is ``None``.

        You can safely chain these functions.

        :type node: BinNode | None
        :rtype: BinNode | None
        """
        return node.left if node else None

    @staticmethod
    def right_of(node):
        """
        Returns the right child of n. Returns ``None`` if ``node`` is ``None``.

        You can safely chain these functions.

        :type node: BinNode | None
        :rtype: BinNode | None
        """
        return node.right if node else None

    @staticmethod
    def parent_of(node):
        """
        Returns the parent of n. Returns ``None`` if ``node`` is ``None``.

        You can safely chain these functions.

        :type node: BinNode | None
        :rtype: BinNode | None
        """
        return node.parent if node else None

    @staticmethod
    def sibling_of(node):
        """
        Returns the sibling of n. Returns ``None`` if ``node`` is ``None``.

        You can safely chain these functions.

        :type node: BinNode | None
        :rtype: BinNode | None
        """
        if not node:
            return None

        if not node.parent:
            return None

        if node == BinTree.left_of(node.parent):
            return node.parent.right
        else:
            return node.parent.left

    def replace_child(self, old_child, new_child):
        """
        Wrapper function to replace one child with another.

        It will automatically check if the child is a left or a right child and will automatically set the correct
        parent and child links of the new node and parent.

        If oldchild is the root node, it will make newchild the new root.

        :param old_child: The child to be replaced.
        :type old_child: BinNode
        :param new_child: The child to replace the old child with.
        :type new_child: BinNode

        **Requires:** ``old_child is not None``

        **Requires:** ``old_child.parent is None`` (root element)
        or ``old_child.parent.left == oldchild`` (left child)
        or ``old_child.parent.light == oldchild`` (right child)
        """
        if not old_child.parent:
            self.root = new_child
            new_child.parent = None
        elif old_child.is_left():
            old_child.parent.attach_left(new_child)
        else:
            old_child.parent.attach_right(new_child)

    def __iter__(self):
        """
        Returns an iterator which iterates over the elements.

        :rtype: BinTreeIterator
        """
        return BinTreeIterator(self)

    def __contains__(self, element):
        """
        Returns whether the element is contained in this set.

        :param element: Element to search
        :rtype: bool
        """
        return bool(self.root.search(element))

    def __len__(self):
        """
        Returns the number of elements in this BinNode. This implementation
        traverses the whole tree.
        """
        return len(self.root) if self.root else 0

    def clone(self):
        """
        Clones the tree.

        :return: Clone of the tree.
        :rtype: BinTree
        """
        return self.__class__(self)

    def __str__(self):
        """
        A rude toString implementation of the tree.
        """
        return self.root.__str__() if self.root else "Empty"


class BinNode:
    """
    Internal class implementing the tree.
    """

    def __init__(self, tree, node_or_value, parent):
        """
        Creates a new node given a parent and a value or copies a node including its children (used for cloning).

        :param tree: The tree this node belongs to.
        :type tree: BinTree
        :param node_or_value: The node to copy or the value of this node.
        :type node_or_value: BinNode | object | None
        :param parent: The parent of this node.
        :type parent: BinNode | None
        """

        self.left = None
        """
        The left child of this node.

        :type : BinNode | None
        """
        self.right = None
        """
        The right child of this node.

        :type : BinNode | None
        """
        self.parent = parent
        """
        The parent of this node.

        :type : BinNode | None
        """

        self.tree = tree
        """
        The tree this node belongs to.

        :type : BinTree
        """

        if isinstance(node_or_value, BinNode):
            node = node_or_value
            self.value = node_or_value.value
            self.left = tree.create_node(node.left, self) if node.left else None
            self.right = tree.create_node(node.right, self) if node.right else None
        else:
            self.value = node_or_value

    def add(self, element):
        """
        Adds the object ``element`` to this ``BinNode`` at the
        right location.

        **IMPORTANT:** This implementation must NOT use the
        ``BinNode`` constructor, but must use ``self.tree.create_node(node_or_value, parent)`` instead.

        :param element: Element to be added.
        :return: The node which was inserted or ``None`` if the node already existed.
        :rtype: BinNode | None

        **Requires:** ``element is not None``
        """

        # Add implmementation here
        if element < self.value:
            if self.left is not None:
                return self.left.add(element)
            else:
                self.left = self.tree.create_node(element, self)
                return self.left
        elif element == self.value:
            return None
        else:
            if self.right is not None:
                return self.right.add(element)
            else:
                self.right = self.tree.create_node(element, self)
                return self.right

    def rotate_left(self):
        """
        Rotates the tree left at this location.

        This will structurally rotate the tree, making the right child the new root of the current subtree and making
        this node the left child of the new root.  The left child of the right child will be the new right child of this
        node.
        """

        # Add implmementation here
        oldParent = self.parent
        newParent = self.right
        self.right = newParent.left
        self.parent = newParent
        if self.right is not None:
            self.right.parent = self
        newParent.left = self
        newParent.parent = oldParent
        if oldParent is not None:
            if oldParent.left == self:
                oldParent.left = newParent
            else:
                oldParent.right = newParent
        else:
            self.tree.root = newParent

    def rotate_right(self):
        """
        Rotates the tree right at this location.

        This will structurally rotate the tree, making the left child the new root of the current subtree and making
        this node the right child of the new root. The right child of the left child will be the new left child of this
        node.
        """

        # Add implmementation here
        oldParent = self.parent
        newParent = self.left
        self.attach_left(newParent.right)
        newParent.attach_right(self)
        newParent.parent = oldParent
        if oldParent is None:
            self.tree.root = newParent
        else:
            if oldParent.right == self:
                oldParent.attach_right(newParent)
            else:
                oldParent.attach_left(newParent)

    # -----------------------------------------------------------------
    # The implementation of the following code is not that interesting.
    # Please refer to the javadoc for information about the methods.
    # -----------------------------------------------------------------

    def right_ancestor(self):
        """
        Returns the closest ancestor of which this element is in its left subtree.

        Currently used by the successor and remove.

        :return The first larger parent of this node. ``None`` if no such ancestor exists.
        :rtype: BinNode | None
        """
        if not self.parent:
            # No parent. This is the top node.
            return None

        if self.is_left():
            # We are the left child of our parent. Found ancestor.
            return self.parent
        else:
            # We are the right child of our parent. Call recursively.
            return self.parent.right_ancestor()

    def successor(self):
        """
        Finds the successor of a current node.

        The successor is always the leftmost node of the right subtree or it is the first right ancestor.

        Used by :py:meth:`~bintree.BinNode.remove` and the iterator.

        :return: The successor of a node or ``None`` if no such successor exists.
        :rtype: BinNone | None
        """
        if self.right:
            # Successor is in right subtree.
            return self.right.first()
        else:
            # Successor is right ancestor.
            return self.right_ancestor()

    def remove(self):
        """
        Logically removes the current node from the tree.

        This method may keep the structural node and replace it's contents with that of another node.
        """
        if not self.right:
            # No successor. Put left subtree on this place.
            self.delete_node()
        else:
            # Put the successor on this place.
            s = self.successor()
            self.value = s.value
            s.delete_node()

    def delete_node(self):
        """
        Structurally delete current node.

        **Requires:** This node may have at most 1 child. Otherwise use :py:meth:`~bintree.BinNode.remove`.
        """
        if self.right:
            self.tree.replace_child(self, self.right)
        else:
            self.tree.replace_child(self, self.left)

    def search(self, element):
        """
        Searches in the tree to the location of an element.

        Used by the remove method.

        :param element: The element to look for.
        :return: The subtree rooted at searched element or None if it is not found.
        :rtype: BinNode | None
        """
        if self.value == element:
            return self
        if element < self.value:
            return self.left.search(element) if self.left else None
        else:
            return self.right.search(element) if self.right else None

    def first(self):
        """
        Returns the first (leftmost) node in the subtree.

        Used by the successor method and the iterator.

        :return: First (leftmost) node in the subtree.
        :rtype: BinNone
        """
        if self.left:
            return self.left.first()
        else:
            return self

    def last(self):
        """
        Returns the last (rightmost) node in the subtree.

        Currently not used.

        :return: Last (rightmost) node in the subtree.
        :rtype: BinNone
        """
        if self.right:
            return self.right.last()
        else:
            return self

    def __bool__(self):
        """
        A BinNode is always True.

        :return: True
        """
        return True

    def __len__(self):
        """
        Returns the number of elements in this ``BinNode``. This implementation
        traverses the whole tree.
        """
        size = 1
        if self.left:
            size += len(self.left)
        if self.right:
            size += len(self.right)
        return size

    def __str__(self):
        """
        Gives a crude ``__str__`` implementation. For better results use AsciiTreeVisualizer.
        """
        l = self.left.__str__() if self.left else '-'
        r = self.right.__str__() if self.right else '-'
        return "[{} {} {}]".format(l, self.value, r)

    # ---- Wrapper functions ----

    def is_left(self):
        """
        Checks if this node is the left child of its parent.
        Returns False when the node is the root element.
        """
        return BinTree.left_of(self.parent) == self

    def is_right(self):
        """
        Checks if this node is the right child of its parent.
        Returns False when the node is the root element.
        """
        return BinTree.right_of(self.parent) == self

    def attach_left(self, new_node):
        """
        Attaches a new node to the left side of the current node. This
        method also sets the parent of the new child and also works when the
        child is None.

        :param new_node: Node to attach.
        :type new_node: BinNode
        """
        self.left = new_node
        if new_node:
            new_node.parent = self

    def attach_right(self, new_node):
        """
        Attaches a new node to the right side of the current node. This
        method also sets the parent of the new child and also works when the
        child is None.

        :param new_node: Node to attach.
        :type new_node: BinNode
        """
        self.right = new_node
        if new_node:
            new_node.parent = self


class BinTreeIterator:
    """
    The iterator returned by BinNode.__iter__().
    """

    def __init__(self, tree):
        """
        Constructs a new Iterator for the given BinTree.

        :type tree : BinTree
        """
        self.curr = None
        """
        Where are we now
        :type : BinNode | None
        """

        self.next = tree.root.first() if tree.root else None
        """
        Where are we heading
        :type : BinNode | None
        """

    def __iter__(self):
        """
        Return the iterator object itself.

        Required by Python.

        :rtype: BinTreeIterator
        """
        return self

    def __next__(self):
        """
        Returns the next element in the tree.
        """
        if not self.next:
            raise StopIteration

        self.curr = self.next
        """:type : BinNode"""
        self.next = self.curr.successor()
        return self.curr.value
