#!/usr/bin/env python3
"""Generate 10 landscape SVG slide images for a NISA + variable insurance deck."""
from __future__ import annotations

import html
from pathlib import Path
import textwrap

W, H = 1600, 900
OUT = Path(__file__).resolve().parent

COLORS = {
    "navy": "#12355B",
    "blue": "#2563EB",
    "sky": "#EAF4FF",
    "teal": "#0F766E",
    "green": "#22C55E",
    "orange": "#F59E0B",
    "red": "#EF4444",
    "purple": "#7C3AED",
    "slate": "#334155",
    "muted": "#64748B",
    "line": "#CBD5E1",
    "white": "#FFFFFF",
    "cream": "#FFF7ED",
}

SLIDES = [
    {
        "title": "NISAを最大限活かし、変額保険で“守り”を足す",
        "subtitle": "長期・資産分散・時間分散を土台に、出口と万が一まで設計する10枚資料",
        "type": "cover",
        "badges": ["NISAは資産形成の中心", "変額保険は出口・保障の補完", "併用で家計の安心度を上げる"],
        "note": "※本資料は一般的な情報提供です。税務・投資・保険判断は制度、商品、個別状況により異なります。",
    },
    {
        "title": "長期投資：時間を味方にする",
        "type": "longterm",
        "lead": "短期の値動きに一喜一憂するより、長く続けて複利の力を受け取る設計へ。",
        "points": [
            "運用益を再投資すると、利益が次の利益を生む“複利”が働く",
            "教育・老後・住宅など、目的別に必要時期を決めておく",
            "長く持つほど、途中の下落を乗り越える余地が広がる",
        ],
        "callout": "営業トーク：『増やす方法』だけでなく『いつ使うか』まで一緒に決めましょう。",
    },
    {
        "title": "資産分散：たまごを1つのかごに盛らない",
        "type": "eggs",
        "lead": "株式だけ、国内だけ、円だけに偏ると、1つの出来事で資産全体が大きく揺れます。",
        "baskets": ["国内株式", "海外株式", "債券", "現金・預金", "保険"],
        "points": [
            "値動きの違う資産に分けることで、家計全体のブレを抑えやすい",
            "NISAは成長資産を効率よく持つ器として優秀",
            "変額保険は保障付きの“別のかご”として役割を分けられる",
        ],
    },
    {
        "title": "時間分散：りんごを毎月少しずつ買う",
        "type": "apples",
        "lead": "りんごの値段が高い月も安い月も、同じ金額で買い続けると購入価格を平準化しやすくなります。",
        "months": [("1月", 200, 5), ("2月", 100, 10), ("3月", 250, 4), ("4月", 125, 8), ("5月", 160, 6)],
        "points": [
            "高い時は少なく、安い時は多く買う仕組みになる",
            "“始めるタイミング”の悩みを小さくできる",
            "NISAのつみたて投資枠と相性がよい考え方",
        ],
    },
    {
        "title": "NISAはまず肯定：非課税で資産形成の主役に",
        "type": "nisa",
        "lead": "NISAは運用益が非課税。2024年以降の制度では年間投資枠が拡大し、非課税保有期間も無期限化されています。",
        "stats": [("年間投資枠", "最大360万円"), ("生涯投資枠", "1,800万円"), ("保有期間", "無期限")],
        "points": [
            "つみたて投資枠：長期・積立・分散に適した投資信託が中心",
            "成長投資枠：上場株式・投資信託等を幅広く活用可能",
            "まずはNISAで非課税メリットを取りに行くのが基本方針",
        ],
        "source": "出典：金融庁 NISA特設サイト（2026年5月確認）",
    },
    {
        "title": "比較：NISAと変額保険は“競合”ではなく“役割分担”",
        "type": "compare",
        "rows": [
            ("主目的", "非課税で増やす", "増やす＋死亡保障・払込免除を組み込む"),
            ("税制", "運用益非課税", "生命保険料控除や保険金課税等は契約形態で異なる"),
            ("流動性", "原則いつでも売却可", "早期解約は元本割れリスク・費用に注意"),
            ("暴落時の出口", "売却時期が重なると評価損が確定し得る", "商品により特別勘定のスイッチングでリスク調整可"),
            ("万が一", "運用は本人の入金継続が前提", "死亡保障・払込免除で計画継続を補完"),
        ],
    },
    {
        "title": "出口戦略：子ども18歳の時に暴落したら？",
        "type": "exit",
        "lead": "教育資金など“使う時期が決まっているお金”は、出口直前の市場下落が最大のストレスになります。",
        "points": [
            "NISAは優秀でも、売却タイミングの価格変動リスクは残る",
            "暴落後の回復には数年かかることがあり、5〜7年待つ想定が必要な局面もある",
            "変額保険を併用し、事前にスイッチングでリスクを下げる選択肢を持つ",
        ],
        "callout": "営業トーク：『増やす入口』はNISA、『使う出口』は保険も含めて二重化しましょう。",
    },
    {
        "title": "スイッチングによる暴落対策：使う数年前から守りへ",
        "type": "switch",
        "steps": [
            ("10年以上前", "株式中心で成長を狙う"),
            ("5〜7年前", "目標額と相場を確認"),
            ("3年前", "債券・安定資産へ段階的に移す"),
            ("使用時期", "必要額を取り崩す"),
        ],
        "points": [
            "スイッチングは“暴落後に慌てる”のではなく“暴落前に備える”考え方",
            "保険商品ごとに対象ファンド、回数、費用、制限は異なるため事前確認が必須",
            "NISAの非課税成長と、変額保険の出口調整を組み合わせる",
        ],
    },
    {
        "title": "万が一への備え：運用にも“団信的発想”を",
        "type": "protection",
        "lead": "住宅ローンに団信があるのは、返済途中で万が一があると家族が困るから。資産形成も同じ視点で考えられます。",
        "points": [
            "通常の投資信託・NISAには、入金者が働けなくなった時の自動補完はない",
            "変額保険の払込免除は、所定状態のとき保険料負担を止めても契約継続を狙える機能",
            "“教育資金・老後資金を積み立て続ける責任”に保障を付ける発想",
        ],
        "callout": "質問例：『住宅ローンには団信を付けるのに、お子さまの教育資金づくりには何を付けますか？』",
    },
    {
        "title": "提案結論：NISAだけでなく、変額保険も持つ理由",
        "type": "closing",
        "columns": [
            ("NISA", ["非課税で効率よく増やす", "低コスト商品を選びやすい", "流動性が高い"]),
            ("変額保険", ["死亡保障・払込免除を備える", "出口前のスイッチングを設計", "目的資金を守る別口座化"]),
            ("併用", ["入口・運用・出口を分けて設計", "市場下落と万が一を同時に対策", "家族に説明しやすい資産形成"]),
        ],
        "closing": "NISAは“増やす主役”。変額保険は“守りと出口の補完”。両方を持つことで、資産形成はより実行しやすくなります。",
        "note": "注意：変額保険は市場リスク、費用、解約控除等により損失が生じる場合があります。NISAも元本保証ではありません。",
    },
]


