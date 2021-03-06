import os

path, file = os.path.split(__file__)
imports = os.listdir(path)
imports = [x.split('.py')[0] for x in imports if not x.startswith('_') and x.endswith('.py')]
imports = ['from .%s import %s' % (x, x) for x in imports]
imports = ['# This file was autogenerated. To add new imports use %s' % file.split('/')[-1]] + imports
imports = '\n'.join(imports)

with open(os.path.join(path, '__init__.py'), 'w') as fp:
    fp.write(imports + '\n')
