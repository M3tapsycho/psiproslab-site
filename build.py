"""Builds the static psiproslab.com pages from the content below. Run: python3 build.py
Source text: Claude Doc "Brain and Sleep – psiproslab draft" (+ approved disclaimer fixes, 4 Nov 2026)."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).parent
PRIVACY = "https://app.psiproslab.com/privacy/"
def _v(f): return hashlib.md5((ROOT / "assets" / f).read_bytes()).hexdigest()[:8]
NAV = [("/", "Home"), ("/building-blocks/", "Building blocks"), ("/exercises/", "Exercises"),
       ("/brain-and-sleep/", "Brain and Sleep"), ("/sources/", "Sources")]
HEALTH_CHECK = ('<p class="note"><strong>Health check:</strong> ask your doctor first if you have a heart '
                'condition, take beta-blockers or have an eating disorder.</p>')


def page(path, title, desc, body):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={_v('site.css')}">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/"><b>Ψ</b>ProsLab</a>
  <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav">{links}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <div class="cols">
    <div>© 2026 MSCPDZ Co., Ltd. · Hua Hin, Thailand<br><a href="mailto:psiproslab@gmail.com">psiproslab@gmail.com</a></div>
    <nav><a href="{PRIVACY}">Privacy policy</a></nav>
  </div>
  <p class="crisis disclaimer">ΨProsLab shares self-help information for learning. It is not therapy, diagnosis or medical advice. <strong>In crisis?</strong> Call your local emergency number or find a helpline at <a href="https://findahelpline.com">findahelpline.com</a>.</p>
</div></footer>
<script src="/assets/site.js?v={_v('site.js')}"></script>
</body>
</html>
"""
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def article(h1, intro, body):
    return f"""<section class="page-head"><div class="wrap narrow"><h1>{h1}</h1><p class="muted">{intro}</p></div></section>
<div class="prose"><div class="wrap narrow">
{body}
</div></div>"""


def ex(text):
    return f"<p><strong>Example:</strong> {text}</p>"


# ---------- Home ----------
HOME = """<section class="hero"><div class="wrap narrow">
  <h1>psiproslab</h1>
  <p class="lead">Simple tools for a calmer, sharper mind. The science, explained simply.</p>
</div></section>
<section><div class="wrap narrow">
  <h2>How to use this site</h2>
  <ol class="rows">
    <li><a href="/building-blocks/"><b>Building blocks</b><span>Short pieces on how your brain works.</span></a></li>
    <li><a href="/exercises/"><b>Exercises</b><span>The blocks put to work on real problems.</span></a></li>
    <li><a href="/brain-and-sleep/"><b>Brain and Sleep</b><span>What really helps, graded A, B or C.</span></a></li>
  </ol>
  <p class="small muted">Every claim has a grade and a <a href="/sources/">source</a> you can check.</p>
</div></section>"""

# ---------- Building blocks (one page each) ----------
TIPP_LINK = '<a href="/building-blocks/tipp/">TIPP</a>'

