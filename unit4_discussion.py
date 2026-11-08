
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start at the root and let recursion find the
        # correct location for the new equipment ID.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # An empty position means we can create a new node.
        if node is None:
            return Node(value)

        # Smaller equipment IDs belong on the left.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger equipment IDs belong on the right.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate IDs are ignored so each ID stays unique.
        else:
            return node

        # Return the updated node to maintain the tree.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can skip an entire subtree after comparing
        # values instead of checking every item in order.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Reaching an empty position means the ID is missing.
        if node is None:
            return False

        # The requested equipment ID was found.
        if value == node.value:
            return True

        # Search only the subtree that could contain the ID.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # An empty node has nothing to visit.
        if node is None:
            return

        # Left subtree contains smaller values.
        self._inorder_recursive(node.left, values)

        # Visit the current equipment ID.
        values.append(node.value)

        # Right subtree contains larger values.
        self._inorder_recursive(node.right, values)

        # Left, root, right produces ascending sorted IDs.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Equipment inventory example:
    # Each number represents a unique equipment ID.
    equipment_ids = [1050, 1025, 1075, 1010, 1040, 1060, 1090]

    inventory = BST()

    for equipment_id in equipment_ids:
        inventory.insert(equipment_id)

    print("Equipment IDs inserted:", equipment_ids)

    # A balanced BST reduces the search space at each level.
    # Instead of checking every ID, the program chooses
    # the left or right subtree based on the target value.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_ids = inventory.inorder()
    print("Equipment IDs in sorted order:", sorted_ids)

    # In-order traversal visits left, root, then right.
    # This prints equipment IDs from smallest to largest.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Existing IDs should return True.
    print("Search for 1025:", inventory.search(1025))
    print("Search for 1090:", inventory.search(1090))

    # Missing IDs should return False.
    print("Search for 1030:", inventory.search(1030))
    print("Search for 1100:", inventory.search(1100))

    # The search follows only one possible path through
    # the tree instead of scanning every equipment ID.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: An empty tree has no values to traverse.
    empty_tree = BST()
    print("Empty tree traversal:", empty_tree.inorder())

    # Searching an empty tree returns False.
    print("Search empty tree:", empty_tree.search(1050))

    # Edge case 2: Inserting a duplicate should not
    # create a second node with the same equipment ID.
    inventory.insert(1025)
    print("After duplicate insertion:", inventory.inorder())

    # Edge case 3: A tree with only one node still works.
    single_tree = BST()
    single_tree.insert(2000)

    print("Single-node tree:", single_tree.inorder())
    print("Search single-node tree:", single_tree.search(2000))

    # Insertion order affects the tree's shape.
    # Sequential insertion can create an unbalanced tree
    # with O(n) search time, while a balanced BST usually
    # supports searching in O(log n) time.


if __name__ == "__main__":
    main()
