import runpy

if __name__ != "__main__":
    from twodgs.scripts.render import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.render", run_name="__main__")
