class tree_node: 

    value = None 

    left_child = None 

    right_child = None 

 

    def __init__(self, v, l=None, r=None): 

        self.value = v 

        self.left_child = l 

        self.right_child = r 

 

    def add_child(self, v): 

        if v < self.value: 

            if self.left_child == None: 

                self.left_child = tree_node(v) 

            else: 

                self.left_child.add_child(v) 

        else: 

            if self.right_child == None: 

                self.right_child = tree_node(v) 

            else: 

                self.right_child.add_child(v) 

 

    def is_in_subtree(self, v): 

        if v == self.value: 

            return True 

 

        if v < self.value and self.left_child != None: 

            return self.left_child.is_in_subtree(v) 

 

        elif self.right_child != None: 

            return self.right_child.is_in_subtree(v) 

 

        return False 

 

    def size(self): 

        size = 1 

 

        if self.left_child != None: 

            size += self.left_child.size() 

 

        if self.right_child != None: 

            size += self.right_child.size() 

 

        return size 

 

    def generate_subtree_inorder(self): 

        subtree = [] 

 

        if self.left_child != None: 

            subtree.append(self.left_child.generate_subtree_inorder()) 

 

        subtree.append(f"{self.value}") 

 

        if self.right_child != None: 

            subtree.append(self.right_child.generate_subtree_inorder()) 

 

        return ", ".join(subtree) 

 

    def __str__(self): 

        return f"({self.value},{self.left_child!=None},{self.right_child!=None})" 

 

class binary_search_tree: 

    root = None 

 

    def add_value(self, value): 

        if self.root == None: 

            self.root = tree_node(value) 

 

        else: 

            self.root.add_child(value) 

 

    def is_in_tree(self, value): 

        if self.root == None: 

            return False 

 

        return self.root.is_in_subtree(value) 

 

    def size(self): 

        if self.root == None: 

            return 0 

 

        return self.root.size() 

 

    def __str__(self): 

        # how to visit all nodes? 

        if self.root == None: 

            return "T[]" 

 

        return f"T[{self.root.generate_subtree_inorder()}]" 
