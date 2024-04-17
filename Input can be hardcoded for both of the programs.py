#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question → 1) Write a program of Balancing Brackets, use a suitable data structure to print whether the string entered is a Balanced Brackets or Unbalanced String

Sample input.

( [ [ { } ] ] )

Sample Output

The entered String has Balanced Brackets

Sample Input

( [ [ { } ] ] ) )

Sample Output

The entered Strings do not contain Balanced Brackets

-------------------------------------------------------------------------------------------------------------------------------

                                                                                                                                  MARKS 10
Question 2) Find a pair with a given sum in Binary Search Tree
 
Sum = 130
Pair is (60,70)


If the sum is not found, print nodes are not found.
-------------------------------------------------------------------------------------------------------------------------------



# # Answer – 1

# In[1]:


def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False
    return not stack

def main():
    # Sample input strings
    inputs = [
        "( [ [ { } ] ] )",
        "( [ [ { } ] ] ) )",
        "{ [ ( ) ] }",
        "{ [ ( } ) ]",
        "[ ( { } ) ]",
        "[ ( { } ) ] )",
    ]

    for input_str in inputs:
        if is_balanced(input_str):
            print(f"The entered string '{input_str}' has balanced brackets")
        else:
            print(f"The entered string '{input_str}' does not contain balanced brackets")

if __name__ == "__main__":
    main()


# # Answer – 2

# In[2]:


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root, inorder):
    if root:
        inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        inorder_traversal(root.right, inorder)

def find_pair_with_sum(root, target_sum):
    inorder = []
    inorder_traversal(root, inorder)
    left, right = 0, len(inorder) - 1
    
    while left < right:
        current_sum = inorder[left] + inorder[right]
        if current_sum == target_sum:
            return inorder[left], inorder[right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return None

# Create the BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Find pair with sum
target_sum = 130
pair = find_pair_with_sum(root, target_sum)
if pair:
    print("Pair is:", pair)
else:
    print("Nodes are not found.")


# In[ ]:





# In[ ]:




