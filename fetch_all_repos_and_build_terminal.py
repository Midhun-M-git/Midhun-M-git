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
    output_svg = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_all_repos_terminal.svg"
    output_legacy = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_projects_terminal.svg"
    
    if not repos:
        repos = [
            {"name": "webapp-security-analyzer", "description": "Custom GUI tool for vulnerability scanning & threat detection", "language": "Python", "html_url": "https://github.com/Midhun-M-git/webapp-security-analyzer"},
            {"name": "asthra", "description": "AI-driven mobile app automating technical documentation generation", "language": "Flutter", "html_url": "https://github.com/Midhun-M-git/asthra"},
            {"name": "breach-checker-app", "description": "Secure credential validation engine querying global breach data", "language": "Python", "html_url": "https://github.com/Midhun-M-git/breach-checker-app"},
            {"name": "Midhun-M-git", "description": "Personal Spider-Man themed GitHub Profile README & Workspace", "language": "Python", "html_url": "https://github.com/Midhun-M-git/Midhun-M-git"}
        ]
        
    total_repos = len(repos)
    print(f"Building terminal for {total_repos} repositories with integer keyframe percentages...")
    
    # 4 seconds per repo
    duration = max(30, total_repos * 4)
    pct_per_repo = 100.0 / total_repos
    
    css_keyframes = []
    repo_groups = []
    
    for i, repo in enumerate(repos):
        r_name = html.escape(str(repo.get("name", "repository")))
        raw_desc = str(repo.get("description") or "Open source software project repository")
        if len(raw_desc) > 75:
            raw_desc = raw_desc[:72] + "..."
        r_desc = html.escape(raw_desc)
        r_lang = html.escape(str(repo.get("language") or "Code"))
        r_url = html.escape(str(repo.get("html_url") or f"https://github.com/Midhun-M-git/{r_name}"))
        
        cls_name = f"proj-{i}"
        
        # Calculate clean INTEGER keyframe percentages (GitHub Camo safe!)
        start_p = int(round(i * pct_per_repo))
        active_p = int(round(start_p + (pct_per_repo * 0.88)))
        end_p = int(round((i + 1) * pct_per_repo))
        
        # Ensure bounds
        start_p = max(0, min(100, start_p))
        active_p = max(0, min(100, active_p))
        end_p = max(0, min(100, end_p))
        
        if i == 0:
            kf = f"""
            .{cls_name} {{ animation: kf_{i} {duration}s infinite; -webkit-animation: kf_{i} {duration}s infinite; }}
            @keyframes kf_{i} {{ 0%, {active_p}% {{ opacity: 1; }} {end_p}%, 100% {{ opacity: 0; }} }}
            @-webkit-keyframes kf_{i} {{ 0%, {active_p}% {{ opacity: 1; }} {end_p}%, 100% {{ opacity: 0; }} }}"""
        elif i == total_repos - 1:
            kf = f"""
            .{cls_name} {{ animation: kf_{i} {duration}s infinite; -webkit-animation: kf_{i} {duration}s infinite; opacity: 0; }}
            @keyframes kf_{i} {{ 0%, {start_p}% {{ opacity: 0; }} {start_p + 1}%, {active_p}% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
            @-webkit-keyframes kf_{i} {{ 0%, {start_p}% {{ opacity: 0; }} {start_p + 1}%, {active_p}% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}"""
        else:
            kf = f"""
            .{cls_name} {{ animation: kf_{i} {duration}s infinite; -webkit-animation: kf_{i} {duration}s infinite; opacity: 0; }}
            @keyframes kf_{i} {{ 0%, {start_p}% {{ opacity: 0; }} {start_p + 1}%, {active_p}% {{ opacity: 1; }} {end_p}%, 100% {{ opacity: 0; }} }}
            @-webkit-keyframes kf_{i} {{ 0%, {start_p}% {{ opacity: 0; }} {start_p + 1}%, {active_p}% {{ opacity: 1; }} {end_p}%, 100% {{ opacity: 0; }} }}"""
            
        css_keyframes.append(kf)
        
        g_elm = f'''<!-- [{i+1}/{total_repos}] {r_name} -->
<g class="{cls_name}" style="opacity: 0;">
  <text x="25" y="70" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">cat {r_name}.json</tspan></text>
  <a href="{r_url}" target="_blank">
    <text x="25" y="105" class="proj-title">📂 [{i+1}/{total_repos}] {r_name}</text>
  </a>
  <text x="25" y="132" class="term-text proj-desc">├─ Description: {r_desc}</text>
  <text x="25" y="156" class="term-text">└─ Tech: <tspan class="tech-tag">{r_lang}</tspan>  |  Status: <tspan class="status-tag">🌐 Public</tspan></text>
  <text x="25" y="188" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
</g>'''
        repo_groups.append(g_elm)

    full_css = "\n".join(css_keyframes)
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 210" width="100%" height="auto">
<defs>
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
</defs>

<!-- TERMINAL WINDOW CONTAINER -->
<rect width="800" height="210" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>

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

<!-- ALL REPOSITORY GROUPS -->
{''.join(repo_groups)}

</svg>'''

    with open(output_svg, 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    with open(output_legacy, 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    print(f"Successfully generated GitHub Camo safe SVG with ALL {total_repos} repositories!")

if __name__ == '__main__':
    repos = fetch_repos()
    build_svg(repos)
