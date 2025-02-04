from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value="None"):
        self.value = value
        self.next_value = None
    
    def __repr__(self):
        return self.value

    
class Linked_list:
    
    def __init__(self):
        self.head = None
    
    def append(self, value):
        """
        Add element to linked list
        """
        # TODO: homework
        
        new_node = Node(value)
 
        if self.head is None:
             self.head = new_node
             return
        
        last = self.head
        while (last.next_value):
            last = last.next_value
        
        last.next_value =  new_node
    
    
    def delitem(self, value) -> bool: # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        ans = False
        temp = self.head
        
        if (temp is not None):
            if (temp.value == value):
                self.head = temp.next_value
                temp = None
                ans = True
        

        while(temp is not None):
            if temp.value == value:
                ans = True
                break
                
            prev = temp
            temp = temp.next_value
 
        if(temp == None):
            pass
 
        prev.next_value = temp.next_value
 
        temp = None
        return (ans)

    
    def getitem(self, value) -> Node:
        """
        Search for element and return
        """
        # TODO: homework
        
        temp = self.head
        
        b = Node()
        while(temp is not None):
            if temp.value == value:
                b = temp
            prev = temp
            temp = temp.next_value
        
        return(b)
    
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next_value
        nodes.append("None")
        return " -> ".join(nodes)


def binary_search(input_list: List[Union[int, float, str]]) -> Optional[int, float, str]:
    pass


class BTSNode:
    def __init__(self):
        pass


class BinaryTree:
    def __init__(self):
        pass

    def __getitem__(self, key) -> BTSNode:
        """
        find and return requested node
        """
        pass

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        pass

    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """
        pass
