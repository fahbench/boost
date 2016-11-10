want = [
    'filesystem',
    'program_options',
    'system',
]

import shutil
import os
for d in os.listdir('libs'):
    if d in want:
        continue

    if os.path.isdir('libs/{}'.format(d)):
        shutil.rmtree('libs/{}'.format(d))
    else:
        os.remove('libs/{}'.format(d))
