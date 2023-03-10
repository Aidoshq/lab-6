import os
fn = input()
if os.path.exists(fn):
    os.remove(fn)
else:
    print('file does not exist')
