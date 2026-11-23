import os, re, json

BASE_DIR = "/Users/green/Downloads/Takealot Refrigerator"
HERO_CDN = "https://files.catbox.moe/fvy3gd.jpg"
OPEN_CDN = "https://files.catbox.moe/3zcemq.jpg"
DISPENSER_CDN = "https://files.catbox.moe/yzkw8u.jpg"
INTERIOR_CDN = "https://files.catbox.moe/4rig0s.jpg"

HERO_TITLE = "Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox"
HERO_MODEL = "RB30J3611S9/FA"
HERO_PRICE = "2,199"
HERO_OLD_PRICE = "R 9,999"

# =========================================================================
# 1. UPDATE INDEX.HTML
# =========================================================================
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace <title>
html = re.sub(r'<title>.*?</title>', f'<title>{HERO_TITLE} ({HERO_MODEL}) | Takealot</title>', html)

# Replace breadcrumbs
html = re.sub(
    r'<div class="breadcrumb-bar".*?</div>',
    '<div class="breadcrumb-bar" style="padding: 10px 16px; font-size: 11.5px; color: #666; background: #fff; border-bottom: 1px solid #f0f0f0; display: flex; align-items: center; gap: 6px; overflow-x: auto; white-space: nowrap;">'
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Home</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Kitchen & Large Appliances</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Large Appliances</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<span style="color: #333; font-weight: 500;">Refrigerators & Freezers</span></div>',
    html,
    flags=re.DOTALL
)

# Replace product-title
html = re.sub(
    r'<h1 class="product-title" id="main-product-title">.*?</h1>',
    f'<h1 class="product-title" id="main-product-title">{HERO_TITLE} ({HERO_MODEL})</h1>',
    html
)

# Replace carousel slides
carousel_replacement = """        <div class="carousel-slide"><img src="imagens/samsung_fridge_1_hero.jpg" alt="Samsung 300L Bottom Freezer Refrigerator Hero Front" /></div>
        <div class="carousel-slide"><img src="imagens/samsung_fridge_2_open.jpg" alt="Samsung 300L Refrigerator Open Doors Interior" /></div>
        <div class="carousel-slide"><img src="imagens/samsung_fridge_3_dispenser.jpg" alt="Samsung Refrigerator Water Dispenser Detail" /></div>
        <div class="carousel-slide"><img src="imagens/samsung_fridge_4_interior.jpg" alt="Samsung Refrigerator Multi Flow Interior Shelving" /></div>"""

html = re.sub(
    r'<div class="carousel-track" id="carousel-track">.*?</div>\s*<div class="dots-row"',
    f'<div class="carousel-track" id="carousel-track">\n{carousel_replacement}\n    </div>\n    <div class="dots-row"',
    html,
    flags=re.DOTALL
)

# Replace price display
html = re.sub(
    r'<span class="price-val" id="main-price-display">.*?</span>',
    f'<span class="price-val" id="main-price-display">R {HERO_PRICE}</span>',
    html
)
html = re.sub(
    r'<span class="price-old" id="main-old-price">.*?</span>',
    f'<span class="price-old" id="main-old-price">{HERO_OLD_PRICE}</span>',
    html
)

# Replace footer price display
html = re.sub(
    r'<span class="bar-price" id="footer-price-display">.*?</span>',
    f'<span class="bar-price" id="footer-price-display">R {HERO_PRICE}</span>',
    html
)

# Replace variation pills section
pills_replacement = """    <div class="variation-selector-sec">
        <div class="variation-header-row">
            <span>Capacity / Model: <strong id="selected-size-label">300L Inox (RB30)</strong></span>
            <span style="font-size: 11.5px; color: var(--takealot-blue); font-weight: 600;"><i class="fas fa-sliders" style="margin-right: 3px;"></i> Choose variant</span>
        </div>
        <div class="variation-pills-row">
            <button class="var-pill" data-var-key="254l" onclick="selectProductVariation('254l')">
                254L Defy <span class="pill-badge">R 1,499</span>
            </button>
            <button class="var-pill" data-var-key="298l" onclick="selectProductVariation('298l')">
                298L Hisense <span class="pill-badge">R 1,899</span>
            </button>
            <button class="var-pill active" data-var-key="300l" onclick="selectProductVariation('300l')">
                300L Samsung Inox <span class="pill-badge" style="background: #007a3d;">Hot R 2,199</span>
            </button>
            <button class="var-pill" data-var-key="432l" onclick="selectProductVariation('432l')">
                432L Side-by-Side <span class="pill-badge">R 2,999</span>
            </button>
            <button class="var-pill" data-var-key="300l-bundle" onclick="selectProductVariation('300l-bundle')">
                300L + Surge Bundle <span class="pill-badge">R 2,399</span>
            </button>
        </div>
    </div>"""

