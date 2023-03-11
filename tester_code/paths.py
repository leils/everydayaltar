import os
from pathlib import Path

dirname = os.path.dirname(__file__)
print(dirname)
p = Path(dirname)
parentPath = str(p.parent)
print(parentPath)
source_filename = os.path.join(parentPath, 'shared/source.json')
datastore = os.path.join(parentPath, "shared/data.json")

print(source_filename)
print(datastore)