BLOCKS = [
    dict(slug="abc-model", name="The ABC model", short="ABC model",
         teaser="Why the same event makes one person angry and another grateful.",
         body="""<p>It's not the situation that decides how you feel, but what you think about it. This model comes from Albert Ellis (REBT) and is a core idea of cognitive behavioural therapy.</p>
<ul>
<li><strong>A, Activating event:</strong> what happens.</li>
<li><strong>B, Belief:</strong> what you think about it.</li>
<li><strong>C, Consequence:</strong> what you feel and do.</li>
</ul>
<p><strong>Example: the traffic light.</strong> You're waiting at a red light, you get distracted, and the light turns green. The driver behind you honks.</p>
<div class="table-scroll"><table>
<tr><th></th><th>Driver 1</th><th>Driver 2</th></tr>
<tr><td><strong>A: Event</strong></td><td>Someone honks</td><td>Someone honks</td></tr>
<tr><td><strong>B: Thought</strong></td><td>"How impatient, it's only a few seconds!"</td><td>"Good, they noticed I was distracted."</td></tr>
<tr><td><strong>C: Feeling and action</strong></td><td>Anger, annoyed at the other driver</td><td>Gratitude, a friendly wave</td></tr>
</table></div>
<p>Same situation, different thought, different outcome.</p>
<p><strong>Try it yourself:</strong></p>
<ol>
<li>Think of a recent moment when you felt a strong emotion. That's your <strong>C</strong>.</li>
<li>Write down what happened, just the facts. That's your <strong>A</strong>.</li>
<li>Ask yourself: "What did I think at that moment?" That's your <strong>B</strong>.</li>
<li>Look for another possible thought about the same event. How would you feel then?</li>
</ol>"""),
    dict(slug="three-brains", name="The three brains", short="Three brains",
         teaser="Instinct, emotion and thinking: who's in charge under stress.",
         body="""<p>Think of your brain as three helpers. The instinct brain keeps you alive, the emotion brain makes you feel, and the thinking brain plans and decides. This is a simple picture, not exact anatomy: the old "triune brain" model by MacLean is outdated, but the idea that stress hands control to faster systems is well supported (Arnsten, 2009 review).</p>"""),
    dict(slug="instinct-is-faster", name="Instinct is faster", short="Instinct",
         teaser="Why you jump before you know why.",
         body="""<p>Your survival reflex acts before you feel or think. Nothing is switched off; it simply wins the race.</p>
""" + ex('You see a garden hose in the grass and jump back. A moment later you feel fear. Only then does your thinking brain say, "It\'s just a hose." (LeDoux\'s research on the brain\'s fast survival circuit.)')),
    dict(slug="emotion-takes-over", name="Emotion takes over", short="Emotion",
         teaser="Why you say things you regret in a fight.",
         body="""<p>When an emotion is very strong, it turns down your thinking brain. You act first and think later.</p>
""" + ex('In a heated fight with your partner, you say hurtful things you don\'t mean. When you calm down, your thinking brain comes back and you think, "Why did I say that?" Regret follows.')),
    dict(slug="white-bear-effect", name="The white bear effect", short="White bear",
         teaser="Why \"don't think of it\" backfires.",
         body="""<p>Trying not to think about something keeps it in your head. Your brain can't do "don't"; it only hears the thing itself. Fighting the thought also costs energy. (Wegner's research, confirmed by a meta-analysis.)</p>
""" + ex('Try not to think of a white bear for one minute. It keeps popping up.')),
    dict(slug="emotional-bucket", name="The emotional bucket", short="Bucket",
         teaser="Why small things overflow on a bad day.",
         body="""<p>Stress and strong feelings fill a bucket inside you over the day. When it's full, even small things make it overflow.</p>
""" + ex('After a stressful day, a spilled glass of milk makes you snap at your kids. On a calm morning, you\'d just wipe it up.')),
    dict(slug="clogged-engine", name="The clogged engine", short="Clogged engine",
         teaser="Why effort feels harder as the day goes on.",
         body="""<p>Hard thinking is like a car engine working hard: dirt builds up in the filter. The more it clogs, the harder every effort feels, so you pick the easy option. A full emotional bucket is like driving uphill with a heavy load: the filter clogs faster. Rest and sleep clean it. (A 2022 brain study by Wiehler and colleagues; more studies are needed.)</p>
""" + ex('After a long workday you planned to cook, but you order takeaway instead.')),
    dict(slug="relief-reward", name="The relief reward", short="Relief reward",
         teaser="Why avoiding feels good and keeps you stuck.",
         body="""<p>Avoiding something unpleasant feels good right away. That relief works like a reward, so your brain learns to avoid it again. (Research by Sirois and Pychyl; a meta-analysis by Steel.)</p>
""" + ex('You open your tax forms, feel a knot in your stomach, and grab your phone instead. The knot goes away, so next time you grab the phone sooner.')),
    dict(slug="tipp", name="TIPP: empty the bucket fast", short="TIPP",
         teaser="Four fast ways to calm your body.",
         body=f"""<p>Four quick ways to calm your body when emotions run high. (A skill from Dialectical Behaviour Therapy.)</p>
<ol>
<li><strong>Temperature:</strong> Cold water on your face for 30 seconds.</li>
<li><strong>Intense exercise:</strong> A few minutes of hard movement.</li>
<li><strong>Paced breathing:</strong> Breathe out longer than in, for example in for 4, out for 6.</li>
<li><strong>Paired muscle relaxation:</strong> Tense a muscle while breathing in, let go while breathing out.</li>
</ol>
{HEALTH_CHECK}
""" + ex('Panic rises before a meeting. You splash cold water on your face, and your heart slows down.')),
]

