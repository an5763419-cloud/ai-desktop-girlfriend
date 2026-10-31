"""Check the upstream MPFB authoring path in an isolated Blender process."""

import argparse
import importlib
import json
import shutil
import sys
from pathlib import Path

import addon_utils
import bpy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mpfb-source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:])
    source = args.mpfb_source.resolve()
    output = args.output.resolve()
    if not (source / "blender_manifest.toml").is_file():
        raise ValueError("Expected the MPFB src/mpfb directory")
    if output.exists():
        raise FileExistsError("Use a new output directory to preserve prior results")
    output.mkdir(parents=True)

    extension_root = output / "extensions"
    shutil.copytree(source, extension_root / "mpfb")
    bpy.context.preferences.extensions.repos.new(
        name="Character authoring probe",
        module="character_probe",
        custom_directory=str(extension_root),
    )
    module_name = "bl_ext.character_probe.mpfb"
    mpfb = addon_utils.enable(module_name, default_set=True, persistent=False)
    if mpfb is None:
        raise RuntimeError("MPFB registration failed. Check the Blender log.")
    human_service = importlib.import_module(
        module_name + ".services.humanservice"
    ).HumanService
    target_service = importlib.import_module(
        module_name + ".services.targetservice"
    ).TargetService

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    macro = target_service.get_default_macro_info_dict()
    mesh = human_service.create_human(macro_detail_dict=macro)
    rig = human_service.add_builtin_rig(mesh, "game_engine")
    if rig is None or not mesh.vertex_groups or not rig.data.bones:
        raise RuntimeError("MPFB did not produce a weighted rig")
    mesh["asset_status"] = "technical-probe-not-approved-character"
    mesh["source_license"] = "CC0-1.0 (MPFB bundled assets)"
    blend_path = output / "mpfb-rig-probe.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    report = {
        "status": "technical-probe-only",
        "blender": bpy.app.version_string,
        "mpfb": list(mpfb.VERSION),
        "rig_profile": "mpfb-game-engine",
        "vertices": len(mesh.data.vertices),
        "polygons": len(mesh.data.polygons),
        "vertex_groups": len(mesh.vertex_groups),
        "bones": len(rig.data.bones),
        "macro_parameters": macro,
        "blend_file": blend_path.name,
        "not_verified": [
            "approved appearance", "VRM export", "AIRI rendering",
            "speech visemes", "expressions", "chibi proportions",
        ],
    }
    (output / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("CHARACTER_PROBE_RESULT", json.dumps(report))


if __name__ == "__main__":
    main()
