# theme.py ── Centralised design tokens & CSS injection with Light/Dark support

def get_theme(mode="dark"):
    is_dark = mode == "dark"
    
    COLORS = {
        "bg":        "#080818" if is_dark else "#f8fafc",
        "bg2":       "#0e0e24" if is_dark else "#f1f5f9",
        "card":      "rgba(14,14,36,0.9)" if is_dark else "rgba(255,255,255,0.95)",
        "teal":      "#00ffe0" if is_dark else "#0d9488",
        "teal_dim":  "rgba(0,255,224,0.15)" if is_dark else "rgba(13,148,136,0.15)",
        "purple":    "#a855f7" if is_dark else "#7e22ce",
        "purple_dim":"rgba(168,85,247,0.15)" if is_dark else "rgba(126,34,206,0.15)",
        "orange":    "#632080" if is_dark else "#0c4fea",
        "orange_dim":"rgba(249,115,22,0.15)" if is_dark else "rgba(234,88,12,0.15)",
        "red":       "#ff4d6d" if is_dark else "#e11d48",
        "red_dim":   "rgba(255,77,109,0.15)" if is_dark else "rgba(225,29,72,0.15)",
        "blue":      "#38bdf8" if is_dark else "#0284c7",
        "green":     "#4ade80" if is_dark else "#16a34a",
        "yellow":    "#fbbf24" if is_dark else "#d97706",
        "grid":      "rgba(255,255,255,0.05)" if is_dark else "rgba(0,0,0,0.06)",
        "border":    "rgba(0,255,224,0.1)" if is_dark else "rgba(0,0,0,0.1)",
        "text":      "#e2e2f0" if is_dark else "#0f172a",
        "text_dim":  "#6e6e9a" if is_dark else "#64748b",
        "text_mid":  "#a0a0c0" if is_dark else "#475569",
    }

    PLOTLY_BASE = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor ="rgba(0,0,0,0)",
        font=dict(family="'IBM Plex Mono', monospace", color=COLORS["text"], size=11),
        xaxis=dict(gridcolor=COLORS["grid"], zeroline=False, showline=False, tickfont=dict(color=COLORS["text_dim"])),
        yaxis=dict(gridcolor=COLORS["grid"], zeroline=False, showline=False, tickfont=dict(color=COLORS["text_dim"])),
        hovermode="x unified",
        hoverlabel=dict(bgcolor=COLORS["bg2"], bordercolor=COLORS["teal"], font=dict(family="'IBM Plex Mono', monospace", color=COLORS["text"], size=11)),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor=COLORS["border"], borderwidth=1, font=dict(size=10), orientation="h", yanchor="bottom", y=1.01, xanchor="left", x=0),
    )

    CSS = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&family=Syne:wght@400;600;700;800&display=swap');

    :root {{
      --teal: {COLORS['teal']}; --purple: {COLORS['purple']}; --orange: {COLORS['orange']};
      --red: {COLORS['red']}; --blue: {COLORS['blue']}; --green: {COLORS['green']};
      --bg: {COLORS['bg']}; --bg2: {COLORS['bg2']}; --text: {COLORS['text']};
      --dim: {COLORS['text_dim']}; --card: {COLORS['card']}; --border: {COLORS['border']};
      --grid: {COLORS['grid']};
    }}

    html, body, [class*="css"] {{ font-family: 'IBM Plex Mono', monospace !important; background: var(--bg) !important; color: var(--text) !important; }}
    .stApp {{ background: radial-gradient(ellipse at 20% 10%, {COLORS['purple_dim']} 0%, transparent 50%), radial-gradient(ellipse at 80% 90%, {COLORS['teal_dim']} 0%, transparent 50%), var(--bg) !important; }}
    .block-container {{ padding: 0 1.5rem 3rem 1.5rem !important; max-width: 100% !important; }}
    #MainMenu, footer, header {{ visibility: hidden !important; }}

    .topbar {{ background: {COLORS['bg2']}; border-bottom: 1px solid var(--border); padding: 0.75rem 2rem; margin: 0 -1.5rem 2rem -1.5rem; display: flex; align-items: center; justify-content: space-between; backdrop-filter: blur(20px); position: sticky; top: 0; z-index: 999; }}
    .logo {{ font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 800; letter-spacing: -1px; color: var(--teal); }}
    .logo em {{ color: var(--purple); font-style: normal; }}
    .topbar-right {{ display:flex; gap:1rem; align-items:center; font-size:0.7rem; color:var(--dim); }}
    .live-dot {{ width:6px; height:6px; border-radius:50%; background:var(--green); box-shadow:0 0 8px var(--green); animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%,100%{{opacity:1}} 50%{{opacity:0.4}} }}

    .sec-title {{ font-family: 'Syne', sans-serif; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--teal); margin: 1.5rem 0 1rem 0; display: flex; align-items: center; gap: 0.6rem; }}
    .sec-title::after {{ content:''; flex:1; height:1px; background: linear-gradient(to right, {COLORS['teal_dim']}, transparent); }}

    .metric-card {{ background: var(--card); border: 1px solid var(--grid); border-radius: 12px; padding: 1.1rem 1.3rem; transition: all 0.25s ease; position: relative; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.02); }}
    .metric-card:hover {{ border-color: var(--border); transform: translateY(-3px); }}
    .m-label {{ font-size:0.65rem; color:var(--dim); letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.4rem; }}
    .m-value {{ font-size:1.6rem; font-weight:600; color:var(--text); line-height:1; }}
    .m-sub {{ font-size:0.68rem; margin-top:0.35rem; }}

    .info-row {{ display:flex; justify-content:space-between; align-items:center; padding: 0.5rem 0; border-bottom: 1px solid var(--grid); font-size: 0.78rem; }}
    .info-row:last-child {{ border-bottom: none; }}
    .info-key {{ color: var(--dim); }} .info-val {{ color: var(--text); font-weight: 500; }}

    .badge {{ display:inline-block; padding:2px 8px; border-radius:5px; font-size:0.65rem; font-weight:600; letter-spacing:0.05em; }}
    .badge-bull {{ background:{COLORS['teal_dim']}; color:var(--teal); border:1px solid var(--border); }}
    .badge-bear {{ background:{COLORS['red_dim']}; color:var(--red);  border:1px solid var(--border); }}
    .badge-neu  {{ background:{COLORS['orange_dim']}; color:var(--yellow);border:1px solid var(--border); }}

    .signal-row {{ display:flex; flex-wrap:wrap; gap:0.5rem; margin:0.5rem 0 1rem 0; }}
    .signal {{ padding:4px 12px; border-radius:20px; font-size:0.68rem; font-family:'Syne',sans-serif; font-weight:600; letter-spacing:0.04em; }}
    .sig-buy   {{ background:{COLORS['green']}; color:white; border:1px solid var(--border); opacity: 0.9; }}
    .sig-sell  {{ background:{COLORS['red']}; color:white;   border:1px solid var(--border); opacity: 0.9; }}
    .sig-hold  {{ background:{COLORS['yellow']}; color:white; border:1px solid var(--border); opacity: 0.9; }}

    .stTabs [data-baseweb="tab-list"] {{ background: var(--card) !important; border: 1px solid var(--grid) !important; border-radius: 12px !important; padding: 5px !important; gap: 4px !important; }}
    .stTabs [data-baseweb="tab"] {{ color: var(--dim) !important; border-radius: 8px !important; font-family: 'Syne', sans-serif !important; font-size: 0.78rem !important; font-weight: 600 !important; padding: 6px 16px !important; }}
    .stTabs [aria-selected="true"] {{ background: linear-gradient(135deg, var(--purple), {COLORS['blue']}) !important; color: white !important; }}

    .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div, .stMultiSelect > div > div {{ background: var(--bg2) !important; border: 1px solid var(--border) !important; border-radius: 8px !important; color: var(--text) !important; font-family: 'IBM Plex Mono', monospace !important; }}
    .stSlider > div > div > div {{ background: var(--purple) !important; }}
    .streamlit-expanderHeader {{ background: var(--card) !important; border: 1px solid var(--grid) !important; border-radius: 8px !important; font-family: 'Syne', sans-serif !important; font-size: 0.8rem !important; font-weight: 600 !important; color:var(--text) !important; }}
    .footer {{ text-align:center; padding:1.5rem; margin-top:2rem; border-top:1px solid var(--grid); font-size:0.65rem; color:var(--dim); }}
    </style>
    """
    return COLORS, PLOTLY_BASE, CSS