html = re.sub(
    r'<div class="variation-selector-sec">.*?</div>\s*</div>\s*<!-- 6\. TakealotMORE Banner',
    f'{pills_replacement}\n\n    <!-- 6. TakealotMORE Banner',
    html,
    flags=re.DOTALL
)

# Replace What's Hot carousel
hot_replacement = """    <div class="category-hot-sec">
        <div class="sec-title" style="margin-bottom: 12px;">What's Hot in Refrigerators</div>
        <div class="hot-carousel">
            <!-- Variation 1: Defy 254L -->
            <div class="hot-card" data-var-key="254l" onclick="selectProductVariation('254l', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">75%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_fridge_1_hero.jpg" alt="Defy 254L Bottom Freezer Fridge" />
                </div>
                <div class="hot-title">Defy 254L Bottom Freezer Fridge Metallic (DAD254)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,499</span>
                    <span class="hot-old-price">R 5,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.7 (890)</div>
            </div>

            <!-- Variation 2: Hisense 298L -->
            <div class="hot-card" data-var-key="298l" onclick="selectProductVariation('298l', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">76%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_fridge_3_dispenser.jpg" alt="Hisense 298L Bottom Freezer with Dispenser" />
                </div>
                <div class="hot-title">Hisense 298L Bottom Freezer with Water Dispenser (H370)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 1,899</span>
                    <span class="hot-old-price">R 7,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.8 (1,420)</div>
            </div>

            <!-- Variation 3: Samsung 300L Hero -->
            <div class="hot-card active-selection" data-var-key="300l" onclick="selectProductVariation('300l', true)">
                <div class="hot-badges">
                    <div class="badge-black">Top<br>Seller.</div>
                    <div class="badge-blue">78%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_fridge_1_hero.jpg" alt="Samsung 300L Bottom Freezer Inox" />
                </div>
                <div class="hot-title">Samsung 300L Bottom Freezer Refrigerator + Dispenser (RB30)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 2,199</span>
                    <span class="hot-old-price">R 9,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (2,416)</div>
            </div>

            <!-- Variation 4: Samsung 432L Side-by-Side -->
            <div class="hot-card" data-var-key="432l" onclick="selectProductVariation('432l', true)">
                <div class="hot-badges">
                    <div class="badge-black">SpaceMax</div>
                    <div class="badge-blue">82%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_fridge_4_interior.jpg" alt="Samsung 432L Side-by-Side Inox" />
                </div>
                <div class="hot-title">Samsung 432L Side-by-Side Inox Refrigerator (RS64)</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 2,999</span>
                    <span class="hot-old-price">R 16,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (672)</div>
            </div>

            <!-- Variation 5: 300L Bundle -->
            <div class="hot-card" data-var-key="300l-bundle" onclick="selectProductVariation('300l-bundle', true)">
                <div class="hot-badges">
                    <div class="badge-black">Bundle<br>Deal</div>
                    <div class="badge-blue">78%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/samsung_fridge_2_open.jpg" alt="Samsung 300L Refrigerator + Surge Protector" />
                </div>
                <div class="hot-title">Samsung 300L Inox + Fridge Surge Protector & Odor Filter</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 2,399</span>
                    <span class="hot-old-price">R 10,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (518)</div>
            </div>
        </div>
    </div>"""

html = re.sub(
    r'<div class="category-hot-sec">.*?</div>\s*</div>\s*<!-- 8\. Divider -->',
    f'{hot_replacement}\n\n    <!-- 8. Divider -->',
    html,
    flags=re.DOTALL
)

# Replace Other Offers seller
html = re.sub(
    r'<div class="offer-seller-name">.*?</div>',
    '<div class="offer-seller-name">KIC & Appliance Megastore SA</div>',
    html
)
html = re.sub(
    r'<div class="offer-price">R \d+[\d,]*</div>',
    '<div class="offer-price">R 2,299</div>',
    html
)

