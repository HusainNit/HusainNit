import random
from pathlib import Path

out_dir = Path("images/gen")
out_dir.mkdir(parents=True, exist_ok=True)

main_categories = [
    ("compiled", "COMPILED", "#38BDF8"),
    ("interpreted", "INTERPRETED", "#FACC15"),
    ("frontend", "FRONTEND", "#60A5FA"),
    ("backend", "BACKEND", "#4ADE80"),
    ("databases", "DATABASES", "#C084FC"),
    ("cloud-ops", "CLOUD & OPS", "#FB923C"),
    ("version-control", "VERSION CONTROL", "#F97316"),
    ("tools-ides", "TOOLS & IDES", "#94A3B8"),
    ("ecommerce", "E-COMMERCE", "#F472B6"),
    ("ai-agents", "AI AGENTS", "#E879F9"),
]

muted_categories = [
    ("creative-3d", "CREATIVE & 3D"),
    ("discovering", "DISCOVERING"),
]

discover_subgroups = [
    ("disc-langs", "LANGS & WEB"),
    ("disc-cloud", "CLOUD & OPS"),
    ("disc-data", "DATA & QUEUES"),
    ("disc-tools", "TOOLS & MORE"),
]


def jagged_edge_path(width: int, height: int, seed: str, jitter: float = 2.2) -> str:
    """Build a closed jagged edge path around the outer perimeter without inner tint."""
    rng = random.Random(seed)
    pad = 4.0
    x0, y0 = pad, pad
    x1, y1 = width - pad, height - pad

    pts: list[tuple[float, float]] = []

    top_steps = 8
    for i in range(top_steps + 1):
        t = i / top_steps
        x = x0 + t * (x1 - x0)
        dy = rng.uniform(-jitter, jitter) if 0 < i < top_steps else 0.0
        pts.append((round(x, 1), round(y0 + dy, 1)))

    right_steps = 3
    for i in range(1, right_steps + 1):
        t = i / right_steps
        y = y0 + t * (y1 - y0)
        dx = rng.uniform(-jitter, jitter) if i < right_steps else 0.0
        pts.append((round(x1 + dx, 1), round(y, 1)))

    for i in range(top_steps - 1, -1, -1):
        t = i / top_steps
        x = x0 + t * (x1 - x0)
        dy = rng.uniform(-jitter, jitter) if i > 0 else 0.0
        pts.append((round(x, 1), round(y1 + dy, 1)))

    for i in range(right_steps - 1, 0, -1):
        t = i / right_steps
        y = y0 + t * (y1 - y0)
        dx = rng.uniform(-jitter, jitter)
        pts.append((round(x0 + dx, 1), round(y, 1)))

    commands = [f"M {pts[0][0]} {pts[0][1]}"] + [f"L {x} {y}" for x, y in pts[1:]] + ["Z"]
    return " ".join(commands)


def build_header_svg(
    slug: str,
    label: str,
    accent: str,
    width: int = 220,
    height: int = 44,
    muted: bool = False,
) -> str:
    path_d = jagged_edge_path(width, height, seed=f"hdr-{slug}", jitter=2.2 if not muted else 1.7)
    fill_bg = "#0D1117" if muted else "#12161F"
    stroke_color = "#484F58" if muted else accent
    text_color = "#8B949E" if muted else "#F0F6FC"
    font_size = 10.0 if height <= 30 else (11.5 if muted else 13.0)
    font_weight = 700 if muted else 800
    text_y = (height // 2) + 4
    xml_label = label.replace("&", "&amp;")

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="{path_d}" fill="{fill_bg}" stroke="{stroke_color}" stroke-width="1.5" stroke-linejoin="miter"/>
  <text x="{width // 2}" y="{text_y}" text-anchor="middle" fill="{text_color}" font-family="DejaVu Sans, Liberation Sans, Arial, Helvetica, sans-serif" font-size="{font_size}" font-weight="{font_weight}" letter-spacing="1">{xml_label}</text>
</svg>
"""


for slug, label, color in main_categories:
    (out_dir / f"hdr-top-{slug}.svg").write_text(
        build_header_svg(slug, label, color, width=220, height=44, muted=False),
        encoding="utf-8",
    )

for slug, label in muted_categories:
    (out_dir / f"hdr-top-{slug}.svg").write_text(
        build_header_svg(slug, label, "#484F58", width=220, height=44, muted=True),
        encoding="utf-8",
    )

for slug, label in discover_subgroups:
    (out_dir / f"hdr-top-{slug}.svg").write_text(
        build_header_svg(slug, label, "#484F58", width=150, height=28, muted=True),
        encoding="utf-8",
    )

print("Generated jagged-edge SVGs for all categories and Discovering sub-groups.")