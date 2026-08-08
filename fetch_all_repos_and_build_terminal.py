#!/usr/bin/env python3
import json
import urllib.request
import re
import html

FONT = "-apple-system, BlinkMacSystemFont, 'Fira Code', 'Courier New', monospace"

def fetch_repos():
    url = "https://api.github.com/users/Midhun-M-git/repos?per_page=100&sort=updated"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []

def build_svg(repos):
    output_svg = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_real_terminal.svg"
    output_scroll = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_scroll_terminal.svg"
    output_v2 = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_terminal_typewriter_v2.svg"
    
    if not repos:
        repos = [
            {"name": "webapp-security-analyzer", "description": "Custom GUI tool for vulnerability scanning & threat detection", "language": "Python", "html_url": "https://github.com/Midhun-M-git/webapp-security-analyzer"},
            {"name": "asthra", "description": "AI-driven mobile app automating technical documentation generation", "language": "Flutter", "html_url": "https://github.com/Midhun-M-git/asthra"},
            {"name": "breach-checker-app", "description": "Secure credential validation engine querying global breach data", "language": "Python", "html_url": "https://github.com/Midhun-M-git/breach-checker-app"},
            {"name": "Midhun-M-git", "description": "Personal Spider-Man themed GitHub Profile README & Workspace", "language": "Python", "html_url": "https://github.com/Midhun-M-git/Midhun-M-git"}
        ]
        
    total_repos = len(repos)
    print(f"Building authentic multi-line terminal session for {total_repos} repositories...")
    
    # Calculate SVG height based on number of repositories
    # Top header = 100px, Each repo = 28px line, Bottom prompt = 40px
    svg_height = 100 + (total_repos * 28) + 50
    
    duration = max(30, total_repos * 1.5)
    pct_per_repo = 80.0 / total_repos
    
    css_rules = []
    clip_defs = []
    repo_lines = []
    
    for i, repo in enumerate(repos):
        r_name = html.escape(str(repo.get("name", "repository")))
        raw_desc = str(repo.get("description") or "Open source software project repository")
        if len(raw_desc) > 55:
            raw_desc = raw_desc[:52] + "..."
        r_desc = html.escape(raw_desc)
        r_lang = html.escape(str(repo.get("language") or "Code"))
        r_url = html.escape(str(repo.get("html_url") or f"https://github.com/Midhun-M-git/{r_name}"))
        
        y_pos = 110 + (i * 28)
        cls_clip = f"clip-line-{i}"
        clip_id = f"c_line_{i}"
        
        start_p = int(round(15 + (i * pct_per_repo)))
        done_p = int(round(start_p + (pct_per_repo * 0.8)))
        
        start_p = max(0, min(100, start_p))
        done_p = max(0, min(100, done_p))
        
        # Line typewriter reveal animation
        clip_kf = f"""
        .{cls_clip} {{ animation: l_kf_{i} {duration}s infinite steps(25); -webkit-animation: l_kf_{i} {duration}s infinite steps(25); }}
        @keyframes l_kf_{i} {{ 0%, {start_p}% {{ width: 0px; }} {done_p}%, 100% {{ width: 770px; }} }}
        @-webkit-keyframes l_kf_{i} {{ 0%, {start_p}% {{ width: 0px; }} {done_p}%, 100% {{ width: 770px; }} }}"""

        css_rules.append(clip_kf)
        clip_defs.append(f'<clipPath id="{clip_id}"><rect x="20" y="{y_pos - 18}" width="0" height="26" class="{cls_clip}"/></clipPath>')

        # Format clean terminal line
        num_str = f"{i+1:02d}"
        
        line_elm = f'''<!-- [{num_str}] {r_name} -->
<g clip-path="url(#{clip_id})">
  <text x="25" y="{y_pos}" class="term-text">
    <tspan class="num">[{num_str}]</tspan> 
    <a href="{r_url}" target="_blank" class="proj-title">📂 {r_name}</a> 
    <tspan class="lang">({r_lang})</tspan> - 
    <tspan class="desc">{r_desc}</tspan>
  </text>
</g>'''
        repo_lines.append(line_elm)

    # Header animation (cmd typed at start)
    header_clip_kf = f"""
    .clip-header {{ animation: h_kf {duration}s infinite steps(30); -webkit-animation: h_kf {duration}s infinite steps(30); }}
    @keyframes h_kf {{ 0% {{ width: 0px; }} 12%, 100% {{ width: 770px; }} }}
    @-webkit-keyframes h_kf {{ 0% {{ width: 0px; }} 12%, 100% {{ width: 770px; }} }}"""
    
    css_rules.append(header_clip_kf)
    clip_defs.append(f'<clipPath id="c_header"><rect x="20" y="40" width="0" height="60" class="clip-header"/></clipPath>')

    full_css = "\n".join(css_rules)
    full_clips = "\n".join(clip_defs)
    
    bottom_y = 110 + (total_repos * 28) + 15
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 {svg_height}" width="100%" height="auto">
<defs>
{full_clips}
  <style>
    .term-text {{
      font-family: 'Fira Code', Consolas, Monaco, monospace, sans-serif;
      font-size: 13px;
      fill: #c9d1d9;
    }}
    .prompt {{
      fill: #e74c3c;
      font-weight: 700;
    }}
    .path {{
      fill: #38bdf8;
    }}
    .cmd {{
      fill: #f0f6fc;
      font-weight: 600;
    }}
    .num {{
      fill: #8b949e;
      font-weight: 600;
    }}
    .proj-title {{
      fill: #58a6ff;
      font-weight: 700;
      text-decoration: none;
    }}
    .proj-title:hover {{
      text-decoration: underline;
    }}
    .lang {{
      fill: #2ea043;
      font-weight: 600;
    }}
    .desc {{
      fill: #8b949e;
    }}
    .cursor {{
      animation: blink 0.8s infinite;
      -webkit-animation: blink 0.8s infinite;
      fill: #e74c3c;
    }}
    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
    @-webkit-keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}

