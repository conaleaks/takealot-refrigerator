import re

with open('/Users/green/Downloads/Takealot Refrigerator/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace the bullet highlights
old_ul_match = re.search(r'<ul>\s*<li><strong>All-Around Cooling.*?</ul>', text, re.DOTALL)
if old_ul_match:
    new_ul = """<ul>
                <li><strong>All-Around Cooling™ System:</strong> Cools evenly from corner to corner. Cold air is blown through multiple vents on every shelf level, maintaining a constant and optimal temperature so food stays fresh longer.</li>
                <li><strong>Non-Plumbed Water Dispenser:</strong> 4.5L internal slim water tank dispenses chilled filtered water with zero plumbing or pipe installations required.</li>
                <li><strong>Digital Inverter Compressor (20-Year Warranty):</strong> Automatically adjusts cooling speed in response to demand across 7 levels. Uses significantly less energy, runs at 37 dBA whisper-quiet, and comes backed by a 20-year compressor warranty.</li>
                <li><strong>Total No Frost Technology:</strong> Enhances air circulation to maintain constant temperature throughout the fridge, preventing ice and frost buildup on food and interior walls forever.</li>
                <li><strong>Power Freeze &amp; Power Cool:</strong> Delivers a rapid blast of intensely cold air into the freezer or fridge with a single touch, freezing food fast and chilling drinks in minutes.</li>
                <li><strong>Easy Slide Tempered Glass Shelf:</strong> Built on rolling hinges, it slides in and out smoothly so you can efficiently organise and easily access groceries stored right at the back.</li>
                <li><strong>Volt Control &amp; Loadshedding Protection:</strong> Safeguards the refrigerator against high voltage spikes and power fluctuations common during South African load shedding.</li>
            </ul>"""
    text = text[:old_ul_match.start()] + new_ul + text[old_ul_match.end():]
    print("Replaced bullet highlights")

# 2. Replace extra spec rows
old_rows_match = re.search(r'<tr class="extra-spec-row".*?</tr>\s*<tr class="extra-spec-row".*?</tr>\s*<tr class="extra-spec-row".*?</tr>', text, re.DOTALL)
if old_rows_match:
    new_rows = """<tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Cooling Type</td>
                <td class="col-val">All-Around Cooling &amp; Multi Flow</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Defrost Type</td>
                <td class="col-val">Total No Frost (Automatic Defrost)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Water Dispenser Tank</td>
                <td class="col-val">4.5 Litres Non-Plumbed Manual Fill</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Refrigerant</td>
                <td class="col-val">R600a Eco-Friendly Gas</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Door Reversible</td>
                <td class="col-val">Yes (Left or Right Hand Opening)</td>
            </tr>"""
    text = text[:old_rows_match.start()] + new_rows + text[old_rows_match.end():]
    print("Replaced extra spec rows")

# 3. Replace the rugby grass review
old_rev = re.search(r'<div class="review-single-card">.*?rugby grass.*?</div>\s*</div>', text, re.DOTALL)
if old_rev:
    new_rev = """<div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Kagiso Sithole - 26 Sep 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">25</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Keeps braai meat and fresh greens ice cold during weekend gatherings. Power Freeze chills beers in under 20 minutes...</span>
                    <span class="review-full" style="display: none;">Keeps braai meat and fresh greens ice cold during weekend gatherings. Power Freeze chills beers and sodas in under 20 minutes without exploding. The vegetable crisper keeps salad ingredients fresh for two full weeks. Outstanding value from Takealot!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>"""
    text = text[:old_rev.start()] + new_rev + text[old_rev.end():]
    print("Replaced rugby grass review")

with open('/Users/green/Downloads/Takealot Refrigerator/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Finished updating index.html details")
