import runpy

if __name__ != "__main__":
    from twodgs.scripts.eval_tnt.run import *  # noqa: F401,F403
else:
    runpy.run_module("twodgs.scripts.eval_tnt.run", run_name="__main__")
