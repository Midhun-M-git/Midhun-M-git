#!/usr/bin/env python3
import json
import urllib.request
import re
import html

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

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
    output_svg = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_scroll_terminal.svg"
    output_v2 = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_terminal_typewriter_v2.svg"
    output_typewriter = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_typewriter_terminal.svg"
    
    if not repos:
        repos = [
            {"name": "webapp-security-analyzer", "description": "Custom GUI tool for vulnerability scanning & threat detection", "language": "Python", "html_url": "https://github.com/Midhun-M-git/webapp-security-analyzer"},
            {"name": "asthra", "description": "AI-driven mobile app automating technical documentation generation", "language": "Flutter", "html_url": "https://github.com/Midhun-M-git/asthra"},
            {"name": "breach-checker-app", "description": "Secure credential validation engine querying global breach data", "language": "Python", "html_url": "https://github.com/Midhun-M-git/breach-checker-app"},
            {"name": "Midhun-M-git", "description": "Personal Spider-Man themed GitHub Profile README & Workspace", "language": "Python", "html_url": "https://github.com/Midhun-M-git/Midhun-M-git"}
        ]
        
    total_repos = len(repos)
    print(f"Building Real Vertical Scroll-Up Terminal for {total_repos} repositories...")
    
    # Each repo occupies 160px vertical height block
    block_height = 160
    viewport_height = 240
    
    duration = max(40, total_repos * 4.5)
    pct_per_repo = 100.0 / total_repos
    
    css_rules = []
    clip_defs = []
    repo_blocks = []
    scroll_keyframes = []
    
    for i, repo in enumerate(repos):
        r_name = html.escape(str(repo.get("name", "repository")))
        raw_desc = str(repo.get("description") or "Open source software project repository")
        if len(raw_desc) > 75:
            raw_desc = raw_desc[:72] + "..."
        r_desc = html.escape(raw_desc)
        r_lang = html.escape(str(repo.get("language") or "Code"))
        r_url = html.escape(str(repo.get("html_url") or f"https://github.com/Midhun-M-git/{r_name}"))
        
        y_offset = i * block_height
        cls_cmd_clip = f"clip-cmd-{i}"
        cls_out_clip = f"clip-out-{i}"
        cmd_clip_id = f"cmd_c_{i}"
        out_clip_id = f"out_c_{i}"
        
        # Calculate keyframe timings for Step 1 (command type) and Step 2 (output print)
        start_p = int(round(i * pct_per_repo))
        cmd_typed_p = int(round(start_p + (pct_per_repo * 0.35)))
        out_typed_p = int(round(start_p + (pct_per_repo * 0.65)))
        end_p = int(round((i + 1) * pct_per_repo))
        
        start_p = max(0, min(100, start_p))
        cmd_typed_p = max(0, min(100, cmd_typed_p))
        out_typed_p = max(0, min(100, out_typed_p))
        end_p = max(0, min(100, end_p))
        
        # Command line typing clip animation
        cmd_kf = f"""
        .{cls_cmd_clip} {{ animation: cmd_kf_{i} {duration}s infinite steps(25); -webkit-animation: cmd_kf_{i} {duration}s infinite steps(25); }}
        @keyframes cmd_kf_{i} {{ 0%, {start_p}% {{ width: 0px; }} {cmd_typed_p}%, 100% {{ width: 770px; }} }}
        @-webkit-keyframes cmd_kf_{i} {{ 0%, {start_p}% {{ width: 0px; }} {cmd_typed_p}%, 100% {{ width: 770px; }} }}"""

        # Output lines typing clip animation
        out_kf = f"""
        .{cls_out_clip} {{ animation: out_kf_{i} {duration}s infinite steps(30); -webkit-animation: out_kf_{i} {duration}s infinite steps(30); }}
        @keyframes out_kf_{i} {{ 0%, {cmd_typed_p}% {{ width: 0px; }} {out_typed_p}%, 100% {{ width: 770px; }} }}
        @-webkit-keyframes out_kf_{i} {{ 0%, {cmd_typed_p}% {{ width: 0px; }} {out_typed_p}%, 100% {{ width: 770px; }} }}"""

        css_rules.append(cmd_kf + "\n" + out_kf)
        
        clip_defs.append(f'<clipPath id="{cmd_clip_id}"><rect x="20" y="{y_offset + 10}" width="0" height="30" class="{cls_cmd_clip}"/></clipPath>')
        clip_defs.append(f'<clipPath id="{out_clip_id}"><rect x="20" y="{y_offset + 40}" width="0" height="110" class="{cls_out_clip}"/></clipPath>')

        # Build repository block inside vertical stream
        block = f'''<!-- [{i+1}/{total_repos}] {r_name} -->
<g transform="translate(0, {y_offset})">
  <!-- Line 1: Command typed -->
  <g clip-path="url(#{cmd_clip_id})">
    <text x="25" y="30" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">cat {r_name}.json</tspan></text>
  </g>
  
  <!-- Line 2,3,4: Output printed -->
  <g clip-path="url(#{out_clip_id})">
    <a href="{r_url}" target="_blank">
      <text x="25" y="62" class="proj-title">📂 [{i+1}/{total_repos}] {r_name}</text>
    </a>
    <text x="25" y="86" class="term-text proj-desc">├─ Description: {r_desc}</text>
    <text x="25" y="108" class="term-text">└─ Tech: <tspan class="tech-tag">{r_lang}</tspan>  |  Status: <tspan class="status-tag">🌐 Public</tspan></text>
  </g>
</g>'''
        repo_blocks.append(block)

        # Build vertical scroll keyframe step
        y_scroll = -i * block_height
        if i == 0:
            scroll_keyframes.append(f"0%, {end_p - 1}% {{ transform: translateY(0px); -webkit-transform: translateY(0px); }}")
        elif i == total_repos - 1:
            scroll_keyframes.append(f"{start_p}%, 100% {{ transform: translateY({y_scroll}px); -webkit-transform: translateY({y_scroll}px); }}")
        else:
            scroll_keyframes.append(f"{start_p}%, {end_p - 1}% {{ transform: translateY({y_scroll}px); -webkit-transform: translateY({y_scroll}px); }}")

    scroll_css = f"""
    .scroll-stream {{
      animation: term_scroll {duration}s infinite cubic-bezier(0.25, 1, 0.5, 1);
      -webkit-animation: term_scroll {duration}s infinite cubic-bezier(0.25, 1, 0.5, 1);
    }}
    @keyframes term_scroll {{
      {chr(10).join(scroll_keyframes)}
    }}
    @-webkit-keyframes term_scroll {{
      {chr(10).join(scroll_keyframes)}
    }}"""

    full_css = "\n".join(css_rules) + "\n" + scroll_css
    full_clips = "\n".join(clip_defs)
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 240" width="100%" height="auto">
<defs>
{full_clips}
  <style>
    .term-text {{
      font-family: Consolas, Monaco, monospace, sans-serif;
      font-size: 14px;
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
    .proj-title {{
      fill: #58a6ff;
      font-weight: 700;
      font-size: 16px;
    }}
    .proj-desc {{
      fill: #8b949e;
      font-size: 13px;
    }}
    .tech-tag {{
      fill: #2ea043;
      font-weight: 600;
    }}
    .status-tag {{
      fill: #38bdf8;
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

  <!-- CLIP VIEWPORT TO PREVENT OVERFLOW -->
  <clipPath id="viewport_clip">
    <rect x="0" y="32" width="800" height="208" />
  </clipPath>
</defs>

<!-- TERMINAL WINDOW CONTAINER -->
<rect width="800" height="240" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>

<!-- TERMINAL HEADER BAR -->
<path d="M0 10 Q0 0 10 0 L790 0 Q800 0 800 10 L800 32 L0 32 Z" fill="#21262d"/>
<line x1="0" y1="32" x2="800" y2="32" stroke="#30363d" stroke-width="1"/>

<!-- TERMINAL DOTS -->
<circle cx="20" cy="16" r="6" fill="#ff5f56"/>
<circle cx="38" cy="16" r="6" fill="#ffbd2e"/>
<circle cx="56" cy="16" r="6" fill="#27c93f"/>

<!-- TERMINAL TITLE -->
<text x="400" y="21" fill="#8b949e" font-family="{FONT}" font-size="12" text-anchor="middle" font-weight="600">🕷️ spidey@novustech: ~/repositories ({total_repos} Repositories)</text>

<!-- SPIDER WEB ACCENT IN TOP RIGHT OF TERMINAL -->
<g transform="translate(800, 0) scale(-1, 1)">
  <path d="M 0 0 L 50 0 M 0 0 L 40 18 M 0 0 L 20 32" stroke="#0099ff" stroke-width="1.5" fill="none" opacity="0.6"/>
</g>

<!-- TERMINAL VIEWPORT CONTAINER -->
<g clip-path="url(#viewport_clip)">
  <!-- VERTICAL SCROLL STREAM -->
  <g class="scroll-stream" transform="translate(0, 32)">
    {''.join(repo_blocks)}
  </g>
</g>

<!-- FIXED BOTTOM PROMPT WITH BLINKING CURSOR (ALWAYS VISIBLE) -->
<g transform="translate(0, 202)">
  <rect x="0" y="-12" width="800" height="50" fill="#161b22" opacity="0.95"/>
  <line x1="0" y1="-12" x2="800" y2="-12" stroke="#21262d" stroke-width="1"/>
  <text x="25" y="10" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
</g>

</svg>'''

    for path in [output_svg, output_v2, output_typewriter]:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
    print(f"Successfully generated Real Vertical Scroll-Up Terminal for ALL {total_repos} repositories!")

if __name__ == '__main__':
    repos = fetch_repos()
    build_svg(repos)
