"""Builds the static psiproslab.com pages from the content below. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
PRIVACY = "https://app.psiproslab.com/privacy/"
NAV = [("/", "Lab"), ("/about/", "About"), ("/mindwork/", "Mindwork"),
       ("/mindtools/", "Mindtools")]


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
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/"><b>Ψ</b>ProsLab</a>
  <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav">{links}<a class="btn" href="/reset/">Free humming reset</a></nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <div class="cols">
    <div>© 2026 MSCPDZ Co., Ltd. · Hua Hin, Thailand<br><a href="mailto:psiproslab@gmail.com">psiproslab@gmail.com</a></div>
    <nav><a href="{PRIVACY}">Privacy policy</a><a href="/mindtools/#disclosure">Affiliate disclosure</a></nav>
  </div>
  <p class="crisis"><strong>In crisis?</strong> ΨProsLab offers self-help resources, not therapy or an emergency service. In Thailand call the Mental Health Hotline <a href="tel:1323">1323</a> or emergency services <a href="tel:1669">1669</a>. Elsewhere, contact your local emergency number.</p>
</div></footer>
<script src="/assets/site.js"></script>
</body>
</html>
"""
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


LEAD = f"""
<section class="band"><div class="wrap narrow" style="text-align:center">
  <span class="tag">Free</span>
  <h2>Get the free 5-minute humming reset</h2>
  <p class="muted">A science-backed breathing protocol you can use anywhere, anytime.</p>
  <form id="lead-form" class="inline-form">
    <label class="hp" aria-hidden="true">Leave empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
    <input type="email" name="email" required placeholder="Your email address" aria-label="Email address" autocomplete="email">
    <button class="btn" type="submit">Send it to me</button>
    <label class="check" style="flex-basis:100%;max-width:520px;margin:0 auto;text-align:left"><input type="checkbox" name="consent" required><span>I'd like the humming reset and occasional ΨProsLab updates. Unsubscribe any time. See the <a href="{PRIVACY}">Privacy Policy</a>.</span></label>
    <p class="msg" role="status" style="flex-basis:100%"></p>
  </form>
</div></section>
"""

# ---------- Lab (home) ----------
page("/", "ΨProsLab — Behavioural science you can practise.",
     "Evidence-based self-help tools and exercises for calm, focus and lasting habits, grounded in behavioural psychology.", f"""
<section class="hero"><div class="wrap">
  <p class="eyebrow">Behavioural psychology · Evidence-based</p>
  <h1>Behavioural science<br>you can practise.</h1>
  <p class="lead">Evidence-based self-help tools and exercises for calm, focus and lasting habits — grounded in behavioural psychology.</p>
  <div class="actions"><a class="btn" href="/reset/">Try the 5-minute humming reset</a><a class="btn ghost" href="#ways">Explore the Lab</a></div>
</div></section>
<section id="ways"><div class="wrap">
  <h2 style="text-align:center">Two ways to practise behavioural science.</h2>
  <div class="cards" style="margin-top:28px">
    <div class="card"><h3>Mindwork</h3><p class="muted">Articles and self-help protocols, grounded in research.</p><a class="more" href="/mindwork/">Explore Mindwork →</a></div>
    <div class="card"><h3>Mindtools</h3><p class="muted">Apps and recommended tools for your practice.</p><a class="more" href="/mindtools/">Explore Mindtools →</a></div>
  </div>
</div></section>
{LEAD}
""")

# ---------- About ----------
page("/about/", "About Pros De Zutter — ΨProsLab",
     "Pros De Zutter, Behavioral Psychologist (MSc, Maastricht University).", """
<section class="page-head"><div class="wrap narrow">
  <p class="eyebrow">About</p>
  <h1>Pros De Zutter</h1>
  <p class="lead muted" style="font-size:19px">Behavioral Psychologist (MSc, Maastricht University)</p>
</div></section>
<section><div class="wrap narrow">
  <p>ΨProsLab turns behavioural science into practical, do-it-yourself tools: short protocols, exercises and apps that help you build calm, focus and habits that last.</p>
  <p>The approach is evidence-based and measurable: we start from what research shows works, set clear goals, and track whether things actually change for you.</p>
  <h2 style="margin-top:1.4em">Methods</h2>
  <ul class="clean">
    <li><strong>Cognitive behavioural therapy (CBT)</strong> — working with thoughts and behaviour patterns that keep problems going.</li>
    <li><strong>Behaviour change &amp; habits</strong> — small, structured steps that stick.</li>
    <li><strong>Breathing &amp; HRV training</strong> — paced breathing and humming practice for calm and focus.</li>
    <li><strong>Motivational interviewing</strong> — finding and strengthening your own reasons to change.</li>
  </ul>
</div></section>
""")

