"""Merge unique cores for M-174 through M-1036."""

from __future__ import annotations

from rest_de import facts as facts_de
from rest_fgh import facts as facts_fgh
from rest_ijk import facts as facts_ijk
from rest_lmn import facts as facts_lmn
from rest_opq import facts as facts_opq
from rest_rst import facts as facts_rst
from rest_uvwxy import facts as facts_uvwxy


def facts() -> dict[int, dict]:
    F: dict[int, dict] = {}
    for loader in (
        facts_de,
        facts_fgh,
        facts_ijk,
        facts_lmn,
        facts_opq,
        facts_rst,
        facts_uvwxy,
    ):
        chunk = loader()
        overlap = set(F) & set(chunk)
        if overlap:
            raise RuntimeError(f"overlapping skill cores: {sorted(overlap)[:12]}")
        F.update(chunk)
    return F
