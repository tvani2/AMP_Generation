"""Checkpoint loading helpers shared by training / generation notebooks."""

from __future__ import annotations

from typing import Any, Dict, Tuple


def strip_module_prefix(state_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Remove a leading ``module.`` prefix (DataParallel checkpoints)."""
    return {k.replace("module.", "", 1): v for k, v in state_dict.items()}


def load_checkpoint(path: str, device) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Load a raw state dict or a dict with ``model_state`` + metadata."""
    import torch

    checkpoint = torch.load(path, map_location=device)
    metadata: Dict[str, Any] = {}
    if isinstance(checkpoint, dict) and "model_state" in checkpoint:
        for key in ("num_organisms", "null_label", "num_steps", "num_levels", "level_null"):
            if key in checkpoint:
                metadata[key] = int(checkpoint[key])
        checkpoint = checkpoint["model_state"]
    if not isinstance(checkpoint, dict):
        raise TypeError(f"Unsupported checkpoint format in {path}")
    return strip_module_prefix(checkpoint), metadata
