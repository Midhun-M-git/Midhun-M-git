#!/usr/bin/env python3
import os
import re
import urllib.request
from datetime import datetime, timedelta

def fetch_contributions():
    url = "https://github.com/users/Midhun-M-git/contributions"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            total_match = re.search(r'([\d,]+)\s+contributions?\s+in\s+the\s+last\s+year', html, re.IGNORECASE)
            total_count = total_match.group(1) if total_match else "420+"
            days = re.findall(r'data-date=[\x22\x27](\d{4}-\d{2}-\d{2})[\x22\x27][^>]*data-level=[\x22\x27](\d+)[\x22\x27]', html)
            return total_count, days
    except Exception as e:
        print(f"Error fetching contributions: {e}")
        return "420+", []

def build_clean_graph_svg(total_count, days):
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spidey_contribution.svg")
    
    # Palette matching Spider-Man Red theme
    COLORS = ['#21262d', '#5c1d24', '#93232c', '#e74c3c', '#ff4d4d']
    
    cell_size = 10
    gap = 3
    step = cell_size + gap
    sx = 55
    sy = 75
    
    # Map date to level
    date_to_level = {d[0]: int(d[1]) for d in days}
    
    # Organize grid by 53 weeks x 7 days
    # Find the earliest date or generate last 52-53 weeks of dates
    today = datetime.now()
    # Go back 52 weeks to Sunday of that week
    start_date = today - timedelta(days=364)
    # Align to previous Sunday
    while start_date.weekday() != 6: # 6 is Sunday in Python datetime (0=Mon, 6=Sun)
        start_date -= timedelta(days=1)
        
    grid_rects = []
    month_labels = []
    current_month = None
    
    for col in range(53):
        col_date = start_date + timedelta(weeks=col)
        m_name = col_date.strftime("%b")
        if m_name != current_month and col % 4 == 0:
            current_month = m_name
            mx = sx + col * step
            month_labels.append(f'<text x="{mx}" y="{sy - 10}" fill="#8b949e" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="10">{m_name}</text>')
            
        for row in range(7):
            d = col_date + timedelta(days=row)
            d_str = d.strftime("%Y-%m-%d")
            lvl = date_to_level.get(d_str, 0)
            x = sx + col * step
            y = sy + row * step
            color = COLORS[min(4, max(0, lvl))]
            pulse_cls = ' class="cg-pulse"' if lvl >= 3 else ''
            grid_rects.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" ry="2" fill="{color}"{pulse_cls}/>')
            
    day_labels = [
        f'<text x="{sx - 28}" y="{sy + 1 * step + 8}" fill="#8b949e" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="9">Mon</text>',
        f'<text x="{sx - 28}" y="{sy + 3 * step + 8}" fill="#8b949e" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="9">Wed</text>',
        f'<text x="{sx - 28}" y="{sy + 5 * step + 8}" fill="#8b949e" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="9">Fri</text>'
    ]
    
    # Legend
    lx = sx + 52 * step - 75
    ly = sy + 7 * step + 16
    legend_items = [
        f'<text x="{lx - 26}" y="{ly + 8}" fill="#8b949e" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="9">Less</text>'
    ]
    for i, c in enumerate(COLORS):
        cx = lx + i * 11
        legend_items.append(f'<rect x="{cx}" y="{ly}" width="9" height="9" rx="2" fill="{c}"/>')
    legend_items.append(f'<text x="{lx + 56}" y="{ly + 8}" fill="#8b949e" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', sans-serif" font-size="9">More</text>')

    FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="auto">
<defs>
  <style>
    .cg-pulse {{
      animation: pulse 2.5s ease-in-out infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 0.7; }}
      50% {{ opacity: 1; }}
    }}
  </style>
</defs>

<!-- BACKGROUND CARD -->
<rect width="800" height="200" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1.5"/>

<!-- HEADER TITLE -->
<text x="25" y="32" fill="#f0f6fc" font-family="{FONT}" font-size="15" font-weight="700">🕷️ GitHub Contributions</text>
<text x="25" y="48" fill="#8b949e" font-family="{FONT}" font-size="11">{total_count} contributions in the last year</text>

<!-- SPIDER-MAN RED WEB CORNER ACCENT -->
<g transform="translate(800, 0) scale(-1, 1)">
  <path d="M 0 0 L 45 0 M 0 0 L 35 15 M 0 0 L 18 28" stroke="#e74c3c" stroke-width="1.5" fill="none" opacity="0.7"/>
  <path d="M 12 0 Q 10 7 0 10 M 25 0 Q 20 12 0 20 M 38 0 Q 30 20 0 26" stroke="#e74c3c" stroke-width="1" fill="none" opacity="0.5"/>
</g>

<!-- MONTH LABELS -->
{''.join(month_labels)}

<!-- DAY LABELS -->
{''.join(day_labels)}

<!-- GRID CELLS -->
{''.join(grid_rects)}

<!-- LEGEND -->
{''.join(legend_items)}

</svg>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Successfully generated clean spidey_contribution.svg!")

if __name__ == '__main__':
    total, days = fetch_contributions()
    build_clean_graph_svg(total, days)
