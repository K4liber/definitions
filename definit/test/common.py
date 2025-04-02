from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class _Const:
    PACKAGE_ROOT_DIR: Path = Path(__file__).parent.parent


CONST = _Const()
