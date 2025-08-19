# backend/services/pdf_reader.py
from __future__ import annotations
import re
from pathlib import Path

def _clean_text(t: str) -> str:
    t = re.sub(r"-\n", "", t)                   # des-hifeniza no fim de linha
    t = re.sub(r"\n(?=[a-z0-9])", " ", t, flags=re.IGNORECASE)  # quebra ruim
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

def extract_text_from_pdf(path: str | Path, max_pages: int | None = None) -> str:
    import fitz  # lazy import
    path = Path(path)
    texts = []
    with fitz.open(path) as doc:
        for i, page in enumerate(doc):
            if max_pages is not None and i >= max_pages: break
            txt = page.get_text("text") or ""
            texts.append(_clean_text(txt))
    return "\n\n".join([t for t in texts if t]).strip()

def extract_text_from_pdf_bytes(data: bytes, max_pages: int | None = None) -> str:
    import fitz  # lazy import
    texts = []
    with fitz.open(stream=data, filetype="pdf") as doc:
        for i, page in enumerate(doc):
            if max_pages is not None and i >= max_pages: break
            txt = page.get_text("text") or ""
            texts.append(_clean_text(txt))
    return "\n\n".join([t for t in texts if t]).strip()
