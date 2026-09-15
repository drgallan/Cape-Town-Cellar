#!/usr/bin/env python3
"""
Build both Cape Cellar apps from source into self-contained pages.

    python3 src/build.py

Writes:
    index.html          phone app (the site's entry point)
    desk/index.html     desktop workbench

Every asset (1,805 wines, the Barlow Condensed subsets, the winelands map,
React and the DC runtime) is inlined, so each output is a single file that
opens offline and makes no network request until you tap Satellite.
"""

import base64
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

WEIGHTS = ("400", "500", "600")
SUBSETS = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,"
                  "U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin-ext":  "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,"
                  "U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,"
                  "U+2113,U+2C60-2C7F,U+A720-A7FF",
    "latin":      "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,"
                  "U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,"
                  "U+FEFF,U+FFFD",
}
# The desktop build skips Vietnamese: no wine or producer name in the report needs it.
DESK_SUBSETS = ("latin-ext", "latin")


def read(name, binary=False):
    with open(os.path.join(HERE, name), "rb" if binary else "r",
              encoding=None if binary else "utf-8") as fh:
        return fh.read()


def b64(name):
    return base64.b64encode(read(name, binary=True)).decode()


def face(weight, subset):
    src = b64("fonts/barlow-condensed-%s-%s.woff2" % (weight, subset))
    return ("@font-face{font-family:'Barlow Condensed';font-style:normal;font-weight:%s;"
            "font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');"
            "unicode-range:%s}" % (weight, src, SUBSETS[subset]))


def fontcss(subsets):
    return "\n".join(face(w, s) for w in WEIGHTS for s in subsets)


def script(name):
    """Inline a JS file, refusing anything that would close the script tag early."""
    js = read(name)
    assert "</script" not in js.lower(), "%s contains a script-closing sequence" % name
    return js


def wines():
    keep = ("n", "v", "r", "st", "s", "p", "f", "t", "vr", "fr", "d", "pr", "id")
    data = json.loads(read("wines.json"))
    trimmed = [{k: w[k] for k in keep} for w in data]
    return json.dumps(trimmed, ensure_ascii=False, separators=(",", ":"))


def region_groups():
    raw = re.search(r"window\.REGION_GROUPS=(\[.*?\]);", read("regions.js"), re.S).group(1)
    return json.dumps(json.loads(re.sub(r"(\w+):", r'"\1":', raw)),
                      ensure_ascii=False, separators=(",", ":"))


def build_desk():
    html = read("desk.src.html")
    html = html.replace("__FONTS__", fontcss(DESK_SUBSETS))
    html = html.replace("__WINES__", wines())
    html = html.replace("__GROUPS__", region_groups())
    html = html.replace("__MAP__", "data:image/png;base64," + b64("map.png"))
    for token in ("__FONTS__", "__WINES__", "__GROUPS__", "__MAP__"):
        assert token not in html, "unsubstituted %s" % token
    head, body = html.split("</style>", 1)
    page = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>")
    write_out("desk/index.html", page)


def build_mobile():
    html = read("mobile.dc.html")
    # The artboard loads its assets by filename; inline each one in place.
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>',
                  "<style>" + fontcss(SUBSETS) + "</style>", html)
    html = html.replace('src="map.png"',
                        'src="data:image/png;base64,%s"' % b64("map.png"))
    html = html.replace('<script src="wines.js"></script>',
                        "<script>%s</script>" % script("wines.js"))
    html = html.replace('<script src="regions.js"></script>',
                        "<script>%s</script>" % script("regions.js"))
    # React must exist before the DC runtime boots, or it fetches it from a CDN.
    html = html.replace(
        '<script src="dc-runtime.js"></script>',
        "<script>%s</script>\n<script>%s</script>\n"
        "<script>window.__resources={};</script>\n<script>%s</script>"
        % (script("react.production.min.js"),
           script("react-dom.production.min.js"),
           script("dc-runtime.js")))
    assert 'script src="' not in html, "an asset was left as an external reference"
    write_out("index.html", html)


def write_out(relpath, text):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("%-20s %6.2f MB" % (relpath, len(text.encode()) / 1e6))


if __name__ == "__main__":
    build_desk()
    build_mobile()
