"""Path helpers for JM_Custom_Maya_Tools.

Goal: make path resolution robust across Maya versions and OS path separators.
"""

from __future__ import annotations

import os
import maya.cmds as cmds


_OPTIONVAR = "JMDirectory"


def norm(p: str) -> str:
    return os.path.normpath(p).replace('\\', '/')


def get_repo_root() -> str:
    """Return the repo root folder (the folder containing Scripts/ and Icons/)."""
    # 1) Prefer stored optionVar if set and valid
    try:
        if cmds.optionVar(exists=_OPTIONVAR):
            p = cmds.optionVar(q=_OPTIONVAR)
            if p and os.path.isdir(p):
                return norm(p)
    except Exception:
        pass

    # 2) Try to infer from this file's location: <root>/Scripts/jm_path.py
    here = os.path.dirname(__file__)
    candidate = os.path.abspath(os.path.join(here, os.pardir))
    if os.path.isdir(os.path.join(candidate, "Scripts")):
        return norm(candidate)

    # 3) Fallback: Maya user scripts dir -> <maya>/scripts
    try:
        usd = cmds.internalVar(userScriptDir=True)  # more explicit than usd=True
        # userScriptDir ends with /scripts/
        maya_dir = os.path.abspath(os.path.join(usd, os.pardir))
        # If the repo lives under <maya_dir>/JM_Custom_Maya_Tools
        candidate = os.path.join(maya_dir, "JM_Custom_Maya_Tools")
        if os.path.isdir(os.path.join(candidate, "Scripts")):
            return norm(candidate)
    except Exception:
        pass

    raise RuntimeError("Could not resolve JM_Custom_Maya_Tools root folder. Run Setup.py again.")


def get_scripts_dir() -> str:
    return norm(os.path.join(get_repo_root(), "Scripts"))


def get_icons_dir() -> str:
    return norm(os.path.join(get_repo_root(), "Icons"))


def ensure_sys_path() -> str:
    import sys
    scripts_dir = get_scripts_dir()
    if scripts_dir not in sys.path:
        sys.path.append(scripts_dir)
    return scripts_dir


def set_optionvar(path: str) -> None:
    cmds.optionVar(sv=(_OPTIONVAR, norm(path)))
