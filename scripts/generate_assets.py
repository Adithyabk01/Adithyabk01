import os
import math

ASSETS_DIR = r"c:\Users\adith\Adithyabk01\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# ----------------------------------------------------
# 1. HERO BANNERS
# ----------------------------------------------------

def generate_hero_svg(filename, is_dark=True):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    border_color = "#30363d" if is_dark else "#e1e4e8"
    title_color = "#f0f6fc" if is_dark else "#1f2328"
    accent_start = "#38bdf8" if is_dark else "#0284c7"
    accent_end = "#818cf8" if is_dark else "#4f46e5"
    sub_color = "#8b949e" if is_dark else "#57606a"
    grid_stroke = "rgba(56, 189, 248, 0.07)" if is_dark else "rgba(2, 132, 199, 0.05)"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="200" style="background:{bg_color}; border-radius: 12px;">
  <defs>
    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_start}" />
      <stop offset="100%" stop-color="{accent_end}" />
    </linearGradient>
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent_start}" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{accent_end}" stop-opacity="0.1"/>
    </linearGradient>
    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .hero-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-weight: 800;
        font-size: 42px;
        fill: url(#title-grad);
      }}
      .hero-subtitle {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-weight: 500;
        font-size: 18px;
        fill: {sub_color};
      }}
      .typewriter-text {{
        font-family: "Fira Code", "Courier New", Courier, monospace;
        font-size: 16px;
        font-weight: 600;
        fill: {accent_start};
      }}
      .cursor {{
        animation: blink 1s infinite;
        fill: {accent_start};
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
    </style>
  </defs>

  <!-- Background Card & Grid -->
  <rect width="800" height="200" rx="12" fill="{bg_color}" stroke="url(#border-grad)" stroke-width="1.5"/>
  <rect width="800" height="200" rx="12" fill="url(#grid)" />

  <!-- Decorative Corner Glows -->
  <circle cx="0" cy="0" r="140" fill="{accent_start}" opacity="0.08" filter="blur(20px)" />
  <circle cx="800" cy="200" r="140" fill="{accent_end}" opacity="0.08" filter="blur(20px)" />

  <!-- Content Group centered -->
  <g transform="translate(400, 70)" text-anchor="middle">
    <text y="0" class="hero-title">Adithya B K</text>
    <text y="36" class="hero-subtitle">AI/ML Enthusiast • Full-Stack Developer • Data Analytics Explorer</text>
    
    <!-- Code / Typing Banner -->
    <g transform="translate(0, 72)">
      <rect x="-240" y="-22" width="480" height="36" rx="18" fill="{bg_color}" stroke="{border_color}" stroke-width="1"/>
      <text x="0" y="2" class="typewriter-text" text-anchor="middle">⚡ Building Practical &amp; Intelligent Web Solutions <tspan class="cursor">█</tspan></text>
    </g>
  </g>
</svg>'''
    
    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filename}")

# ----------------------------------------------------
# 2. SKILL RADAR SVG
# ----------------------------------------------------

def generate_skill_radar_svg(filename, is_dark=True):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    border_color = "#30363d" if is_dark else "#e1e4e8"
    text_color = "#f0f6fc" if is_dark else "#1f2328"
    sub_color = "#8b949e" if is_dark else "#57606a"
    accent_start = "#38bdf8" if is_dark else "#0284c7"
    accent_end = "#818cf8" if is_dark else "#4f46e5"
    grid_line = "#30363d" if is_dark else "#e1e4e8"
    fill_poly = "rgba(56, 189, 248, 0.25)" if is_dark else "rgba(2, 132, 199, 0.2)"
    stroke_poly = "#38bdf8" if is_dark else "#0284c7"

    axes = [
        ("Full-Stack Dev", 0.85),
        ("React & Frontend", 0.85),
        ("TypeScript / JS", 0.80),
        ("Python", 0.75),
        ("AI / ML Basics", 0.75),
        ("Data Analytics", 0.70),
        ("SQL & Databases", 0.70),
    ]

    num_axes = len(axes)
    cx, cy = 300, 190
    max_r = 120

    angles = [math.pi / 2 - 2 * math.pi * i / num_axes for i in range(num_axes)]

    # Build background polygon levels (20%, 40%, 60%, 80%, 100%)
    levels_svg = ""
    for level in [0.2, 0.4, 0.6, 0.8, 1.0]:
        pts = []
        r = max_r * level
        for angle in angles:
            x = cx + r * math.cos(angle)
            y = cy - r * math.sin(angle)
            pts.append(f"{x:.1f},{y:.1f}")
        poly_pts = " ".join(pts)
        stroke_dash = 'stroke-dasharray="2,2"' if level < 1.0 else ''
        levels_svg += f'<polygon points="{poly_pts}" fill="none" stroke="{grid_line}" stroke-width="1" {stroke_dash}/>\n'

    # Build axis lines and labels
    axis_svg = ""
    labels_svg = ""
    for i, (label, val) in enumerate(axes):
        angle = angles[i]
        x_end = cx + max_r * math.cos(angle)
        y_end = cy - max_r * math.sin(angle)
        axis_svg += f'<line x1="{cx}" y1="{cy}" x2="{x_end:.1f}" y2="{y_end:.1f}" stroke="{grid_line}" stroke-width="1"/>\n'

        # Label position slightly outside max_r
        lr = max_r + 25
        lx = cx + lr * math.cos(angle)
        ly = cy - lr * math.sin(angle)

        anchor = "middle"
        if math.cos(angle) > 0.3:
            anchor = "start"
        elif math.cos(angle) < -0.3:
            anchor = "end"

        labels_svg += f'<text x="{lx:.1f}" y="{ly:.1f}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="12" font-weight="600" fill="{text_color}" text-anchor="{anchor}" dominant-baseline="central">{label}</text>\n'

    # Build data polygon
    data_pts = []
    nodes_svg = ""
    for i, (label, val) in enumerate(axes):
        angle = angles[i]
        r = max_r * val
        x = cx + r * math.cos(angle)
        y = cy - r * math.sin(angle)
        data_pts.append(f"{x:.1f},{y:.1f}")
        nodes_svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{stroke_poly}" stroke="{bg_color}" stroke-width="1.5"/>\n'

    poly_pts_str = " ".join(data_pts)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 370" width="100%" height="370" style="background:{bg_color}; border-radius: 12px;">
  <defs>
    <linearGradient id="radar-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent_start}" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="{accent_end}" stop-opacity="0.1"/>
    </linearGradient>
  </defs>

  <!-- Border Card -->
  <rect width="600" height="370" rx="12" fill="{bg_color}" stroke="url(#radar-border)" stroke-width="1.5"/>

  <!-- Section Title -->
  <text x="300" y="32" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="18" font-weight="700" fill="{text_color}" text-anchor="middle">Developer Capability Radar</text>
  <text x="300" y="50" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="12" fill="{sub_color}" text-anchor="middle">Relative distribution across primary focus areas</text>

  <!-- Grid Levels -->
  {levels_svg}

  <!-- Axis Lines -->
  {axis_svg}

  <!-- Data Polygon -->
  <polygon points="{poly_pts_str}" fill="{fill_poly}" stroke="{stroke_poly}" stroke-width="2.5" stroke-linejoin="round"/>

  <!-- Data Nodes -->
  {nodes_svg}

  <!-- Labels -->
  {labels_svg}
</svg>'''

    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filename}")

# ----------------------------------------------------
# 3. LANGUAGE VISUALIZATION SVG
# ----------------------------------------------------

def generate_language_svg(filename, is_dark=True):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    border_color = "#30363d" if is_dark else "#e1e4e8"
    text_color = "#f0f6fc" if is_dark else "#1f2328"
    sub_color = "#8b949e" if is_dark else "#57606a"
    accent_start = "#38bdf8" if is_dark else "#0284c7"
    accent_end = "#818cf8" if is_dark else "#4f46e5"

    langs = [
        ("TypeScript", 52.0, "#3178c6", "986 KB"),
        ("Python & Data", 24.0, "#3572A5", "456 KB"),
        ("JavaScript", 14.0, "#f1e05a", "266 KB"),
        ("HTML & CSS", 6.0, "#e34c26", "114 KB"),
        ("SQL / PLpgSQL", 4.0, "#e8274b", "76 KB"),
    ]

    # Bar geometry
    bar_x, bar_y, bar_w, bar_h = 40, 75, 520, 16

    segments_svg = ""
    curr_x = bar_x
    for name, pct, color, size in langs:
        w = (pct / 100.0) * bar_w
        segments_svg += f'<rect x="{curr_x:.1f}" y="{bar_y}" width="{w:.1f}" height="{bar_h}" fill="{color}" />\n'
        curr_x += w

    # Legend geometry (2 columns)
    legend_svg = ""
    for i, (name, pct, color, size) in enumerate(langs):
        col = i % 2
        row = i // 2
        lx = 40 + col * 270
        ly = 125 + row * 32

        legend_svg += f'''
    <g transform="translate({lx}, {ly})">
      <circle cx="8" cy="8" r="6" fill="{color}" />
      <text x="22" y="12" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="13" font-weight="600" fill="{text_color}">{name}</text>
      <text x="250" y="12" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="12" font-weight="500" fill="{sub_color}" text-anchor="end">{pct:.1f}% ({size})</text>
    </g>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 230" width="100%" height="230" style="background:{bg_color}; border-radius: 12px;">
  <defs>
    <linearGradient id="lang-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{accent_start}" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="{accent_end}" stop-opacity="0.1"/>
    </linearGradient>
    <clipPath id="bar-clip">
      <rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="8" />
    </clipPath>
  </defs>

  <rect width="600" height="230" rx="12" fill="{bg_color}" stroke="url(#lang-border)" stroke-width="1.5"/>

  <text x="40" y="38" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="18" font-weight="700" fill="{text_color}">Most Used Languages Across Projects</text>
  <text x="40" y="56" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="12" fill="{sub_color}">Calculated from public GitHub repository codebase sizes</text>

  <!-- Segmented Bar -->
  <g clip-path="url(#bar-clip)">
    {segments_svg}
  </g>

  <!-- Legend Items -->
  {legend_svg}
</svg>'''

    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filename}")

