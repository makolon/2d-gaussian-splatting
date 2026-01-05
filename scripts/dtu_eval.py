import runpy

if __name__ != "__main__":
    from twodgs.scripts.dtu_eval import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.dtu_eval", run_name="__main__")
