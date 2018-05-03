#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:29:38 2018

@author: anthony
"""

import ast


#from collections import defaultdict
#
#class AstGraphGenerator(object):
#
#    def __init__(self, source):
#        self.graph = defaultdict(lambda: [])
#        self.source = source  # lines of the source code
#
#    def __str__(self):
#        return str(self.graph)
#
#    def _getid(self, node):
#        try:
#            lineno = node.lineno - 1
#            return "%s: %s" % (type(node), self.source[lineno].strip())
#
#        except AttributeError:
#            return type(node)
#
#    def visit(self, node):
#        """Visit a node."""
#        method = 'visit_' + node.__class__.__name__
#        visitor = getattr(self, method, self.generic_visit)
#        return visitor(node)
#
#    def generic_visit(self, node):
#        """Called if no explicit visitor function exists for a node."""
#        for _, value in ast.iter_fields(node):
#            if isinstance(value, list):
#                for item in value:
#                    if isinstance(item, ast.AST):
#                        self.visit(item)
#
#            elif isinstance(value, ast.AST):
#                node_source = self._getid(node)
#                value_source = self._getid(value)
#                self.graph[node_source].append(value_source)
#                # self.graph[type(node)].append(type(value))
#                self.visit(value)
            


def str_node(node):
    if isinstance(node, ast.AST):
        fields = [(name, str_node(val)) for name, val in ast.iter_fields(node) if name not in ('left', 'right')]
        rv = '%s(%s' % (node.__class__.__name__, ', '.join('%s=%s' % field for field in fields))
        return rv + ')'
    else:
        return repr(node)
def ast_visit(node, level=0):
    print('  ' * level + str_node(node))
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    ast_visit(item, level=level+1)
        elif isinstance(value, ast.AST):
            ast_visit(value, level=level+1)


ast_visit(ast.parse('a + b'))


source="""

n=random.randrange(0,1001)
c=1
x=int(input("Essai n°1 : "))

while (x!=n) and (x!=1001):
    if (x<n):
        print("trop petit")
    else:
        print("trop grand")
    c=c+1
    x=int(input("Essai n°"+str(c)+" :"))

if x==n:
    print("Vous avez réussi en ",c,"essais")
else:
    print("Il fallait trouver ",n)
    

"""

ast_visit(ast.parse(source))
