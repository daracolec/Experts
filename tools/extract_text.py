#!/usr/bin/env python3
"""Print the readable text of .docx, .pptx, .xlsx, .pdf, .md or .txt files.

Usage: python3 tools/extract_text.py <file> [<file> ...]
"""
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


def docx_text(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf8", "ignore")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:tab/>", "\t", xml)
    return re.sub(r"<[^>]+>", "", xml)


def pptx_text(path):
    out = []
    with zipfile.ZipFile(path) as z:
        slides = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        slides.sort(key=lambda n: int(re.search(r"(\d+)", n.rsplit("/", 1)[1]).group(1)))
        for name in slides:
            xml = z.read(name).decode("utf8", "ignore")
            xml = re.sub(r"</a:p>", "\n", xml)
            out.append(f"--- {name.rsplit('/', 1)[1]}\n" + re.sub(r"<[^>]+>", "", xml))
    return "\n".join(out)


def xlsx_text(path):
    import openpyxl

    wb = openpyxl.load_workbook(path, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"===== SHEET: {ws.title} ({ws.dimensions}) =====")
        for row in ws.iter_rows(values_only=True):
            if any(v is not None for v in row):
                out.append(" | ".join("" if v is None else str(v) for v in row))
    return "\n".join(out)


def pdf_text(path):
    if shutil.which("pdftotext"):
        return subprocess.run(
            ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True
        ).stdout
    from pypdf import PdfReader

    return "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)


READERS = {".docx": docx_text, ".pptx": pptx_text, ".xlsx": xlsx_text, ".pdf": pdf_text}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for arg in sys.argv[1:]:
        path = Path(arg)
        reader = READERS.get(path.suffix.lower())
        print(f"\n######## {path.name} ########")
        if reader:
            print(reader(path))
        else:
            print(path.read_text(errors="ignore"))


if __name__ == "__main__":
    main()