# ---------- Exercises (one page each) ----------
EXERCISES = [
    dict(slug="quitting-smoking", name="Quitting smoking", short="Quit smoking",
         teaser="Stop fighting the urge; empty the bucket instead.",
         uses=["white-bear-effect", "emotional-bucket", "clogged-engine", "tipp"],
         body=f"""<p>Telling yourself "don't smoke" all day keeps the urge alive. On a stressful day the bucket overflows, the engine clogs, and you light up. So stop fighting the thought, and empty the bucket with {TIPP_LINK} before the urge wins.</p>
{HEALTH_CHECK}"""),
    dict(slug="beating-procrastination", name="Beating procrastination", short="Procrastination",
         teaser="Deal with the feeling first, then the task.",
         uses=["relief-reward", "emotional-bucket", "tipp"],
         body=f"""<p>Deal with the feeling first, then the task.</p>
<ol>
<li><strong>Name the feeling:</strong> "This task makes me anxious" or "bored."</li>
<li><strong>Lower it:</strong> Use {TIPP_LINK}, or remind yourself the feeling will pass.</li>
<li><strong>Make the start tiny:</strong> Commit to only 5 minutes.</li>
<li><strong>Notice the good feeling of doing:</strong> Progress feels better than escape.</li>
</ol>
{HEALTH_CHECK}"""),
    dict(slug="limitless-wish-list", name="Find your real goals: the limitless wish list", short="Wish list",
         teaser="Find what you really want in 15 minutes.",
         uses=[],
         body="""<p>This exercise shows what you really want once "realistic" filters are out of the way. It takes about 15 minutes.</p>
<ol>
<li><strong>Remove every limit.</strong> Imagine there are no limits on age, money, situation, personality or other people. Anything goes, from a private jet to becoming a squirrel.</li>
<li><strong>Write 10 wishes.</strong> List the first 10 things you want. Don't judge or edit them.</li>
<li><strong>Compare in pairs.</strong> Compare wish 1 with wish 2 and keep the one you want more. Compare that winner with wish 3, then with wish 4, and so on to the end of the list. The last one standing is your number one.</li>
<li><strong>Repeat without the winner.</strong> Go back to the top of the list and run the comparisons again, skipping your number one. The new winner is your number two.</li>
<li><strong>Repeat once more.</strong> Skip both winners and run it again to find your number three.</li>
<li><strong>Reflect.</strong> Your top three are a good indication of what you really want. Ask yourself what each one gives you, such as freedom, safety, connection or meaning. Then ask what small, realistic step would move you toward that today.</li>
</ol>"""),
]
BY_SLUG = {b["slug"]: b for b in BLOCKS}


def tiles(items, base):
    return '<div class="tiles">' + "".join(
        f'<a class="tile" href="{base}{i["slug"]}/"><h3>{i["name"]}</h3><p>{i["teaser"]}</p></a>'
        for i in items) + "</div>"


def chips(items, base):
    return '<div class="chips">' + "".join(
        f'<a class="chip" href="{base}{i["slug"]}/">{i["name"]}</a>' for i in items) + "</div>"