# Replace Product Specifications
specs_replacement = """        <div class="spec-row">
            <span class="spec-label">Brand</span>
            <span class="spec-val">Samsung</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Model Number</span>
            <span class="spec-val" id="spec-model-number">RB30J3611S9/FA</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Total Net Capacity</span>
            <span class="spec-val" id="spec-screen-size">300 Litres (Fridge: 202L, Freezer: 98L)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Cooling System</span>
            <span class="spec-val">All-Around Cooling & Multi Flow Air Circulation</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Defrost Technology</span>
            <span class="spec-val">Total No Frost (Frost Free System)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Water Dispenser</span>
            <span class="spec-val">4.5L Non-Plumbed In-Door Dispenser (No plumbing required)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Compressor</span>
            <span class="spec-val">Digital Inverter Compressor with 20-Year Warranty</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Energy Efficiency</span>
            <span class="spec-val">A+ Rating (Low Loadshedding Power Consumption)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Noise Level</span>
            <span class="spec-val">37 dBA (Whisper Quiet Inverter)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Shelving & Storage</span>
            <span class="spec-val">Tempered Glass Easy Slide Shelves + Humidity Controlled Crisper</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Dimensions & Weight</span>
            <span class="spec-val">595mm (W) x 1780mm (H) x 668mm (D) | 66.5 kg</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Finish</span>
            <span class="spec-val">Premium Inox Metallic (Fingerprint Resistant)</span>
        </div>"""

html = re.sub(
    r'<div class="spec-table">.*?</div>\s*</div>\s*<!-- Description Tab Content -->',
    f'<div class="spec-table">\n{specs_replacement}\n        </div>\n    </div>\n    <!-- Description Tab Content -->',
    html,
    flags=re.DOTALL
)

# Replace Description Tab Content
desc_replacement = """    <div id="desc-tab-content" class="tab-content">
        <h3 style="font-size: 15px; margin-bottom: 10px; color: #222;">Evenly Cools Every Corner of Your Fridge</h3>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            The <strong>Samsung 300L Bottom Freezer Refrigerator (RB30J3611S9)</strong> is engineered specifically for South African households. With <strong>All-Around Cooling</strong>, cold air is blown out through multiple vents on every shelf level, maintaining a steady, even temperature from top to bottom so your fresh groceries, meat, and dairy stay crisp and fresh up to twice as long.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            <strong>Chilled Water on Demand Without Plumbing:</strong> The built-in 4.5-litre slimline water tank is completely non-plumbed. Simply fill the dispenser tank with filtered or tap water and enjoy ice-cold, refreshing water straight through the outer door paddle. No plumber, no pipes, and zero installation hassle.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            <strong>Built to Beat Loadshedding:</strong> Powered by Samsung's celebrated <strong>Digital Inverter Compressor</strong>, which automatically adjusts its speed across 7 cooling levels in response to cooling demand. It uses significantly less power than conventional compressors, recovers interior temperatures in minutes when power returns after loadshedding, and runs whisper-quiet at just 37 dBA with a 20-year compressor warranty.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555;">
            <strong>Total No Frost Technology:</strong> Prevents frost and ice buildup on freezer walls and food packaging, eliminating manual defrosting forever and preserving the texture and flavour of frozen foods.
        </p>
    </div>"""

html = re.sub(
    r'<div id="desc-tab-content" class="tab-content">.*?</div>\s*</div>\s*<!-- 14\. Customer Reviews',
    f'{desc_replacement}\n    </div>\n    <!-- 14. Customer Reviews',
    html,
    flags=re.DOTALL
)

