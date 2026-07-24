"""Peptide sequence validation and potency-level helpers."""

from __future__ import annotations

import re
from typing import Optional

# Alphabet used by the TransVAE / diffusion notebooks
VALID_AA_PATTERN = re.compile(r"^[GALVIMFWPSTCYHNQDEKR]+$")
VALID_AAS = set("ACDEFGHIKLMNPQRSTVWY")

LEVEL_NAMES = ["Weak", "Moderate", "Strong"]
LEVEL_NAME_TO_ID = {"weak": 0, "moderate": 1, "strong": 2}

DEFAULT_ORGANISM_MAP = [
    "A. baumannii",
    "B. subtilis",
    "E. coli",
    "E. faecalis",
    "K. pneumoniae",
    "P. aeruginosa",
    "S. aureus",
    "S. enterica",
    "S. epidermidis",
]


def is_valid_peptide(seq: str, min_len: int = 1, alphabet: Optional[str] = None) -> bool:
    """Return True if `seq` only contains allowed amino acids."""
    if seq is None:
        return False
    s = str(seq).strip().upper()
    if len(s) < min_len:
        return False
    if alphabet is None:
        return bool(VALID_AA_PATTERN.fullmatch(s))
    allowed = set(alphabet.upper())
    return all(c in allowed for c in s)


def resolve_level_id(
    num_levels: int,
    level_null: Optional[int],
    potency_level: Optional[str] = None,
) -> Optional[int]:
    """Map a potency label to an embedding id, or None if leveling is off."""
    if num_levels <= 0:
        return None
    if potency_level is None:
        return level_null
    key = str(potency_level).strip().lower()
    if key in ("null", "none", ""):
        return level_null
    if key in LEVEL_NAME_TO_ID:
        return LEVEL_NAME_TO_ID[key]
    if key.isdigit():
        return int(key)
    raise ValueError(
        f"Unknown POTENCY_LEVEL {potency_level!r}. Use Weak, Moderate, Strong, or None"
    )