def item_page(kind_path, kind_name, item, extra):
    body = f"""<section class="page-head"><div class="wrap narrow">
<a class="back" href="{kind_path}">← {kind_name}</a>
<h1>{item["name"]}</h1><p class="muted">{item["teaser"]}</p></div></section>
<div class="prose"><div class="wrap narrow">
{item["body"]}
{extra}
</div></div>"""
    page(f'{kind_path}{item["slug"]}/', f'{item["name"]} — psiproslab', item["teaser"], body)


def node_map():
    """Brain-style map: building blocks on an outer ring, exercises inside, lines = 'uses'."""
    import math
    cx, cy, R = 200, 200, 158
    pos = {}
    n = len(BLOCKS)
    for k, b in enumerate(BLOCKS):
        a = -math.pi / 2 + 2 * math.pi * k / n
        pos[b["slug"]] = (cx + R * math.cos(a), cy + R * math.sin(a))
    inner = [(200, 128), (146, 238), (254, 238)]
    for e, p in zip(EXERCISES, inner):
        pos[e["slug"]] = p
    lines = "".join(
        f'<line x1="{pos[e["slug"]][0]:.0f}" y1="{pos[e["slug"]][1]:.0f}" x2="{pos[u][0]:.0f}" y2="{pos[u][1]:.0f}"/>'
        for e in EXERCISES for u in e["uses"])
    def node(i, href, cls, r, fill, stroke):
        x, y = pos[i["slug"]]
        return (f'<a href="{href}{i["slug"]}/" class="{cls}"><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
                f'<text x="{x:.0f}" y="{y + r + 14:.0f}" font-size="12" text-anchor="middle" fill="#8a94ab">{i["short"]}</text></a>')
    nodes = "".join(node(b, "/building-blocks/", "nb", 9, "#e6f0fa", "#1b2a4e") for b in BLOCKS)
    nodes += "".join(node(e, "/exercises/", "ne", 13, "#2f7a5b", "#2f7a5b") for e in EXERCISES)
    return f"""<svg class="nodemap" width="100%" style="max-width:440px;height:auto" viewBox="0 -6 400 420" role="img" aria-label="Map of building blocks and the exercises that use them">
<g class="links" stroke="#9aa6bd" stroke-width="1.5">{lines}</g>{nodes}</svg>
<p class="legend"><span class="dot b"></span>Building block <span class="dot e"></span>Exercise · tap a node to open it</p>"""
def g(grade):
    return f'<span class="grade">{grade}</span>'