# Replace 14 Authentic South African Customer Reviews
reviews_replacement = """        <div class="reviews-list-container">
            <!-- Review 1 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Johan van der Merwe - 18 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">38</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Survives loadshedding effortlessly. The inverter compressor cools down rapidly when power returns and meat stays frozen solid...</span>
                    <span class="review-full" style="display: none;">Survives loadshedding effortlessly. The inverter compressor cools down rapidly when power returns and meat stays frozen solid even during 4-hour power cuts here in Sandton. The bottom freezer setup is so ergonomic. R 2,199 on Takealot promo is unbeatable!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 2 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Nthabiseng Khumalo - 15 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">29</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The non-plumbed water dispenser is a lifesaver. We fill the 4.5L tank and always have chilled water without any plumbing pipes...</span>
                    <span class="review-full" style="display: none;">The non-plumbed water dispenser is a lifesaver. We fill the 4.5L tank and always have chilled water without any plumbing pipes. Kids love it, no dripping or mess. The Inox finish doesn't show greasy fingerprints either.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 3 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>David Naidoo - 12 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">24</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">300L is the sweet spot for a family of four. Fresh vegetables stay crisp for over 10 days in the humidity crisper...</span>
                    <span class="review-full" style="display: none;">300L is the sweet spot for a family of four. Fresh vegetables stay crisp for over 10 days in the humidity crisper. We live in humid Durban North and our old fridge would turn greens to mush in 3 days. This Samsung All-Around cooling actually works.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 4 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Willem Steenkamp - 09 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">19</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Extremely quiet. Our kitchen is open-plan and you cannot even hear the Digital Inverter motor running...</span>
                    <span class="review-full" style="display: none;">Extremely quiet. Our kitchen is open-plan and you cannot even hear the Digital Inverter motor running. Also noticed our monthly prepaid electricity units lasting significantly longer thanks to the A+ energy rating. Stellar quality.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 5 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Sipho Mthembu - 06 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">31</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Takealot large appliance delivery team brought it right into my kitchen, unboxed it, and carried away the packaging...</span>
                    <span class="review-full" style="display: none;">Takealot large appliance delivery team brought it right into my kitchen, unboxed it, and carried away the packaging. Driver called 30 mins before arrival. Fridge settled for 2 hours, plugged in and chilled down to 3°C in under an hour.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 6 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Liezl Pretorius - 03 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">17</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The Inox metallic finish is smudge and fingerprint resistant. Beautiful sleek modern look in Pretoria East...</span>
                    <span class="review-full" style="display: none;">The Inox metallic finish is smudge and fingerprint resistant. Beautiful sleek modern look in Pretoria East. Deep door balconies comfortably fit 2L milk bottles and wine bottles upright. Very happy with this purchase.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 7 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Pieter Fourie - 31 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">22</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Freezes ice cubes in under 45 minutes on Power Freeze mode. Great for hot Free State summers in Bloemfontein...</span>
                    <span class="review-full" style="display: none;">Freezes ice cubes in under 45 minutes on Power Freeze mode. Great for hot Free State summers in Bloemfontein. The three transparent freezer drawers pull out completely making it easy to organise meat packages.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 8 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Zanele Dlamini - 28 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">26</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The bottom freezer design is so ergonomic. Fresh food at eye level means no more bending down for daily groceries...</span>
                    <span class="review-full" style="display: none;">The bottom freezer design is so ergonomic. Fresh food at eye level means no more bending down for daily groceries. Interior LED light is bright and lights up every corner clearly at night. Best fridge on the market.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 9 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Francois Meyer - 24 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">14</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Digital temperature controls on the door are accurate and easy to use. Great build quality from Samsung...</span>
                    <span class="review-full" style="display: none;">Digital temperature controls on the door are accurate and easy to use. Great build quality from Samsung. Tested the internal temperature with a probe thermometer and it stayed rock solid at 3.2°C across 48 hours.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 10 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Brenda Cooper - 20 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">18</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The Easy Slide shelf pulls out smoothly so you can reach jars at the very back without knocking things over...</span>
                    <span class="review-full" style="display: none;">The Easy Slide shelf pulls out smoothly so you can reach jars at the very back without knocking things over. Build quality feels sturdy and premium. Takealot delivery was swift and driver was very courteous in Gqeberha.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 11 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Thabo Molefe - 16 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">21</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Best purchase of 2026. The 20-year compressor warranty gives peace of mind in Roodepoort...</span>
                    <span class="review-full" style="display: none;">Best purchase of 2026. The 20-year compressor warranty gives peace of mind. Power surges often blow appliances in Gauteng, but paired with a good surge plug this Samsung is unstoppable. Definite 5 stars.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 12 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Anet Botha - 11 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">15</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">No frost buildup whatsoever. The multi-airflow keeps milk and dairy consistently cold on every shelf...</span>
                    <span class="review-full" style="display: none;">No frost buildup whatsoever. The multi-airflow keeps milk and dairy consistently cold on every shelf. In Nelspruit heat, fridges usually struggle, but this unit keeps ice cream at the perfect firmness. Love it!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 13 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Clinton Pillay - 07 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">33</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">R 2,199 on promotion was an absolute steal for a 300L Samsung. Delivered in 48 hours to Chatsworth...</span>
                    <span class="review-full" style="display: none;">R 2,199 on promotion was an absolute steal for a 300L Samsung. Delivered in 48 hours to Chatsworth. Excellent communication on the tracking link with driver location. Will recommend Takealot appliance deals to all my colleagues.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 14 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Marika Louw - 02 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">20</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Wine rack and deep door bins easily fit 2L milk cartons and cool drink bottles in Paarl...</span>
                    <span class="review-full" style="display: none;">Wine rack and deep door bins easily fit 2L milk cartons and cool drink bottles in Paarl. The non-plumbed dispenser tank is easy to remove and wash in warm soapy water. Outstanding craftsmanship!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>
        </div>"""

