#!/usr/bin/python3

def safe_function(fct, *args):
    """Executes a function safely"""
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception:", e, file=sys.stderr)
        return (None)