# ----------------------------------------------------
# 4. DEFAULT PLACEHOLDER SNAKE SVGs
# ----------------------------------------------------

def generate_snake_placeholder_svg(filename, is_dark=True):
    bg_color = "#0d1117" if is_dark else "#ffffff"
    text_color = "#8b949e" if is_dark else "#57606a"
    accent = "#38bdf8" if is_dark else "#0284c7"
    border = "#30363d" if is_dark else "#e1e4e8"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 140" width="100%" height="140" style="background:{bg_color}; border-radius: 12px;">
  <rect width="800" height="140" rx="12" fill="{bg_color}" stroke="{border}" stroke-width="1"/>
  <g transform="translate(400, 70)" text-anchor="middle">
    <text y="-10" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="16" font-weight="600" fill="{accent}">🐍 GitHub Contribution Snake Activity</text>
    <text y="15" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto" font-size="13" fill="{text_color}">Automated snake animation syncs daily via GitHub Actions</text>
  </g>
</svg>'''

    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {filename}")

if __name__ == "__main__":
    generate_hero_svg("hero-dark.svg", is_dark=True)
    generate_hero_svg("hero-light.svg", is_dark=False)
    generate_skill_radar_svg("skill-radar-dark.svg", is_dark=True)
    generate_skill_radar_svg("skill-radar-light.svg", is_dark=False)
    generate_language_svg("languages-dark.svg", is_dark=True)
    generate_language_svg("languages-light.svg", is_dark=False)
    generate_snake_placeholder_svg("snake-dark.svg", is_dark=True)
    generate_snake_placeholder_svg("snake-light.svg", is_dark=False)
    print("All SVG assets successfully generated!")
