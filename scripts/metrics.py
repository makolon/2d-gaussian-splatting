import runpy

if __name__ != "__main__":
    from twodgs.scripts.metrics import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.metrics", run_name="__main__")
