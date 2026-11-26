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

# Wider 288px header to span 4x 68px icons per row cleanly
top_centered_tpl = """<svg width="288" height="36" viewBox="0 0 288 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="clip_{id}">
      <rect x="0.5" y="0.5" width="287" height="35" rx="8.5"/>
    </clipPath>
    <linearGradient id="glow_{id}" x1="144" y1="0" x2="144" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#12161F" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#clip_{id})">
    <rect x="0" y="0" width="288" height="36" fill="#12161F"/>
    <rect x="0" y="0" width="288" height="36" fill="url(#glow_{id})"/>
    <rect x="0" y="0" width="288" height="3" fill="{color}"/>
  </g>

  <rect x="0.5" y="0.5" width="287" height="35" rx="8.5" stroke="#262D3A" stroke-width="1"/>

  <text x="144" y="23" text-anchor="middle" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12" font-weight="700" letter-spacing="1.4">{label}</text>
</svg>
"""

# Smaller 168x26 muted dashed header for Creative & Discovering
discovering_muted_tpl = """<svg width="168" height="26" viewBox="0 0 168 26" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" width="167" height="25" rx="7" fill="#0D1117" stroke="#21262D" stroke-dasharray="4 3" stroke-width="1"/>
  <text x="84" y="16.5" text-anchor="middle" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="9.5" font-weight="600" letter-spacing="1.4">{label}</text>
</svg>
"""

for slug, label, color in main_categories:
    safe_id = slug.replace("-", "_")
    xml_label = label.replace("&", "&amp;")
    content = top_centered_tpl.format(
        id=safe_id,
        label=xml_label,
        color=color,
    )
    with open(f"images/gen/hdr-top-{slug}.svg", "w", encoding="utf-8") as f:
        f.write(content)

for slug, label in muted_categories:
    xml_label = label.replace("&", "&amp;")
    content = discovering_muted_tpl.format(label=xml_label)
    with open(f"images/gen/hdr-top-{slug}.svg", "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 288px main headers and 168x26 muted headers.")