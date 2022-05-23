import sys
if '-m' not in sys.argv:
    from .summary import Head, Tail

__all__ = ['Head', 'Tail']
