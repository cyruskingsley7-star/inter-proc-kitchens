from pathlib import Path
import json, re

p = Path("index.html")
html = p.read_text(encoding="utf-8")

# Update existing structured data without inventing a street address or storefront.
pattern = r'(<script type="application/ld\+json">)(.*?)(</script>)'
m = re.search(pattern, html, flags=re.S)
if not m:
    raise SystemExit("INTER-PROC structured data not found")
data = json.loads(m.group(2))
if data.get("name") != "INTER-PROC":
    raise SystemExit("Unexpected business structured data")
data["description"] = "INTER-PROC is based in Kampala, Uganda and designs, builds and installs custom kitchens and cabinetry."
data["areaServed"] = {"@type": "City", "name": "Kampala"}
html = html[:m.start()] + m.group(1) + json.dumps(data, separators=(",", ":")) + m.group(3) + html[m.end():]

# Update SEO copy where it is defined in the existing per-page metadata script.
old = {
  "Custom Kitchens & Cabinetry in Uganda | INTER-PROC": "Custom Kitchens & Cabinetry in Kampala | INTER-PROC",
  "INTER-PROC designs, builds and installs custom fitted kitchens and cabinetry in Uganda. Explore original kitchen projects and contact our team.": "Based in Kampala, Uganda, INTER-PROC designs, builds and installs custom fitted kitchens and cabinetry. Explore original projects and contact our team.",
  "Kitchen Projects & Before-and-After Photos | INTER-PROC": "Kitchen Projects in Kampala | INTER-PROC",
  "Explore real INTER-PROC kitchen projects in Uganda, including original before-and-after photographs of fitted cabinetry and kitchen installations.": "Explore real INTER-PROC kitchen projects from Kampala, Uganda, including original before-and-after photographs of fitted cabinetry.",
  "About INTER-PROC | Kitchen Cabinetry in Uganda": "About INTER-PROC | Kitchen Cabinetry in Kampala",
  "Learn about INTER-PROC, a Ugandan business creating custom fitted kitchens and cabinetry.": "Learn about INTER-PROC, a Kampala-based business creating custom fitted kitchens and cabinetry.",
  "Contact INTER-PROC | Custom Kitchens in Uganda": "Contact INTER-PROC | Custom Kitchens in Kampala",
  "Contact INTER-PROC about custom kitchen cabinets and installation in Uganda. Call 0752 400 883 or 0761 470 436, or message us on WhatsApp.": "Contact Kampala-based INTER-PROC about custom kitchen cabinetry. Call 0752 400 883 or 0761 470 436, or message us on WhatsApp."
}
for a,b in old.items():
    if a not in html:
        raise SystemExit("Expected SEO copy not found: " + a)
    html=html.replace(a,b,1)

# Make the verified city visible to customers on the contact section.
contact = '<p class="reveal" style="--reveal-delay: 70ms;">Tell us about your space, what you need and what you would like it to become.</p>'
if contact not in html:
    raise SystemExit("Contact section insertion point not found")
html=html.replace(contact,contact+'\n          <p class="reveal" style="--reveal-delay: 70ms;">Based in Kampala, Uganda.</p>',1)

footer = '<p>INTER-PROC · Custom kitchens and cabinetry</p>'
if footer not in html:
    raise SystemExit("Footer insertion point not found")
html=html.replace(footer,'<p>INTER-PROC · Custom kitchens and cabinetry · Kampala, Uganda</p>',1)

p.write_text(html,encoding="utf-8")
print("Added verified Kampala location to visible contact/footer, SEO metadata, and structured business data.")