# ---------- Brain and Sleep ----------
SLEEP = f"""<p><strong>Grades:</strong> A = strong proof, B = some proof, C = little proof.</p>

<h2>The basics that work best</h2>
<ol>
<li><strong>Sleep</strong>{g('A')}: 7–9 hours, at the same times every day. Get daylight in the morning, and dim screens at night.</li>
<li><strong>Move</strong>{g('A')}: Walking, cycling or swimming helps your thinking and your mood.</li>
<li><strong>Eat</strong>{g('B')}: Lots of vegetables, fish and olive oil, like in the Mediterranean.</li>
<li><strong>Focus</strong>{g('B')}: Do one thing at a time and take breaks.</li>
</ol>

<h2>Melatonin: for sleep timing {g('A for jet lag, B for falling asleep')}</h2>
<p>Melatonin tells your body clock "it's night." It sets the time; it doesn't knock you out.</p>
<ul>
<li><strong>Good for:</strong> jet lag, night shifts and night owls. You fall asleep a few minutes faster.</li>
<li><strong>How:</strong> A small dose (0.5–1 mg) works as well as a big one. Take it 1–3 hours before bedtime.</li>
<li><strong>Watch out:</strong> It doesn't cure long-term sleep problems; a sleep therapy called CBT-I does. It can make you groggy or give you headaches or vivid dreams. Rules differ by country: in some, melatonin needs a prescription. Check with your doctor or pharmacist.</li>
</ul>

<h2>Creatine: brain fuel {g('B')}</h2>
<p>Your muscles use creatine, and so does your brain.</p>
<ul>
<li><strong>Good for:</strong> a little better memory, mostly in older people, vegetarians and people short on sleep.</li>
<li><strong>How:</strong> 3–5 g of creatine monohydrate a day.</li>
<li><strong>Watch out:</strong> The effect is small. If you have kidney problems, ask your doctor first.</li>
</ul>

<h2>L-theanine: calm focus {g('B')}</h2>
<p>L-theanine comes from tea.</p>
<ul>
<li><strong>Good for:</strong> together with coffee, it helps you focus without the jitters.</li>
<li><strong>Watch out:</strong> The effect is mild. A cup of green tea gives you both at once.</li>
</ul>

<h2>Omega-3: fish oil {g('B')}</h2>
<p>Your brain is partly built from these fats.</p>
<ul>
<li><strong>Good for:</strong> a small help with low mood. Little effect on memory.</li>
<li><strong>How:</strong> Oily fish twice a week, or about 1 g of fish oil a day.</li>
<li><strong>Watch out:</strong> If you take blood thinners, ask your doctor first.</li>
</ul>

<h2>Lion's mane: a mushroom {g('C')}</h2>
<ul>
<li><strong>Good for:</strong> maybe memory and mood, but it's mostly tested on animals.</li>
<li><strong>Watch out:</strong> Quality differs a lot between brands. A few people get allergic reactions.</li>
</ul>

<h2>Peptides such as BPC-157 {g('C')}</h2>
<ul>
<li><strong>Proof:</strong> Almost no good tests in people.</li>
<li><strong>Watch out:</strong> Often sold online with unknown contents, usually as injections, and many are not approved.</li>
<li><strong>Bottom line:</strong> Not an approved medicine and banned in sport. Best avoided.</li>
</ul>

<p><em>This page is for learning, not medical advice.</em></p>
<p>Want to check the science? See <a href="/sources/">Sources</a>.</p>"""


# ---------- Sources ----------
def src(label, links):
    return "<li>" + label + ": " + " and ".join(f'<a href="{u}">{t}</a>' for t, u in links) + "</li>"


