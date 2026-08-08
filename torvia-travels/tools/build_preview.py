"""Builds a single self-contained preview file: CSS, JS and every image inlined.

Run from the site folder:  python3 tools/build_preview.py
Output: torvia-preview.html  (one file, works with no other files next to it)
"""
import base64
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
css = (root / "style.css").read_text()
js = (root / "script.js").read_text()


def data_uri(rel_path):
    raw = (root / rel_path).read_bytes()
    b64 = base64.b64encode(raw).decode()
    return f"data:image/svg+xml;base64,{b64}"


# images referenced from the stylesheet
css = re.sub(r'url\("(img/[^"]+)"\)', lambda m: f'url("{data_uri(m.group(1))}")', css)

# images referenced from the markup
html = re.sub(r'src="(img/[^"]+)"', lambda m: f'src="{data_uri(m.group(1))}"', html)

# inline the stylesheet and script so the file stands alone
html = html.replace('<link rel="stylesheet" href="style.css">', f"<style>\n{css}\n</style>")
html = html.replace('<script src="script.js"></script>', f"<script>\n{js}\n</script>")

out = root / "torvia-preview.html"
out.write_text(html)
print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB)")
assert "img/" not in out.read_text(), "some image reference was not inlined"
print("all images inlined")
