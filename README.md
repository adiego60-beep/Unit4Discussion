# Unit 4 Discussion: Binary Search Trees (BST)

## Project Overview

For this assignment, I created a Binary Search Tree (BST) in Python to organize equipment inventory records using identification numbers. I chose this example because organizing equipment by ID is a practical way to demonstrate how a BST stores and retrieves information.

## Implementation

I created a Node class to store each equipment ID and its left and right child references. I also implemented a BST class with recursive insertion, searching, and in-order traversal methods.

I inserted seven equipment IDs: 1050, 1025, 1075, 1010, 1040, 1060, and 1090. Smaller values were placed in the left subtree, while larger values were placed in the right subtree. Duplicate IDs were ignored to prevent repeated entries.

## Testing and Results

I tested the program by searching for existing and missing equipment IDs. The program returned True for IDs that existed and False for IDs that were not found.

I also tested several edge cases, including an empty tree, duplicate insertion, and a tree containing only one node. These tests demonstrated how the BST handled different situations without producing errors.

The in-order traversal returned the equipment IDs in ascending order:

`[1010, 1025, 1040, 1050, 1060, 1075, 1090]`

## Lessons Learned

I learned how recursive methods allowed the BST to search through connected nodes without examining every value when the tree was balanced. I also learned that insertion order affected the tree's shape and overall efficiency.

One challenge was understanding how recursion determined whether a value belonged in the left or right subtree. Working through the equipment IDs helped me understand how each comparison directed the insertion or search process.

A balanced BST could provide faster searching, typically O(log n), while inserting values in sorted order could create an unbalanced tree with O(n) search time.

Overall, this assignment helped me understand how tree structures could be used to organize and search equipment inventory records.