html = re.sub(
    r'<div class="reviews-list-container">.*?</div>\s*</div>\s*<!-- Write a Review Button',
    f'{reviews_replacement}\n    </div>\n    <!-- Write a Review Button',
    html,
    flags=re.DOTALL
)

# Replace Javascript productVariations in index.html
js_variations = """    const productVariations = {
        "254l": {
            id: "254l",
            size: "254L Defy",
            title: "Defy 254L Bottom Freezer Fridge Metallic (DAD254)",
            price: "1499",
            oldPrice: "R 5,999",
            discount: "75%<br>OFF",
            credit: "R 124 p/m x 12 months",
            ebucks: "eB14,990",
            miles: "14,990",
            image: "imagens/samsung_fridge_1_hero.jpg",
            images: [
                "imagens/samsung_fridge_1_hero.jpg",
                "imagens/samsung_fridge_2_open.jpg",
                "imagens/samsung_fridge_3_dispenser.jpg",
                "imagens/samsung_fridge_4_interior.jpg"
            ],
            screenSizeSpec: "254 Litres (Metallic Finish)",
            modelSpec: "DAD254 / DAD254M"
        },
        "298l": {
            id: "298l",
            size: "298L Hisense",
            title: "Hisense 298L Bottom Freezer with Water Dispenser (H370)",
            price: "1899",
            oldPrice: "R 7,999",
            discount: "76%<br>OFF",
            credit: "R 158 p/m x 12 months",
            ebucks: "eB18,990",
            miles: "18,990",
            image: "imagens/samsung_fridge_3_dispenser.jpg",
            images: [
                "imagens/samsung_fridge_3_dispenser.jpg",
                "imagens/samsung_fridge_1_hero.jpg",
                "imagens/samsung_fridge_2_open.jpg",
                "imagens/samsung_fridge_4_interior.jpg"
            ],
            screenSizeSpec: "298 Litres (Water Dispenser)",
            modelSpec: "H370BIT-WD"
        },
        "300l": {
            id: "300l",
            size: "300L Inox (RB30)",
            title: "Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)",
            price: "2199",
            oldPrice: "R 9,999",
            discount: "78%<br>OFF",
            credit: "R 183 p/m x 12 months",
            ebucks: "eB21,990",
            miles: "21,990",
            image: "imagens/samsung_fridge_1_hero.jpg",
            images: [
                "imagens/samsung_fridge_1_hero.jpg",
                "imagens/samsung_fridge_2_open.jpg",
                "imagens/samsung_fridge_3_dispenser.jpg",
                "imagens/samsung_fridge_4_interior.jpg"
            ],
            screenSizeSpec: "300 Litres (All-Around Cooling & Dispenser)",
            modelSpec: "RB30J3611S9/FA"
        },
        "432l": {
            id: "432l",
            size: "432L Side-by-Side",
            title: "Samsung 432L Side-by-Side Inox Refrigerator (RS64)",
            price: "2999",
            oldPrice: "R 16,999",
            discount: "82%<br>OFF",
            credit: "R 249 p/m x 12 months",
            ebucks: "eB29,990",
            miles: "29,990",
            image: "imagens/samsung_fridge_4_interior.jpg",
            images: [
                "imagens/samsung_fridge_4_interior.jpg",
                "imagens/samsung_fridge_1_hero.jpg",
                "imagens/samsung_fridge_2_open.jpg",
                "imagens/samsung_fridge_3_dispenser.jpg"
            ],
            screenSizeSpec: "432 Litres (SpaceMax Inox)",
            modelSpec: "RS64R5311B4/FA"
        },
        "300l-bundle": {
            id: "300l-bundle",
            size: "300L + Surge Bundle",
            title: "Samsung 300L Inox Refrigerator + Surge Protector & Odor Filter Bundle",
            price: "2399",
            oldPrice: "R 10,999",
            discount: "78%<br>OFF",
            credit: "R 199 p/m x 12 months",
            ebucks: "eB23,990",
            miles: "23,990",
            image: "imagens/samsung_fridge_2_open.jpg",
            images: [
                "imagens/samsung_fridge_2_open.jpg",
                "imagens/samsung_fridge_1_hero.jpg",
                "imagens/samsung_fridge_3_dispenser.jpg",
                "imagens/samsung_fridge_4_interior.jpg"
            ],
            screenSizeSpec: "300L + Fridge Surge Protector & CleanAir Filter",
            modelSpec: "RB30J3611S9-BNDL"
        }
    };"""

