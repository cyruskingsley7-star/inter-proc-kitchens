from pathlib import Path
import json

p = Path("index.html")
html = p.read_text(encoding="utf-8")
marker = "<!-- INTER-PROC SEO metadata v1 -->"
if marker in html:
    print("SEO metadata already present")
    raise SystemExit(0)
if "</head>" not in html:
    raise SystemExit("Cannot find document head")
business = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "@id": "https://inter-proc.com/#business",
    "name": "INTER-PROC",
    "url": "https://inter-proc.com/",
    "logo": "https://inter-proc.com/inter-proc-logo.png",
    "image": "https://inter-proc.com/inter-proc-logo.png",
    "description": "INTER-PROC designs, builds and installs custom kitchens and cabinetry in Uganda.",
    "telephone": ["+256752400883", "+256761470436"],
    "email": "interprocug@gmail.com",
    "areaServed": {"@type": "Country", "name": "Uganda"},
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Custom kitchens and cabinetry",
        "itemListElement": [
            {"@type": "OfferCatalog", "name": "Custom fitted kitchen cabinetry"},
            {"@type": "OfferCatalog", "name": "Cabinet making and installation"}
        ]
    }
}
# No invented physical address, map pin, opening hours, ratings or reviews.
seo = """
<!-- INTER-PROC SEO metadata v1 -->
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="INTER-PROC">
<meta property="og:image" content="https://inter-proc.com/inter-proc-logo.png">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="https://inter-proc.com/">
<script type="application/ld+json">""" + json.dumps(business, separators=(",", ":")).replace("</", "<\\/") + """</script>
<script>
(function () {
  var pages = {
    "/": ["Custom Kitchens & Cabinetry in Uganda | INTER-PROC", "INTER-PROC designs, builds and installs custom fitted kitchens and cabinetry in Uganda. Explore original kitchen projects and contact our team."],
    "/work": ["Kitchen Projects & Before-and-After Photos | INTER-PROC", "Explore real INTER-PROC kitchen projects in Uganda, including original before-and-after photographs of fitted cabinetry and kitchen installations."],
    "/craft": ["Kitchen Cabinetry & Craftsmanship | INTER-PROC", "Discover INTER-PROC's approach to custom cabinetry, kitchen finishes and carefully fitted kitchen storage in Uganda."],
    "/process": ["Our Kitchen Design & Installation Process | INTER-PROC", "Learn how INTER-PROC approaches custom kitchen cabinetry and installation, from discussing your requirements to fitting the finished work."],
    "/about": ["About INTER-PROC | Kitchen Cabinetry in Uganda", "Learn about INTER-PROC, a Ugandan business creating custom fitted kitchens and cabinetry."],
    "/contact": ["Contact INTER-PROC | Custom Kitchens in Uganda", "Contact INTER-PROC about custom kitchen cabinets and installation in Uganda. Call 0752 400 883 or 0761 470 436, or message us on WhatsApp."]
  };
  var path = location.pathname.replace(/\\/$/, "") || "/";
  var entry = pages[path] || pages["/"];
  document.title = entry[0];
  var desc = document.querySelector('meta[name="description"]');
  if (desc) desc.setAttribute("content", entry[1]);
  var canonical = document.querySelector('link[rel="canonical"]');
  if (canonical) canonical.setAttribute("href", "https://inter-proc.com" + (pages[path] ? path : "/"));
  var ogTitle = document.createElement("meta");
  ogTitle.setAttribute("property", "og:title");
  ogTitle.setAttribute("content", entry[0]);
  document.head.appendChild(ogTitle);
  var ogDesc = document.createElement("meta");
  ogDesc.setAttribute("property", "og:description");
  ogDesc.setAttribute("content", entry[1]);
  document.head.appendChild(ogDesc);
  var ogUrl = document.createElement("meta");
  ogUrl.setAttribute("property", "og:url");
  ogUrl.setAttribute("content", "https://inter-proc.com" + (pages[path] ? path : "/"));
  document.head.appendChild(ogUrl);
})();
</script>
"""
html = html.replace("</head>", seo + "\n</head>", 1)
p.write_text(html, encoding="utf-8")
print("SEO metadata, per-page titles/descriptions/canonicals, social metadata, and honest business structured data added")