def esc(s: object) -> str:
    return html.escape(str(s), quote=True)


def wrap(text: str, width: int) -> list[str]:
    return textwrap.wrap(text, width=width, break_long_words=False, replace_whitespace=False)


class SVG:
    def __init__(self, title: str):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            '<defs>',
            '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F8FBFF"/><stop offset="1" stop-color="#E0F2FE"/></linearGradient>',
            '<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.16"/></filter>',
            '</defs>',
            '<style>text{font-family:&quot;Noto Sans CJK JP&quot;,&quot;Noto Sans JP&quot;,&quot;Hiragino Sans&quot;,&quot;Yu Gothic&quot;,sans-serif}.small{font-size:28px}.body{font-size:34px}.lead{font-size:42px;font-weight:700}.title{font-size:64px;font-weight:800}.caption{font-size:23px}.mini{font-size:20px}</style>',
            '<rect width="1600" height="900" fill="url(#bg)"/>',
            '<circle cx="1430" cy="110" r="170" fill="#DBEAFE" opacity="0.65"/>',
            '<circle cx="160" cy="790" r="220" fill="#CCFBF1" opacity="0.55"/>',
        ]
        self.title = title

    def add(self, s: str):
        self.parts.append(s)

    def text(self, x, y, text, size=34, color="#0F172A", weight=500, anchor="start", cls=""):
        self.add(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" class="{cls}">{esc(text)}</text>')

    def multiline(self, x, y, text, width=32, size=34, color="#0F172A", weight=500, line=1.35, anchor="start"):
        for i, t in enumerate(wrap(text, width)):
            self.text(x, y + i * int(size * line), t, size, color, weight, anchor)
        return y + len(wrap(text, width)) * int(size * line)

    def card(self, x, y, w, h, fill="#FFFFFF", stroke="#D8E3F0", radius=28):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2" filter="url(#shadow)"/>')

    def header(self, idx):
        self.text(80, 88, self.title, 48, COLORS["navy"], 800)
        self.add(f'<rect x="80" y="115" width="560" height="8" rx="4" fill="{COLORS["blue"]}"/>')
        self.text(1480, 72, f"{idx:02d}/10", 28, COLORS["muted"], 700, "end")

    def footer(self):
        self.add(f'<text x="80" y="852" fill="{COLORS["muted"]}" font-size="22">NISA × 変額保険 併用提案資料｜一般情報・個別商品説明ではありません</text>')

    def save(self, path: Path):
        self.parts.append('</svg>')
        path.write_text('\n'.join(self.parts), encoding='utf-8')


def draw_bullets(svg, x, y, points, width=42, color=COLORS["slate"], bullet=COLORS["blue"]):
    cy = y
    for p in points:
        svg.add(f'<circle cx="{x}" cy="{cy-10}" r="9" fill="{bullet}"/>')
        cy = svg.multiline(x + 28, cy, p, width=width, size=32, color=color, weight=600, line=1.35) + 18
    return cy


def slide_cover(data, idx):
    svg = SVG(data["title"])
    svg.add(f'<rect x="0" y="0" width="1600" height="900" fill="{COLORS["navy"]}"/>')
    svg.add('<circle cx="1260" cy="160" r="280" fill="#1D4ED8" opacity="0.35"/>')
    svg.add('<circle cx="300" cy="760" r="320" fill="#0F766E" opacity="0.32"/>')
    svg.text(110, 220, "NISA × 変額保険", 52, "#BFDBFE", 800)
    svg.multiline(110, 330, data["title"], width=24, size=72, color="#FFFFFF", weight=900, line=1.22)
    svg.multiline(115, 540, data["subtitle"], width=34, size=36, color="#E0F2FE", weight=700)
    x = 115
    for b in data["badges"]:
        svg.add(f'<rect x="{x}" y="685" width="390" height="74" rx="37" fill="#FFFFFF" opacity="0.95"/>')
        svg.text(x + 195, 733, b, 28, COLORS["navy"], 800, "middle")
        x += 430
    svg.multiline(112, 830, data["note"], width=76, size=22, color="#CBD5E1", weight=500)
    svg.save(OUT / f"slide_{idx:02d}_cover.svg")


def slide_longterm(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    svg.card(80, 170, 700, 560); svg.card(830, 170, 690, 560, fill="#F0FDF4")
    svg.multiline(120, 235, data["lead"], width=23, size=42, color=COLORS["navy"], weight=800)
    draw_bullets(svg, 130, 405, data["points"], width=28)
    # growth curve bars
    vals = [80, 120, 190, 310, 500]
    labels = ["5年", "10年", "15年", "20年", "30年"]
    for i, (v, lab) in enumerate(zip(vals, labels)):
        x = 900 + i*110; y = 650-v
        svg.add(f'<rect x="{x}" y="{y}" width="70" height="{v}" rx="14" fill="{COLORS["green"]}"/>')
        svg.text(x+35, 690, lab, 25, COLORS["slate"], 700, "middle")
    svg.add(f'<path d="M910 560 C1050 500 1160 385 1450 185" fill="none" stroke="{COLORS["blue"]}" stroke-width="10" stroke-linecap="round"/>')
    svg.text(1170, 260, "時間 × 複利", 52, COLORS["blue"], 900, "middle")
    svg.multiline(885, 760, data["callout"], width=30, size=28, color=COLORS["teal"], weight=800)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_long_term.svg")


def slide_eggs(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    svg.multiline(100, 165, data["lead"], width=50, size=34, color=COLORS["slate"], weight=700)
    colors = [COLORS["blue"], COLORS["green"], COLORS["orange"], COLORS["purple"], COLORS["teal"]]
    for i, b in enumerate(data["baskets"]):
        x = 130 + i*285
        svg.add(f'<path d="M{x} 585 Q{x+85} 710 {x+170} 585 L{x+145} 760 L{x+25} 760 Z" fill="{colors[i]}" opacity="0.90"/>')
        for e in range(3):
            svg.add(f'<ellipse cx="{x+50+e*40}" cy="{535-e*18}" rx="28" ry="36" fill="#FFF7ED" stroke="#FDBA74" stroke-width="4"/>')
        svg.text(x+85, 815, b, 30, COLORS["navy"], 800, "middle")
    draw_bullets(svg, 135, 290, data["points"], width=58)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_asset_diversification.svg")


def slide_apples(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    svg.multiline(100, 160, data["lead"], width=52, size=34, color=COLORS["slate"], weight=700)
    svg.card(90, 285, 930, 430)
    for i, (m, price, apples) in enumerate(data["months"]):
        x = 140 + i*170
        svg.text(x+55, 340, m, 28, COLORS["navy"], 800, "middle")
        svg.text(x+55, 385, f"{price}円", 26, COLORS["muted"], 700, "middle")
        for a in range(apples):
            ax = x + 12 + (a % 5) * 22; ay = 435 + (a // 5) * 45
            svg.add(f'<circle cx="{ax}" cy="{ay}" r="15" fill="{COLORS["red"]}"/><path d="M{ax} {ay-15} q10 -15 20 0" fill="none" stroke="{COLORS["green"]}" stroke-width="4"/>')
        svg.add(f'<rect x="{x}" y="620" width="110" height="45" rx="22" fill="#DBEAFE"/>')
        svg.text(x+55, 652, f"{apples}個", 25, COLORS["blue"], 900, "middle")
    svg.card(1070, 285, 430, 430, fill="#FFF7ED")
    svg.text(1285, 360, "毎月1,000円", 42, COLORS["orange"], 900, "middle")
    svg.text(1285, 430, "高い月は少なく", 34, COLORS["slate"], 800, "middle")
    svg.text(1285, 490, "安い月は多く", 34, COLORS["slate"], 800, "middle")
    svg.text(1285, 580, "購入単価を平準化", 38, COLORS["navy"], 900, "middle")
    draw_bullets(svg, 120, 765, data["points"], width=70)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_time_diversification.svg")


def slide_nisa(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    svg.multiline(100, 160, data["lead"], width=54, size=34, color=COLORS["slate"], weight=700)
    for i, (k, v) in enumerate(data["stats"]):
        x = 105 + i*490
        svg.card(x, 285, 430, 180, fill="#EFF6FF")
        svg.text(x+215, 350, k, 30, COLORS["muted"], 800, "middle")
        svg.text(x+215, 425, v, 52, COLORS["blue"], 900, "middle")
    draw_bullets(svg, 140, 555, data["points"], width=68)
    svg.text(100, 805, data["source"], 23, COLORS["muted"], 600)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_nisa_strengths.svg")


def slide_compare(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    x0, y0 = 85, 165; widths = [260, 560, 620]; row_h = 105
    headers = ["項目", "NISA", "変額保険"]
    x = x0
    for w, h in zip(widths, headers):
        svg.add(f'<rect x="{x}" y="{y0}" width="{w}" height="75" fill="{COLORS["navy"]}" rx="18"/>')
        svg.text(x+w/2, y0+49, h, 30, "#FFFFFF", 900, "middle")
        x += w + 10
    y = y0 + 90
    for r, row in enumerate(data["rows"]):
        x = x0
        fill = "#FFFFFF" if r % 2 == 0 else "#F8FAFC"
        for c, (w, txt) in enumerate(zip(widths, row)):
            svg.add(f'<rect x="{x}" y="{y}" width="{w}" height="{row_h}" fill="{fill}" stroke="{COLORS["line"]}" rx="16"/>')
            size = 28 if c else 30
            svg.multiline(x+24, y+42, txt, width=25 if c else 10, size=size, color=COLORS["slate"] if c else COLORS["navy"], weight=800 if c == 0 else 650, line=1.2)
            x += w + 10
        y += row_h + 10
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_comparison.svg")


def slide_exit(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    svg.multiline(100, 158, data["lead"], width=52, size=34, color=COLORS["slate"], weight=700)
    # chart panel
    svg.card(95, 285, 760, 390)
    svg.add(f'<polyline points="145,575 255,520 365,455 475,360 585,300 695,250 805,220" fill="none" stroke="{COLORS["green"]}" stroke-width="10" stroke-linecap="round"/>')
    svg.add(f'<polyline points="145,575 255,520 365,455 475,360 585,520 695,610 805,500" fill="none" stroke="{COLORS["red"]}" stroke-width="10" stroke-linecap="round"/>')
    svg.add(f'<line x1="585" y1="285" x2="585" y2="625" stroke="{COLORS["red"]}" stroke-width="4" stroke-dasharray="12 12"/>')
    svg.text(585, 265, "18歳・教育資金", 28, COLORS["red"], 900, "middle")
    svg.text(475, 720, "必要時期が相場下落と重なるリスク", 32, COLORS["navy"], 900, "middle")
    svg.card(900, 285, 580, 390, fill="#FEF2F2")
    draw_bullets(svg, 940, 360, data["points"], width=26, bullet=COLORS["red"])
    svg.multiline(120, 770, data["callout"], width=60, size=30, color=COLORS["teal"], weight=900)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_exit_strategy.svg")


def slide_switch(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    y = 250
    for i, (period, action) in enumerate(data["steps"]):
        x = 110 + i*365
        svg.card(x, y, 285, 210, fill="#EFF6FF" if i < 2 else "#F0FDF4")
        svg.text(x+142, y+70, period, 32, COLORS["blue"] if i < 2 else COLORS["teal"], 900, "middle")
        svg.multiline(x+35, y+130, action, width=10, size=30, color=COLORS["navy"], weight=800, anchor="start")
        if i < 3:
            svg.text(x+320, y+125, "→", 58, COLORS["muted"], 900, "middle")
    svg.add(f'<rect x="120" y="540" width="1320" height="22" rx="11" fill="{COLORS["line"]}"/>')
    svg.add(f'<rect x="120" y="540" width="700" height="22" rx="11" fill="{COLORS["blue"]}"/>')
    svg.add(f'<rect x="820" y="540" width="620" height="22" rx="11" fill="{COLORS["teal"]}"/>')
    svg.text(470, 600, "成長を狙う期間", 30, COLORS["blue"], 900, "middle")
    svg.text(1130, 600, "守りへ移す期間", 30, COLORS["teal"], 900, "middle")
    draw_bullets(svg, 135, 695, data["points"], width=70, bullet=COLORS["teal"])
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_switching.svg")


def slide_protection(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    svg.multiline(100, 155, data["lead"], width=52, size=34, color=COLORS["slate"], weight=700)
    svg.card(105, 290, 610, 320, fill="#EFF6FF")
    svg.text(410, 360, "住宅ローン", 38, COLORS["navy"], 900, "middle")
    svg.text(410, 435, "団信で家族を守る", 42, COLORS["blue"], 900, "middle")
    svg.add(f'<path d="M220 540 L410 390 L600 540 Z" fill="none" stroke="{COLORS["blue"]}" stroke-width="12" stroke-linejoin="round"/>')
    svg.card(880, 290, 610, 320, fill="#F0FDF4")
    svg.text(1185, 360, "資産形成", 38, COLORS["navy"], 900, "middle")
    svg.text(1185, 435, "払込免除で計画を守る", 38, COLORS["teal"], 900, "middle")
    svg.add(f'<circle cx="1185" cy="540" r="72" fill="none" stroke="{COLORS["teal"]}" stroke-width="12"/><path d="M1148 540 l28 30 l55 -70" fill="none" stroke="{COLORS["teal"]}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>')
    draw_bullets(svg, 130, 690, data["points"], width=70, bullet=COLORS["purple"])
    svg.multiline(930, 690, data["callout"], width=28, size=28, color=COLORS["purple"], weight=900)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_protection.svg")


def slide_closing(data, idx):
    svg = SVG(data["title"]); svg.header(idx)
    colors = [COLORS["blue"], COLORS["teal"], COLORS["purple"]]
    for i, (head, items) in enumerate(data["columns"]):
        x = 95 + i*500
        svg.card(x, 175, 450, 440, fill="#FFFFFF")
        svg.add(f'<rect x="{x}" y="175" width="450" height="90" rx="28" fill="{colors[i]}"/>')
        svg.text(x+225, 233, head, 38, "#FFFFFF", 900, "middle")
        draw_bullets(svg, x+45, 330, items, width=18, bullet=colors[i])
    svg.card(110, 650, 1380, 115, fill="#FFF7ED")
    svg.multiline(145, 705, data["closing"], width=55, size=32, color=COLORS["navy"], weight=900, line=1.25)
    svg.multiline(110, 815, data["note"], width=80, size=22, color=COLORS["muted"], weight=700)
    svg.footer(); svg.save(OUT / f"slide_{idx:02d}_closing.svg")


DRAW = {
    "cover": slide_cover,
    "longterm": slide_longterm,
    "eggs": slide_eggs,
    "apples": slide_apples,
    "nisa": slide_nisa,
    "compare": slide_compare,
    "exit": slide_exit,
    "switch": slide_switch,
    "protection": slide_protection,
    "closing": slide_closing,
}


def main():
    for i, slide in enumerate(SLIDES, start=1):
        DRAW[slide["type"]](slide, i)
    print(f"Generated {len(SLIDES)} SVG slides in {OUT}")


if __name__ == "__main__":
    main()
