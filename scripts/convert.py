import runpy

if __name__ != "__main__":
    from twodgs.scripts.convert import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.convert", run_name="__main__")
