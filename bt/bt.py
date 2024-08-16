from __future__ import annotations # https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
from dataclasses import dataclass

# TODO mike@carif.io: git repo for these experiments?
# TODO mike@carif.io: try icecream for structured logging; how do you handle dependencies like icecream in python frameworks?

__test__ = dict(test_driver='./test-bt.py', framework='pytest')

@dataclass # implies python 3.7+
class BT:
    
    '''
    Implementation of a binary tree to experiment with tree inversion or mirroring. I wanted to better understand https://levelup.gitconnected.com/google-rejected-max-howell-creator-of-homebrew-for-getting-this-interview-question-wrong-c99324f6fa90

    Learned python dataclasses along the way, sanded some rust off python syntax. How quickly one forgets.
    '''
    
    contents:Any = None # contents of this node
    left:BT = None # left child subtree
    right:BT = None # right child subtree

    def invert(self:BT|NoneType)->BT|NoneType:
        '''
        self.invert() returns an inverted copy of the binary tree self. Null subtrees are encoded as None and returned as None.
        '''

        if self is None: return None # empty binary tree

        # None.invert() throws an exception so you must check that before calling invert. Python needs something like self.left?.invert().
        # Note: invert() makes an inverted copy of self recursively. Recursion is the key to this solution.
        # TODO mike@carif.io: implement with a recursive generator?
        return BT(contents=self.contents, left=self.right.invert() if self.right else None, right=self.left.invert() if self.left else None)
    
