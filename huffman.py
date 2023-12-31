string = "ABCAABBDDDCCAABBCCDDAAA"

class NodeTree():
    def __init__(self,left=None, right = None):
        self.left = left
        self.right = right

    def children(self):
        return(self.left, self.right)
    
    def nodes(self):
        return (self.left, self.right)
    
    def __str__(self):
        return "%s_%s"%(self.left, self.right)
    
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l,r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString+'0'))
    d.udpate(huffman_code_tree(r, False, binString+'1'))
    return d
