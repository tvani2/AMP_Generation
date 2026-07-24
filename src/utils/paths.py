"""Canonical project paths.

Notebooks and scripts should import from here instead of hard-coding
Google Drive / Colab paths. Override with environment variables when needed.
"""

from __future__ import annotations

import os
from pathlib import Path

# Repository root: …/final
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Allow Colab / cluster overrides without editing code
_DATA_OVERRIDE = os.environ.get("AMP_DATA_DIR")
_CKPT_OVERRIDE = os.environ.get("AMP_CHECKPOINTS_DIR")
_RESULTS_OVERRIDE = os.environ.get("AMP_RESULTS_DIR")

DATA_DIR = Path(_DATA_OVERRIDE) if _DATA_OVERRIDE else PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR = DATA_DIR / "external"

CHECKPOINTS_DIR = (
    Path(_CKPT_OVERRIDE) if _CKPT_OVERRIDE else PROJECT_ROOT / "checkpoints"
)
RESULTS_DIR = Path(_RESULTS_OVERRIDE) if _RESULTS_OVERRIDE else PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
TABLES_DIR = RESULTS_DIR / "tables"

# Common artifact names (fill in once files exist locally / on Drive)
VOCAB_PATH = DATA_DIR / "peptide_vocab.pkl"
WEIGHT_PATH = DATA_DIR / "peptide_weight.npy"
VAE_WEIGHTS_PATH = CHECKPOINTS_DIR / "vae_weights.pth"


def ensure_dir(path: Path) -> Path:
    """Create a directory if missing and return it."""
    path.mkdir(parents=True, exist_ok=True)
    return path
