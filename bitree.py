import time

class Bitree_node(object):
    def __init__(self, item, lchild=None, rchild=None):
        self.data = item
        self.lchild = lchild
        self.rchild = rchild

    def insert_lchild(self, item):
        self.lchild = Bitree_node(item)
        return self.lchild

    def insert_rchild(self, item):
        self.rchild = Bitree_node(item)
        return self.rchild


def log_time(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    print time.time() - start


def pre_search(bitree, preord=[]):
    if bitree is not None:
        preord.append(bitree.data)
        pre_search(bitree.lchild, preord)
        pre_search(bitree.rchild, preord)
    return preord


def in_search(bitree, inord=[]):
    if bitree is not None:
        in_search(bitree.lchild, inord)
        inord.append(bitree.data)
        in_search(bitree.rchild, inord)
    return inord


def pre_in_order(preord, inord, pre_s, pre_t, in_s, in_t, parent = None, left = True):
    if parent is None:
        cr = Bitree_node(preord[pre_s])
    elif left:
        cr = parent.insert_lchild(preord[pre_s])
    else:
        cr = parent.insert_rchild(preord[pre_s])
    if preord[pre_s] in inord[in_s:in_t + 1]:
        root = inord.index(preord[pre_s])
    else:
        print 'inorder is wrong'
        return
    if not (root == in_s):
        pre_in_order(preord, inord, pre_s + 1, pre_s + root - in_s, in_s, root - 1, cr, left = True)
    if not (root == in_t):
        pre_in_order(preord, inord, pre_s + root - in_s + 1, pre_t, root + 1, in_t, cr, left = False)
    return cr


def invert_bitree(bitree):
    if bitree:
        bitree.lchild, bitree.rchild = bitree.rchild, bitree.lchild
        invert_bitree(bitree.lchild)
        invert_bitree(bitree.rchild)


def nr_in_search(bitree, inord=[]):
    if not bitree:
        return
    stack = []
    crt_node = bitree
    stack.append(crt_node)
    while stack:
        print crt_node.data
        if crt_node.lchild and (crt_node.lchild.data not in inord):
            # lchild exists
            crt_node = crt_node.lchild
            stack.append(crt_node)
        else:
            if crt_node.data not in inord:
                inord.append(crt_node.data)
            # output current node
            if crt_node.rchild and (crt_node.rchild.data not in inord):
                crt_node = crt_node.rchild
                stack.append(crt_node)
            else:
                stack.pop()
                if stack:
                    crt_node = stack[-1]
    return inord


def nr_in_search2(bitree, inord=[]):
    if not bitree:
        return
    stack = []
    crt_node = bitree
    while stack or crt_node:
        if crt_node:
            stack.append(crt_node)
            crt_node = crt_node.lchild
        else:
            crt_node = stack.pop()
            print crt_node.data
            inord.append(crt_node.data)
            crt_node = crt_node.rchild
    return inord


def nr_pre_search(bitree, preord=[]):
    if not bitree:
        return
    stack = []
    crt_node = bitree
    while stack or crt_node:
        if crt_node:
            stack.append(crt_node)
            preord.append(crt_node.data)
            crt_node = crt_node.lchild
        else:
            crt_node = stack.pop()
            crt_node = crt_node.rchild
    return preord


# def nr_post_search(bitree, aftord=[]):
#     if not bitree:
#         return
#     stack = []
#     crt_node = bitree
#     while stack or crt_node:
#         if crt_node:
#             stack.append(crt_node)
#             crt_node = crt_node.lchild
#         else:
#             crt_node = stack[-1]
#             if not crt_node.rchild:
#                 aftord.append(stack.pop().data)
#             crt_node = crt_node.rchild
#             else:













