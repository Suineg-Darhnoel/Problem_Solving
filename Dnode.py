class Dnode:
    """
    Graph Node
    """
    def __init__(self, val, parent=None, child=None):
        self.parents = set()
        self.children = set()
        self.value = val
        # Connect parents and children
        # nodes simultaneously
        if parent is not None:
            self.add_parent(parent)
        if child is not None:
            self.add_child(child)

    def add_parent(self, parent):
        """
        After self adds parent into the parents list
        the added parent also adds self as a child
        """
        self.parents.add(parent)
        if self not in parent.children:
            parent.add_child(self)

    def add_child(self, child):
        """
        After self adds child into the children list
        the added child also adds self as a parent
        """
        self.children.add(child)
        if self not in child.parents:
            child.add_parent(self)

    def __repr__(self):
        dnode = '<Dnode({})> at <{}>\n'
        first_line = dnode.format(self.value, hex(id(self)))
        p_data = [
                    dnode.format(p.value, hex(id(p)))
                    for p in self.parents
                 ]
        c_data = [
                    dnode.format(c.value, hex(id(c)))
                    for c in self.children
                 ]

        parent_info = '--Parents--\n|__' +\
                "|__".join(p_data) if p_data\
                else '(no-parent)\n'
        child_info = "--Children--\n|__" +\
                "|__".join(c_data) if c_data\
                else '(no-child)\n'

        info = first_line + parent_info + child_info
        return info + '*'*15

"""
root --> node1
     --> node2
     <-- node3
node1 --> node2
      --> node3
      <-- root
node2 <-- root
      <-- node1
      <-- node3
node3 --> root
      --> node2
      <-- node1
lnode --> lnode
      <-- lnode
"""
root = Dnode(0)
#node1
node1 = Dnode(1, root)
#node2
node2 = Dnode(2, root)
node2.add_parent(node1)
#node3
node3 = Dnode(3, node1, root)
node3.add_child(node2)
#loopnode
lnode = Dnode(4)
lnode.add_child(lnode)