SOURCES = "<h2>Brain and Sleep</h2><ul>" + "".join([
    src("Melatonin", [("Ferracioli-Oda et al., 2013, meta-analysis, PLOS One", "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0063773")]),
    src("Sleep therapy (CBT-I)", [("Trauer et al., 2015, meta-analysis, Annals of Internal Medicine", "https://pubmed.ncbi.nlm.nih.gov/26054060/")]),
    src("Creatine", [("Avgerinos et al., 2018, systematic review, Experimental Gerontology", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6093191/")]),
    src("L-theanine and coffee", [("Owen et al., 2008, trial, Nutritional Neuroscience", "https://pubmed.ncbi.nlm.nih.gov/18681988/")]),
    src("Omega-3 and mood", [("Liao et al., 2019, meta-analysis, Translational Psychiatry", "https://www.nature.com/articles/s41398-019-0515-5")]),
    src("Lion's mane", [("Mori et al., 2009, trial, Phytotherapy Research", "https://pubmed.ncbi.nlm.nih.gov/18844328/")]),
    src("Exercise and thinking", [("Smith et al., 2010, meta-analysis, Psychosomatic Medicine", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2897704/")]),
    src("Mediterranean diet", [("2024 meta-analysis, GeroScience", "https://pubmed.ncbi.nlm.nih.gov/39797935/")]),
    src("Focus and task switching", [("Monsell, 2003, review, Trends in Cognitive Sciences", "https://doi.org/10.1016/S1364-6613(03)00028-7")]),
]) + "</ul><h2>Building blocks</h2><ul>" + "".join([
    src("ABC model and CBT", [("David, Cristea and Hofmann, 2018, Frontiers in Psychiatry", "https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2018.00004/full")]),
    src("Three brains and emotion takes over", [("Arnsten, 2009, review, Nature Reviews Neuroscience", "https://pubmed.ncbi.nlm.nih.gov/19455173/")]),
    src("Instinct is faster", [("LeDoux, 2000, review, Annual Review of Neuroscience", "https://pubmed.ncbi.nlm.nih.gov/10845062/")]),
    src("White bear effect", [("Wegner et al., 1987, experiment", "https://pubmed.ncbi.nlm.nih.gov/3612492/"), ("Abramowitz et al., 2001, meta-analysis", "https://www.sciencedirect.com/science/article/abs/pii/S027273580000057X")]),
    src("Clogged engine", [("Wiehler et al., 2022, Current Biology", "https://pubmed.ncbi.nlm.nih.gov/35961314/"), ("Inzlicht and Friese, 2019, review", "https://econtent.hogrefe.com/doi/10.1027/1864-9335/a000398")]),
    src("Relief reward", [("Sirois and Pychyl, 2013", "https://eprints.whiterose.ac.uk/id/eprint/91793/"), ("Steel, 2007, meta-analysis, Psychological Bulletin", "https://pubmed.ncbi.nlm.nih.gov/17201571/")]),
    src("TIPP", [("Linehan, DBT Skills Training Manual", "https://www.guilford.com/books/DBT-Skills-Training-Manual/Marsha-Linehan/9781462556359")]),
]) + "</ul>"

NOT_FOUND = """<section class="page-head"><div class="wrap narrow"><h1>Page not found</h1>
<p class="muted">This page moved or no longer exists. Start from the <a href="/">home page</a>.</p></div></section>"""

MAP = f"""<section class="band"><div class="wrap narrow">
<h2>How it connects</h2>
{node_map()}</div></section>"""
page("/", "psiproslab — Simple tools for a calmer, sharper mind",
     "Simple, evidence-graded tools for a calmer, sharper mind. The science, explained simply.", HOME + MAP)
page("/building-blocks/", "Building blocks — psiproslab", "Short pieces on how your brain works.",
     article("Building blocks", "Short pieces on how your brain works. Each one stands on its own. Tap a block to open it.",
             tiles(BLOCKS, "/building-blocks/")))
page("/exercises/", "Exercises — psiproslab", "The building blocks put to work on real problems.",
     article("Exercises", "The building blocks put to work on real problems. Tap an exercise to open it.",
             tiles(EXERCISES, "/exercises/")))
for blk in BLOCKS:
    used = [e for e in EXERCISES if blk["slug"] in e["uses"]]
    item_page("/building-blocks/", "Building blocks", blk,
              f'<h2>Used in</h2>{chips(used, "/exercises/")}' if used else "")
for exr in EXERCISES:
    item_page("/exercises/", "Exercises", exr,
              f'<h2>Building blocks used</h2>{chips([BY_SLUG[u] for u in exr["uses"]], "/building-blocks/")}'
              if exr["uses"] else "")
page("/brain-and-sleep/", "Brain and Sleep: what really helps — psiproslab",
     "Sleep, exercise, diet and supplements for the brain, graded A, B or C.",
     article("Brain and Sleep: what really helps",
             "Many pills promise a better brain. Most do little. This page shows what works and what doesn't. "
             "First the basics, because they beat every pill. Ask your doctor before you take anything, "
             "especially if you take medicine, are pregnant or are ill.", SLEEP))
page("/sources/", "Sources — psiproslab", "The studies behind every claim on psiproslab.",
     article("Sources", "For anyone who wants to check the science.", SOURCES))
(ROOT / "404.html").write_text("", encoding="utf-8")
page("/404/", "Page not found — psiproslab", "Page not found.", NOT_FOUND)
(ROOT / "404" / "index.html").rename(ROOT / "404.html")
(ROOT / "404").rmdir()