html = re.sub(
    r'const productVariations = \{.*?\n\s*\};\s*let selectedVariationKey =',
    f'{js_variations}\n\n    let selectedVariationKey = "300l";',
    html,
    flags=re.DOTALL
)

# Also ensure default selectedVariationKey is "300l"
html = html.replace('let selectedVariationKey = "9kg";', 'let selectedVariationKey = "300l";')
html = html.replace('selectedPrice = "1899"', 'selectedPrice = "2199"')
html = html.replace('selectedTitle = "Samsung 9kg', 'selectedTitle = "Samsung 300L')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html successfully")

# =========================================================================
# 2. UPDATE CHECKOUT.HTML
# =========================================================================
checkout_path = os.path.join(BASE_DIR, "checkout.html")
with open(checkout_path, "r", encoding="utf-8") as f:
    chk = f.read()

chk = re.sub(r'<title>.*?</title>', f'<title>Checkout - {HERO_TITLE} | Takealot</title>', chk)
chk = chk.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine (RB30J3611S9)", HERO_TITLE)
chk = chk.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
chk = chk.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine", HERO_TITLE)
chk = chk.replace("Samsung 9kg All-Around Cooling", HERO_TITLE)
chk = chk.replace("Samsung Bottom Freezer Washing Machine", HERO_TITLE)
chk = chk.replace("imagens/samsung_washer_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
chk = chk.replace("imagens/samsung_ww80_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
chk = chk.replace("1899", "2199")
chk = chk.replace("1,899", "2,199")
chk = chk.replace("8,999", "9,999")
chk = chk.replace("All-Around Cooling & Total No Frost", "All-Around Cooling & Water Dispenser")

with open(checkout_path, "w", encoding="utf-8") as f:
    f.write(chk)
print("Updated checkout.html successfully")

# =========================================================================
# 3. UPDATE CART.HTML
# =========================================================================
cart_path = os.path.join(BASE_DIR, "cart.html")
with open(cart_path, "r", encoding="utf-8") as f:
    crt = f.read()

crt = re.sub(r'<title>.*?</title>', f'<title>Shopping Cart - {HERO_TITLE} | Takealot</title>', crt)
crt = crt.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine (RB30J3611S9)", HERO_TITLE)
crt = crt.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
crt = crt.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer", HERO_TITLE)
crt = crt.replace("Samsung Bottom Freezer Washing Machine", HERO_TITLE)
crt = crt.replace("imagens/samsung_washer_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
crt = crt.replace("imagens/samsung_ww80_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
crt = crt.replace("1899", "2199")
crt = crt.replace("1,899", "2,199")
crt = crt.replace("8,999", "9,999")

with open(cart_path, "w", encoding="utf-8") as f:
    f.write(crt)
print("Updated cart.html successfully")

# =========================================================================
# 4. UPDATE TRACK.HTML
# =========================================================================
track_path = os.path.join(BASE_DIR, "track.html")
with open(track_path, "r", encoding="utf-8") as f:
    trk = f.read()

trk = re.sub(r'<title>.*?</title>', f'<title>Track Your Order - {HERO_TITLE} | Takealot</title>', trk)
trk = trk.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine (RB30J3611S9)", HERO_TITLE)
trk = trk.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
trk = trk.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer", HERO_TITLE)
trk = trk.replace("Samsung Bottom Freezer Washing Machine", HERO_TITLE)
trk = trk.replace("imagens/samsung_washer_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
trk = trk.replace("imagens/samsung_ww80_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
trk = trk.replace("1899", "2199")
trk = trk.replace("1,899", "2,199")
trk = trk.replace("8,999", "9,999")
trk = trk.replace("9kg Inox (WW90)", "300L Inox (RB30)")
trk = trk.replace("Large Appliance White Glove Delivery (To Your Kitchen)", "Large Appliance White Glove Delivery (To Your Kitchen)")

with open(track_path, "w", encoding="utf-8") as f:
    f.write(trk)
print("Updated track.html successfully")

# =========================================================================
# 5. UPDATE OBRIGADO.HTML
# =========================================================================
obrigado_path = os.path.join(BASE_DIR, "obrigado.html")
with open(obrigado_path, "r", encoding="utf-8") as f:
    obr = f.read()

obr = re.sub(r'<title>.*?</title>', f'<title>Order Confirmed - {HERO_TITLE} | Takealot</title>', obr)
obr = obr.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine (RB30J3611S9)", HERO_TITLE)
obr = obr.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
obr = obr.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer", HERO_TITLE)
obr = obr.replace("Samsung Bottom Freezer Washing Machine", HERO_TITLE)
obr = obr.replace("imagens/samsung_washer_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
obr = obr.replace("imagens/samsung_ww80_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
obr = obr.replace("1899", "2199")
obr = obr.replace("1,899", "2,199")
obr = obr.replace("8,999", "9,999")

with open(obrigado_path, "w", encoding="utf-8") as f:
    f.write(obr)
print("Updated obrigado.html successfully")

# =========================================================================
# 6. UPDATE UPGRADE-SHIPPING.HTML
# =========================================================================
upg_path = os.path.join(BASE_DIR, "upgrade-shipping.html")
with open(upg_path, "r", encoding="utf-8") as f:
    upg = f.read()

upg = re.sub(r'<title>.*?</title>', f'<title>Priority Delivery Upgrade - {HERO_TITLE} | Takealot</title>', upg)
upg = upg.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine (RB30J3611S9)", HERO_TITLE)
upg = upg.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
upg = upg.replace("Samsung Bottom Freezer Washing Machine", HERO_TITLE)
upg = upg.replace("imagens/samsung_washer_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
upg = upg.replace("imagens/samsung_ww80_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
upg = upg.replace("kitchen", "kitchen")
upg = upg.replace("Kitchen", "Kitchen")

with open(upg_path, "w", encoding="utf-8") as f:
    f.write(upg)
print("Updated upgrade-shipping.html successfully")

# =========================================================================
# 7. UPDATE ALL API SCRIPTS
# =========================================================================
api_dir = os.path.join(BASE_DIR, "api")
for root, dirs, files in os.walk(api_dir):
    for fn in files:
        fpath = os.path.join(root, fn)
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        orig = content
        content = content.replace("Samsung 9kg All-Around Cooling™ Bottom Freezer Washing Machine (RB30J3611S9)", HERO_TITLE)
        content = content.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
        content = content.replace("Samsung 8kg Bottom Freezer Washing Machine", HERO_TITLE)
        content = content.replace("Samsung 8kg Bottom Freezer", HERO_TITLE)
        content = content.replace("Samsung Bottom Freezer Washing Machine", HERO_TITLE)
        content = content.replace("Bottom Freezer Washing Machine", "Bottom Freezer Refrigerator")
        content = content.replace("Washing Machine", "Refrigerator")
        content = content.replace("washing machine", "refrigerator")
        content = content.replace("3015", "3020")
        content = content.replace("1899", "2199")
        content = content.replace("1,899", "2,199")
        content = content.replace("8,999", "9,999")
        content = content.replace("6,499", "9,999")
        
        # Replace image URLs with HERO_CDN
        content = re.sub(r'https://files\.catbox\.moe/[a-z0-9]+\.(?:jpg|png)', HERO_CDN, content)
        
        if content != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {fn}")

print("\n--- ALL REFRIGERATOR FILES UPDATED SUCCESSFULLY ---")