# ---------- Mindwork ----------
page("/mindwork/", "Mindwork — ΨProsLab",
     "Articles and self-help protocols, grounded in research.", f"""
<section class="page-head"><div class="wrap narrow">
  <p class="eyebrow">Mindwork</p>
  <h1>Articles and self-help protocols</h1>
  <p class="muted">Every piece states how strong the evidence behind it is.</p>
</div></section>
<section><div class="wrap">
  <div class="cards">
    <div class="card"><span class="tag">Strong evidence</span><p class="muted" style="margin:0">Supported by systematic reviews or meta-analyses.</p></div>
    <div class="card"><span class="tag blue">Promising</span><p class="muted" style="margin:0">Supported by controlled trials, but not yet by large reviews.</p></div>
    <div class="card"><span class="tag" style="background:var(--line);color:var(--muted)">Early</span><p class="muted" style="margin:0">Based on small studies or expert consensus; try with curiosity.</p></div>
  </div>
  <h2 style="margin-top:48px">Coming soon</h2>
  <div class="cards">
    <div class="card"><h3>The 5-minute humming reset</h3><p class="muted">A short breathing protocol for calm and focus.</p><a class="more" href="/reset/">Read it now →</a></div>
    <div class="card"><h3>Habits that last</h3><p class="muted">Why small, specific steps beat motivation.</p><p class="muted" style="margin:0">Coming soon</p></div>
    <div class="card"><h3>Untangling worry</h3><p class="muted">CBT tools for thoughts that keep you awake.</p><p class="muted" style="margin:0">Coming soon</p></div>
  </div>
</div></section>
{LEAD}
""")

# ---------- Mindtools ----------
page("/mindtools/", "Mindtools — ΨProsLab",
     "Apps and recommended tools for your practice.", """
<section class="page-head"><div class="wrap narrow">
  <p class="eyebrow">Mindtools</p>
  <h1>Apps and tools for your practice</h1>
</div></section>
<section><div class="wrap">
  <div class="cards">
    <div class="card"><span class="tag">ΨProsLab app</span><h3>Humming Trainer</h3><p class="muted">Adaptive humming and breathing practice for calm and focus. Sessions adjust to your pace and progress.</p><p class="muted" style="margin:0">Coming soon to Google Play</p></div>
    <div class="card"><h3>Recommended tools — coming soon</h3><p class="muted" style="margin:0">Carefully selected, evidence-informed tools will be listed here soon.</p></div>
  </div>
  <p id="disclosure" class="muted" style="font-size:14px;margin-top:28px"><strong>Affiliate disclosure:</strong> some links on this page may be affiliate links. If you buy through them, ΨProsLab may earn a small commission at no extra cost to you. We only recommend tools we consider useful and evidence-informed.</p>
</div></section>
""")

# ---------- Humming reset ----------
page("/reset/", "The 5-minute humming reset — ΨProsLab",
     "A short humming and breathing protocol for calm and focus.", """
<section class="page-head"><div class="wrap narrow">
  <p class="eyebrow">Mindwork · Protocol</p>
  <h1>The 5-minute humming reset</h1>
  <span class="tag">Strong evidence</span> <span class="muted" style="font-size:14px">for slow breathing · humming itself: promising</span>
</div></section>
<section><div class="wrap narrow">
  <h2>How to do it</h2>
  <ol class="steps">
    <li><span><strong>Sit comfortably</strong>, shoulders relaxed. Set a timer for 5 minutes.</span></li>
    <li><span><strong>Breathe in through your nose</strong> for about 4 seconds.</span></li>
    <li><span><strong>Hum out with your lips closed</strong> for about 6 seconds, a low, comfortable "mmm". Feel the buzz in your face and chest.</span></li>
    <li><span><strong>Repeat</strong> for 5 minutes. That is about 6 breaths a minute. If it's easy, lengthen the hum a little.</span></li>
    <li><span><strong>Notice</strong> how you feel before and after, on a scale of 0–10.</span></li>
  </ol>
  <h2 style="margin-top:1.4em">Why it works</h2>
  <ul class="clean">
    <li>Breathing at around 6 breaths a minute, with a longer out-breath, reliably increases heart rate variability, a marker of calm, recovery and self-regulation (meta-analyses).</li>
    <li>Humming slows and lengthens the out-breath automatically, which makes this pace easy to keep.</li>
    <li>Humming also raises nitric oxide in the nose many times over compared with quiet breathing (controlled lab studies).</li>
  </ul>
  <p class="muted" style="font-size:14px">This is a wellness exercise, not a medical treatment. Stop if you feel dizzy. If you have a health concern, consult a healthcare professional.</p>
  <p style="margin-top:1.6em"><a class="btn" href="/mindtools/">Practise with Humming Trainer</a></p>
</div></section>
""")

print("built")