{full_css}
  </style>
</defs>

<!-- TERMINAL WINDOW CONTAINER -->
<rect width="800" height="{svg_height}" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>

<!-- TERMINAL HEADER BAR -->
<path d="M0 10 Q0 0 10 0 L790 0 Q800 0 800 10 L800 32 L0 32 Z" fill="#21262d"/>
<line x1="0" y1="32" x2="800" y2="32" stroke="#30363d" stroke-width="1"/>

<!-- TERMINAL DOTS -->
<circle cx="20" cy="16" r="6" fill="#ff5f56"/>
<circle cx="38" cy="16" r="6" fill="#ffbd2e"/>
<circle cx="56" cy="16" r="6" fill="#27c93f"/>

<!-- TERMINAL TITLE -->
<text x="400" y="21" fill="#8b949e" font-family="{FONT}" font-size="12" text-anchor="middle" font-weight="600">🕷️ spidey@novustech: ~/repositories (zsh)</text>

<!-- SPIDER WEB ACCENT IN TOP RIGHT OF TERMINAL -->
<g transform="translate(800, 0) scale(-1, 1)">
  <path d="M 0 0 L 50 0 M 0 0 L 40 18 M 0 0 L 20 32" stroke="#0099ff" stroke-width="1.5" fill="none" opacity="0.6"/>
</g>

<!-- TERMINAL STARTUP SESSION HEADER -->
<g clip-path="url(#c_header)">
  <text x="25" y="56" class="term-text" fill="#8b949e">Last login: Sat Aug 8 16:14:00 on ttys000</text>
  <text x="25" y="80" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">./fetch_repositories.sh --user=Midhun-M-git --all</tspan></text>
</g>

<!-- ALL REPOSITORY OUTPUT LINES (PRINTING SEQUENTIALLY DOWNWARDS) -->
{''.join(repo_lines)}

<!-- FINAL TERMINAL PROMPT AT BOTTOM WITH BLINKING CURSOR -->
<text x="25" y="{bottom_y}" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>

</svg>'''

    for path in [output_svg, output_scroll, output_v2]:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
    print(f"Successfully generated Authentic Terminal Session SVG for ALL {total_repos} repositories!")

if __name__ == '__main__':
    repos = fetch_repos()
    build_svg(repos)
