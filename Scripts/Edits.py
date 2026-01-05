import os
import sys
import maya.cmds as cmds
import maya.mel as mel

import jm_path

class Edits:
    """Small Maya UI / shelf helpers.

    NOTE: Keeping the original class name + method signatures for backward compatibility.
    """

    @staticmethod
    def _ensure_paths():
        jm_path.ensure_sys_path()

    @staticmethod
    def GetCurrentShelf():
        """Return the name of the currently selected shelf tab."""
        try:
            return mel.eval('$tmp = $gShelfTopLevel')
        except Exception:
            return None

    @staticmethod
    def AddButtonToShelf(name, command, icon, shelf=None):
        """Create a shelf button if it doesn't already exist."""
        Edits._ensure_paths()

        current_shelf = shelf or Edits.GetCurrentShelf()
        if not current_shelf:
            cmds.warning("Could not determine current shelf.")
            return

        will_create = True
        try:
            existing = cmds.shelfLayout(current_shelf, q=True, ca=True) or []
            for tool in existing:
                try:
                    tool_label = cmds.shelfButton(tool, q=True, label=True)
                    if name == tool_label:
                        will_create = False
                        break
                except Exception:
                    continue
        except Exception:
            existing = []

        if will_create:
            cmds.shelfButton(p=current_shelf, image1=icon, command=command, l=name)
        else:
            cmds.warning(f"{name} already exists on your shelf, this occurrence is ignored")
