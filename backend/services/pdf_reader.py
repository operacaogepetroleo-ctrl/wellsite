from __future__ import annotations
from pathlib import Path
import re
import fitz  # PyMuPDF

def _clean_text(t: str) -> str:
    # remove hyphenations at line breaks: perfura- \n ção -> perfuração
    t = re.sub(r"-\n", "", t)
    # join wrapped lines where a line ends without punctuation
    t = re.sub(r"\n(?=[a-z0-9])", " ", t, flags=re.IGNORECASE)
    # normalize multiple spaces
    t = re.sub(r"[ \t]+", " ", t)
    # keep newlines between sections
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

def extract_text_from_pdf(path: str | Path, max_pages: int | None = None) -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(str(path))

    texts = []
    with fitz.open(str(path)) as doc:
        for i, page in enumerate(doc):
            if max_pages is not None and i >= max_pages:
                break
            txt = page.get_text("text") or ""
            texts.append(_clean_text(txt))

    return "\n\n".join([t for t in texts if t]).strip()
# NOVO: ler PDF direto de bytes (sem salvar em disco)
def extract_text_from_pdf_bytes(data: bytes, max_pages: int | None = None) -> str:
    import fitz  # PyMuPDF
    import re
    def _clean_text(t: str) -> str:
        t = re.sub(r"-\n", "", t)
        t = re.sub(r"\n(?=[a-z0-9])", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n{3,}", "\n\n", t)
        return t.strip()

    texts = []
    with fitz.open(stream=data, filetype="pdf") as doc:
        for i, page in enumerate(doc):
            if max_pages is not None and i >= max_pages:
                break
            txt = page.get_text("text") or ""
            texts.append(_clean_text(txt))
    return "\n\n".join([t for t in texts if t]).strip()
