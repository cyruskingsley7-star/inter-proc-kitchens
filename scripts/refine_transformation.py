from pathlib import Path
import re
p=Path("index.html")
html=p.read_text(encoding="utf-8")
if 'id="transformation"' not in html:
    raise SystemExit("Existing transformation section not found")
css = """
/* INTER-PROC: clearly labelled real-project transformation */
.transformation{scroll-margin-top:110px}
.transformation .story-head{max-width:1020px;margin-bottom:2.5rem}
.transformation .story-head .eyebrow{color:#cc001b;font-weight:800;letter-spacing:.14em;text-transform:uppercase;font-size:.74rem}
.transformation .story-head h2{font-family:Georgia,serif;font-size:clamp(2.6rem,5.5vw,5.7rem);font-weight:400;line-height:1.05;letter-spacing:-.045em;margin:.7rem 0 1.15rem}
.transformation .story-head>p:last-child{color:#5d5953;max-width:730px;font-size:clamp(.98rem,1.5vw,1.17rem);line-height:1.7}
.transformation .story-compare{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.transformation .story-panel{position:relative;margin:0;min-width:0;background:#e5e0d8}
.transformation .story-panel img{display:block;width:100%;height:clamp(340px,44vw,590px);object-fit:cover}
.transformation .story-flag{position:absolute;left:1rem;top:1rem;z-index:1;padding:.85rem 1.05rem;background:#1c1b19;color:white;font-size:clamp(.88rem,1.4vw,1.1rem);font-weight:850;letter-spacing:.1em}
.transformation .story-panel.is-after .story-flag{background:#c9001b}
.transformation .story-panel figcaption{display:block;padding:1.25rem 1.15rem 1.35rem;border-bottom:2px solid #252321;letter-spacing:normal;text-transform:none;font-weight:400;font-size:.95rem;line-height:1.5}
.transformation .story-panel figcaption strong{display:block;font-size:1.17rem;margin-bottom:.3rem;font-weight:750}
.transformation .story-panel figcaption span{color:#5d5953}
.transformation .story-results{padding:2.2rem 0 2.8rem;border-bottom:1px solid #d4cdc3}
.transformation .story-results h3{font-family:Georgia,serif;font-size:clamp(1.65rem,3vw,2.7rem);font-weight:400;margin:0 0 1.2rem}
.transformation .story-results ul{list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;padding:0;margin:0}
.transformation .story-results li{border-top:3px solid #c9001b;padding:1rem 0;font-size:.96rem;line-height:1.5;font-weight:650}
.transformation .story-steps-title{padding:3.5rem 0 1.8rem}
.transformation .story-steps-title h3{font-family:Georgia,serif;font-size:clamp(1.9rem,3.5vw,3.3rem);font-weight:400;margin:0 0 .5rem}
.transformation .story-steps-title p{color:#66615c;line-height:1.6}
.transformation .story-step{display:grid;grid-template-columns:minmax(200px,.75fr) minmax(0,1.25fr);gap:clamp(1.2rem,4vw,4rem);padding:2.1rem 0;border-top:1px solid #d4cdc3;align-items:start}
.transformation .story-step-number{display:inline-block;color:#c9001b;font-size:.76rem;font-weight:850;letter-spacing:.14em;margin-bottom:.8rem}
.transformation .story-step h4{font-family:Georgia,serif;font-size:clamp(1.55rem,2.5vw,2.5rem);font-weight:400;line-height:1.15;margin:0 0 .9rem}
.transformation .story-step p{color:#615d57;line-height:1.7;font-size:.96rem;max-width:380px}
.transformation .story-step-images{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}
.transformation .story-step-images.one{grid-template-columns:1fr}
.transformation .story-step-images img{width:100%;height:clamp(210px,26vw,370px);object-fit:cover;display:block;background:#dedbd5}
.transformation .story-step-images.one img{height:clamp(270px,36vw,470px);object-position:center 35%}
.transformation .story-step-images figcaption{font-size:.75rem;text-transform:none;letter-spacing:normal;font-weight:550;padding:.7rem 0;border-bottom:0;color:#57524d}
.transformation .story-cta-wrap{border-top:1px solid #d4cdc3;padding-top:1rem}
@media(max-width:760px){.transformation .story-compare{grid-template-columns:1fr}.transformation .story-panel img{height:auto;max-height:600px;aspect-ratio:4/5}.transformation .story-results ul{grid-template-columns:1fr;gap:0}.transformation .story-step{grid-template-columns:1fr;gap:1rem}.transformation .story-step-images img{height:auto;aspect-ratio:3/4}.transformation .story-step-images.one img{height:auto;max-height:530px;aspect-ratio:4/5}.transformation .story-head{margin-bottom:1.6rem}}
"""
section = """
<section id="transformation" class="transformation scroll-section" tabindex="-1" aria-labelledby="transform-title">
  <header class="story-head">
    <p class="eyebrow">Real INTER-PROC project · Before &amp; after</p>
    <h2 id="transform-title">One kitchen.<br>Two very different stages.</h2>
    <p>See how this same space changed from an empty, tiled room into a fitted kitchen. These are original photographs taken before and after INTER-PROC's cabinetry installation.</p>
  </header>
  <div class="story-compare" aria-label="Before and after photographs of the same kitchen project">
    <figure class="story-panel is-before">
      <span class="story-flag">BEFORE</span>
      <img src="/transformations/before-01.jpg" alt="BEFORE: the empty kitchen with tiled walls, floor and window but no cabinets" loading="lazy">
      <figcaption><strong>Before INTER-PROC</strong><span>An empty tiled room, ready for the kitchen cabinetry to be fitted.</span></figcaption>
    </figure>
    <figure class="story-panel is-after">
      <span class="story-flag">AFTER</span>
      <img src="/transformations/after-02.jpg" alt="AFTER: the same kitchen fitted with grey cabinetry, white counters and illuminated glass upper cabinets" loading="lazy">
      <figcaption><strong>After the cabinetry installation</strong><span>Grey fitted cabinets, worktops, sink, hob and illuminated upper storage.</span></figcaption>
    </figure>
  </div>
  <div class="story-results">
    <h3>What changed?</h3>
    <ul>
      <li>Custom-fitted lower and upper cabinets</li>
      <li>Marble-look worktops with sink and hob</li>
      <li>Glass-fronted storage with warm cabinet lighting</li>
    </ul>
  </div>
  <div class="story-steps-title">
    <h3>How the transformation happened.</h3>
    <p>Three clear stages, photographed on the actual site.</p>
  </div>
  <article class="story-step">
    <div><span class="story-step-number">STAGE 01 / BEFORE</span><h4>The starting point</h4><p>The walls and floor were tiled, but there was no fitted kitchen storage or worktop yet. The space was ready for cabinetry.</p></div>
    <div class="story-step-images">
      <figure><img src="/transformations/before-02.jpg" alt="Empty tiled kitchen wall before the cabinetry was installed" loading="lazy"><figcaption>Empty wall, before installation</figcaption></figure>
      <figure><img src="/transformations/before-04.jpg" alt="View through the kitchen opening before installation" loading="lazy"><figcaption>Room viewed from the opening</figcaption></figure>
    </div>
  </article>
  <article class="story-step">
    <div><span class="story-step-number">STAGE 02 / AFTER INSTALLATION</span><h4>Cabinetry in place</h4><p>Lower and upper grey cabinets were fitted around the room, creating practical storage and usable worktop space.</p></div>
    <div class="story-step-images">
      <figure><img src="/transformations/after-01.jpg" alt="INTER-PROC team member checking the installed lower kitchen cabinet storage" loading="lazy"><figcaption>Checking the fitted lower cabinets</figcaption></figure>
      <figure><img src="/transformations/after-03.jpg" alt="INTER-PROC team member inspecting the hob and fitted grey cabinets" loading="lazy"><figcaption>Worktop and hob area</figcaption></figure>
    </div>
  </article>
  <article class="story-step">
    <div><span class="story-step-number">STAGE 03 / DETAILS</span><h4>The finishing touches</h4><p>Glass-fronted upper cupboards and warm internal lighting add a polished, practical finish. Here, an INTER-PROC team member demonstrates the cabinet doors.</p></div>
    <div class="story-step-images one">
      <figure><img src="/transformations/after-04.jpg" alt="INTER-PROC team member opening the illuminated upper glass-fronted kitchen cabinets" loading="lazy"><figcaption>Glass cabinet doors and internal lighting</figcaption></figure>
    </div>
  </article>
  <div class="story-cta-wrap"><a class="transform-cta" href="https://wa.me/256752400883?text=Hello%20INTER-PROC%2C%20I%20saw%20your%20kitchen%20transformation%20and%20would%20like%20to%20discuss%20mine." target="_blank" rel="noopener noreferrer">Discuss your kitchen ↗</a></div>
</section>
"""
html, count = re.subn(r'<section id="transformation".*?</section>', lambda m:section, html, count=1, flags=re.S)
if count != 1: raise SystemExit("Could not uniquely replace transformation section")
if '/* INTER-PROC: clearly labelled real-project transformation */' not in html:
    html=html.replace('</style>',css+'\n</style>',1)
if html.count('id="transformation"')!=1: raise SystemExit("Duplicate transformation section")
for photo in ['before-01.jpg','after-02.jpg','before-02.jpg','before-04.jpg','after-01.jpg','after-03.jpg','after-04.jpg']:
    if not (Path('transformations')/photo).exists(): raise SystemExit('Missing '+photo)
p.write_text(html,encoding="utf-8")
print("Installed clearly labelled before/after story, three stages and 7 original photographs")
