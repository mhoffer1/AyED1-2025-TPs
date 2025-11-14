import ast

def remove_docstrings(node):
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            nuevos_items = []
            for item in value:
                if (isinstance(item, ast.Expr)
                    and isinstance(item.value, ast.Constant)
                    and isinstance(item.value.value, str)):
                    continue
                if isinstance(item, ast.AST):
                    remove_docstrings(item)
                nuevos_items.append(item)
            setattr(node, field, nuevos_items)
        elif isinstance(value, ast.AST):
            remove_docstrings(value)

def eliminar_comentarios(codigo):
    tree = ast.parse(codigo)
    remove_docstrings(tree)      
    return ast.unparse(tree)

codigo_ejemplo = '''
def ejemplo():
    """Esta es una función de ejemplo"""
    x = 10  # Asignar valor a x
    y = 20  # Asignar valor a y
    return x + y  # Devolver la suma
'''

codigo_limpio = eliminar_comentarios(codigo_ejemplo)
print("codigo original:")
print(codigo_ejemplo)
print("codigo sin comentarios/docstrings:")
print(codigo_limpio)