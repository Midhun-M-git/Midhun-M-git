#!/usr/bin/env python3
import os

FONT = "-apple-system, BlinkMacSystemFont, 'Fira Code', 'Courier New', monospace"

def build_typing_projects_terminal():
    output_svg = r"C:\Users\MIDHUN\.gemini\antigravity-ide\scratch\Midhun-M-git\spidey_projects_terminal.svg"
    
    # 4 cycling project terminal views
    # Each view has: Command typed, Project Name, Description, Tech & Link
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 210" width="100%" height="auto">
<defs>
  <style>
    .term-text {{
      font-family: 'Fira Code', Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
      font-size: 14.5px;
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
      font-size: 13.5px;
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
      fill: #e74c3c;
    }}
    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}

    /* Typewriter animation cycle across 4 project repositories */
    .proj-1 {{ animation: cycle1 20s infinite; }}
    .proj-2 {{ animation: cycle2 20s infinite; }}
    .proj-3 {{ animation: cycle3 20s infinite; }}
    .proj-4 {{ animation: cycle4 20s infinite; }}

    @keyframes cycle1 {{ 0%, 23% {{ opacity: 1; }} 25%, 100% {{ opacity: 0; }} }}
    @keyframes cycle2 {{ 0%, 24% {{ opacity: 0; }} 25%, 48% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
    @keyframes cycle3 {{ 0%, 49% {{ opacity: 0; }} 50%, 73% {{ opacity: 1; }} 75%, 100% {{ opacity: 0; }} }}
    @keyframes cycle4 {{ 0%, 74% {{ opacity: 0; }} 75%, 98% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
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
<text x="400" y="21" fill="#8b949e" font-family="{FONT}" font-size="12" text-anchor="middle" font-weight="600">🕷️ spidey@novustech: ~/repositories (zsh)</text>

<!-- SPIDER WEB ACCENT IN TOP RIGHT OF TERMINAL -->
<g transform="translate(800, 0) scale(-1, 1)">
  <path d="M 0 0 L 50 0 M 0 0 L 40 18 M 0 0 L 20 32" stroke="#0099ff" stroke-width="1.5" fill="none" opacity="0.6"/>
</g>

<!-- PROJECT REPOSITORY CYCLE 1: WebApp Security Analyzer -->
<g class="proj-1">
  <text x="25" y="70" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">cat webapp-security-analyzer.json</tspan></text>
  <a href="https://github.com/Midhun-M-git/webapp-security-analyzer" target="_blank">
    <text x="25" y="105" class="proj-title">🚀 [1/4] WebApp Security Analyzer</text>
  </a>
  <text x="25" y="132" class="term-text proj-desc">├─ Description: Custom GUI tool for vulnerability scanning &amp; threat detection</text>
  <text x="25" y="156" class="term-text">└─ Tech: <tspan class="tech-tag">Python</tspan> • <tspan class="tech-tag">Tkinter</tspan>  |  Status: <tspan class="status-tag">🌐 Public</tspan></text>
  <text x="25" y="188" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
</g>

<!-- PROJECT REPOSITORY CYCLE 2: Asthra -->
<g class="proj-2" style="opacity: 0;">
  <text x="25" y="70" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">cat asthra.json</tspan></text>
  <a href="https://github.com/Midhun-M-git/asthra" target="_blank">
    <text x="25" y="105" class="proj-title">🤖 [2/4] Asthra</text>
  </a>
  <text x="25" y="132" class="term-text proj-desc">├─ Description: AI-driven mobile app automating technical documentation generation</text>
  <text x="25" y="156" class="term-text">└─ Tech: <tspan class="tech-tag">Flutter</tspan> • <tspan class="tech-tag">AI Backend</tspan>  |  Status: <tspan class="status-tag">🌐 Public</tspan></text>
  <text x="25" y="188" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
</g>

<!-- PROJECT REPOSITORY CYCLE 3: Breach Checker Engine -->
<g class="proj-3" style="opacity: 0;">
  <text x="25" y="70" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">cat breach-checker-app.json</tspan></text>
  <a href="https://github.com/Midhun-M-git/breach-checker-app" target="_blank">
    <text x="25" y="105" class="proj-title">🛡️ [3/4] Breach Checker Engine</text>
  </a>
  <text x="25" y="132" class="term-text proj-desc">├─ Description: Secure credential validation engine querying global breach data</text>
  <text x="25" y="156" class="term-text">└─ Tech: <tspan class="tech-tag">Python</tspan> • <tspan class="tech-tag">REST APIs</tspan>  |  Status: <tspan class="status-tag">🌐 Public</tspan></text>
  <text x="25" y="188" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
</g>

<!-- PROJECT REPOSITORY CYCLE 4: Midhun-M-git Profile -->
<g class="proj-4" style="opacity: 0;">
  <text x="25" y="70" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cmd">cat Midhun-M-git.json</tspan></text>
  <a href="https://github.com/Midhun-M-git/Midhun-M-git" target="_blank">
    <text x="25" y="105" class="proj-title">🕷️ [4/4] Midhun-M-git Profile &amp; Portfolio</text>
  </a>
  <text x="25" y="132" class="term-text proj-desc">├─ Description: Personal Spider-Man themed GitHub Profile README &amp; Workspace</text>
  <text x="25" y="156" class="term-text">└─ Tech: <tspan class="tech-tag">Python</tspan> • <tspan class="tech-tag">SVG Animations</tspan> • <tspan class="tech-tag">Markdown</tspan>  |  Status: <tspan class="status-tag">🌐 Public</tspan></text>
  <text x="25" y="188" class="term-text"><tspan class="prompt">spidey@novustech</tspan>:<tspan class="path">~/projects</tspan>$ <tspan class="cursor">█</tspan></text>
</g>

</svg>'''

    with open(output_svg, 'w', encoding='utf-8') as f:
        f.write(svg_content)
        
    print(f"Generated animated typewriter Spidey Projects Terminal: {output_svg}")

if __name__ == '__main__':
    build_typing_projects_terminal()
