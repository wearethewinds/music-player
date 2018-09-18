from typing import List
from glob import glob
from os.path import join
import hashlib


def list_files_recursive(path: str, extensions: List[str]):
    files_grabbed = []

    for extension in extensions:
        files_grabbed.extend(glob(join(path, '**/' + extension)))

    return files_grabbed

def md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
