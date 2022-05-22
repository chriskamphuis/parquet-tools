import sys
if '-m' not in sys.argv:
    from .head import Head

__all__ = ['Head']
