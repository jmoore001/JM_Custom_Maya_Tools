import os
import sys
import maya.cmds as cmds

# JM_Custom_Maya_Tools installer / bootstrap
# - Resolves paths without relying on Maya version folders
# - Stores repo root in optionVar "JMDirectory"
# - Adds a shelf button + marking menu and runs initialization

# Infer repo root from this Setup.py location.
# Note: if you *copy/paste* this file into Maya's Script Editor, __file__ won't exist.
# In that case we fall back to a saved optionVar, or we ask you to locate the toolkit once.
def _resolve_repo_root():
    # 1) Normal path: running from the file on disk
    try:
        return os.path.dirname(__file__)
    except NameError:
        pass

    # 2) If previously installed, we stored it here
    try:
        if cmds.optionVar(exists="JMDirectory"):
            return cmds.optionVar(q="JMDirectory")
    except Exception:
        pass

    # 3) Ask user to locate Setup.py (one-time)
    try:
        picked = cmds.fileDialog2(
            fileMode=1,
            caption="Locate JM_Custom_Maya_Tools Setup.py",
            fileFilter="Python Files (*.py)"
        )
        if picked:
            return os.path.dirname(picked[0])
    except Exception:
        pass

    raise RuntimeError(
        "JM Tools: Can't resolve toolkit folder. "
        "Run Setup.py by importing it from disk, or locate it when prompted."
    )

REPO_ROOT = os.path.normpath(_resolve_repo_root())
SCRIPTS_DIR = os.path.join(REPO_ROOT, "Scripts").replace('\\', '/')
ICONS_DIR = os.path.join(REPO_ROOT, "Icons").replace('\\', '/')

cmds.optionVar(sv=("JMDirectory", REPO_ROOT))

if SCRIPTS_DIR not in sys.path:
    sys.path.append(SCRIPTS_DIR)

import jm_path  # noqa: E402
jm_path.set_optionvar(REPO_ROOT)
jm_path.ensure_sys_path()

import Edits  # noqa: E402
import InitilizeTools  # noqa: E402
import JMCustomMarkingMenu  # noqa: E402

# Copy userSetup.mel into the active Maya version scripts folder (optional convenience)
src_mel = os.path.join(SCRIPTS_DIR, "userSetup.mel").replace('\\', '/')
dest_dir = cmds.internalVar(userScriptDir=True)  # ends in /scripts/
dest_mel = os.path.join(dest_dir, "userSetup.mel").replace('\\', '/')

if os.path.exists(dest_mel):
    cmds.warning(
        "userSetup.mel already exists in your Maya scripts folder. "
        "If you want JM tools auto-loaded on startup, copy the contents of "
        f"{src_mel} into {dest_mel}."
    )
else:
    try:
        cmds.sysFile(src_mel, copy=dest_mel)
    except Exception as e:
        cmds.warning(f"Could not copy userSetup.mel: {e}")

# Add shelf button
icon = os.path.join(ICONS_DIR, "CustomToolsIcon.png").replace('\\', '/')

command = (
    "import sys\n"
    "import jm_path\n"
    "jm_path.ensure_sys_path()\n"
    "import InitilizeTools\n"
    "InitilizeTools.CustomToolsJM()\n"
)

Edits.Edits.AddButtonToShelf("JMTools", command, icon)

# Build marking menu + open main tool UI
JMCustomMarkingMenu.JMCustomToolsMarkingMenu()
InitilizeTools.CustomToolsJM()
