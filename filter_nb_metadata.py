#!/usr/bin/env python3

import sys
import json

nb = json.load(sys.stdin)
for cell in nb['cells']:
    if 'metadata' in cell:
        cell['metadata'] = {k: v for k, v in cell['metadata'].items() if k != 'jp-MarkdownHeadingCollapsed'}

json.dump(nb, sys.stdout, sort_keys=True, indent=1, ensure_ascii=False)
