# -*- encoding: utf-8 -*-
from pathlib import Path


def walk_del_temps(root: str, pattern: str, will_del: bool = False) -> int:
    """Walk a directory tree and yield all files that match the given pattern."""
    # walk
    temp_files = Path(root).glob(pattern)
    count = 0
    for temp_file in temp_files:
        count += 1
        # print info
        print(f"{count:4d}: {temp_file.relative_to(root)}")
        # delete
        if temp_file.exists() and will_del:
            temp_file.unlink()
    return count


def cls_mac_temp(root_path: str, will_del: bool = False) -> None:
    """delete temp files of macOS, like .DS_Store  and ._xxx """
    cnt1 = walk_del_temps(root_path, "**/._*", will_del)
    cnt2 = walk_del_temps(root_path, "**/.DS_Store", will_del)
    print(f"total temp files: {cnt1} + {cnt2} = {cnt1 + cnt2}")
