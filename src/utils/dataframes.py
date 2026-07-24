"""Small dataframe helpers shared by encoding / leveling notebooks."""

from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple

import numpy as np
import pandas as pd

from .sequences import LEVEL_NAME_TO_ID, LEVEL_NAMES, VALID_AA_PATTERN


def pick_col(df: pd.DataFrame, candidates: Sequence[str], label: str) -> str:
    """Return the first column name that exists in `df`."""
    for col in candidates:
        if col in df.columns:
            return col
    raise KeyError(
        f"Missing {label}. Tried {list(candidates)}. Have: {list(df.columns)}"
    )


def filter_aa_pairs(
    sequences: Iterable[str],
    organisms: Iterable[str],
    levels: Iterable[int] | None = None,
) -> Tuple[List[str], List[str], List[int] | None, int]:
    """Keep only standard-AA sequences. Returns (seqs, orgs, levels|None, n_dropped)."""
    seqs: List[str] = []
    orgs: List[str] = []
    lvls: List[int] | None = [] if levels is not None else None
    dropped = 0
    level_list = list(levels) if levels is not None else None

    for i, (seq, org) in enumerate(zip(sequences, organisms)):
        if VALID_AA_PATTERN.match(str(seq)):
            seqs.append(seq)
            orgs.append(org)
            if lvls is not None and level_list is not None:
                lvls.append(level_list[i])
        else:
            dropped += 1
    return seqs, orgs, lvls, dropped


def parse_level_column(df: pd.DataFrame) -> Tuple[np.ndarray, str]:
    """Parse Weak/Moderate/Strong labels from a dataframe column."""
    for col in ("potency_level", "label", "level"):
        if col not in df.columns:
            continue
        raw = df[col].astype(str).str.strip()
        ids, bad = [], set()
        for val in raw:
            key = val.lower()
            if key in LEVEL_NAME_TO_ID:
                ids.append(LEVEL_NAME_TO_ID[key])
            else:
                bad.add(val)
        if bad:
            raise ValueError(
                f"Unknown levels in '{col}': {sorted(bad)}. Expected {LEVEL_NAMES}"
            )
        return np.array(ids, dtype=np.int64), col
    raise KeyError(
        "Leveled encoder needs a potency_level column. "
        "Run notebooks/01_potency_leveling.ipynb first."
    )
