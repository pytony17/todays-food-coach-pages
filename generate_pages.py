import os
import random

keywords = [
"meal plan for men over 50",
"diet without calorie counting",
"intermittent fasting meal plan",
"healthy eating after 45",
"how men over 50 should eat",
"simple diet plan for busy professionals",
"weight loss meal plan for men 50",
"easy healthy meals for men over 40",
"how to stop counting calories",
"healthy meal planning for men over 45"
]

meal_examples = [
    ["Greek yogurt with berries", "Grilled chicken salad", "Salmon with roasted vegetables"],
    ["Egg omelet with spinach", "Turkey avocado wrap", "Steak with sweet potato"],
    ["Protein smoothie", "Quinoa bowl with chicken", "Baked cod with broccoli"],
    ["Scrambled eggs and fruit", "Chicken and rice bowl", "Shrimp stir fry"],
    ["Cottage cheese with nuts", "Tuna salad", "Roast chicken with vegetables"]
]

tips = [
    [
    "Focus on protein at every meal",
    "Reduce processed foods",
    "Drink water before meals"
    ],
    [
    "Plan meals ahead of time",
    "Keep healthy snacks nearby",
    "Prioritize sleep for metabolism"
    ],
    [
    "Avoid extreme dieting",
    "Eat slowly and mindfully",
    "Balance protein, fats, and carbs"
    ],
    [
    "Prepare meals in batches",
    "Choose whole foods",
    "Limit sugary drinks"
    ]
]

os.makedirs("pages", exist_ok=True)

def slugify(text):
    return text.lower().replace(" ", "-")

# Create slug lookup
pages = {kw: slugify(kw) for kw in keywords}

def build_related_links(current_kw):

    others = [kw for kw in keywords if kw != current_kw]

    # randomly select 3 other pages
    related = random.sample(others, min(3, len(others)))

    links = ""

    for r in related:
        slug = pages[r]
        title = r.title()
        links += f'<li><a href="{slug}.html">{title}</a></li>\n'

    return links

template = """
<!DOCTYPE html>
<html>

<head>
<title>{title}</title>

<meta name="description" content="Guide to {title}">

<link rel="stylesheet" href="../style.css">

</head>

<body>

<div class="container">

<p class="backlink">
<a href="../index.html">← Back to all nutrition guides</a>
</p>

<h1>{title}</h1>

<p>
Eating well becomes more important as we get older.
This guide explains a simple approach to {title}.
</p>

<div class="image-section">

<img
src="https://source.unsplash.com/800x400/?healthy-food,meal"
alt="Healthy meal example">

</div>

<h2>Why It Matters</h2>

<p>
Many people struggle with complicated diet plans and calorie tracking.
A simpler system often works better.
</p>

<h2>Simple Strategy</h2>

<p>
Focus on whole foods, protein, vegetables, and consistent meals.
Avoid overly restrictive dieting.
</p>

<h2>Example Meals</h2>

<p>
<h2>Example Day of Eating</h2>

<ul>
    <li>Breakfast: {breakfast}</li>
    <li>Lunch: {lunch}</li>
    <li>Dinner: {dinner}</li>
</ul>

</p>

<h2>3 Practical Tips</h2>

<ul>
    <li>{tip1}</li>
    <li>{tip2}</li>
    <li>{tip3}</li>
</ul>


<h2>Related Nutrition Guides</h2>

<ul>
{related_links}
</ul>

<div class="cta">

<h2>Try Today's Food Coach</h2>

<p>
Create a personalized meal plan using AI.
</p>

<p>
<a href="https://todays-food-coach--pytony18.replit.app/">
Try the AI Food Coach
</a>
</p>

</div>

</div>

</body>
</html>
"""

for kw in keywords:

    slug = pages[kw]
    related_links = build_related_links(kw)

    meals = random.choice(meal_examples)
    tipset = random.choice(tips)

    html = template.format(
        title=kw.title(),
        related_links=related_links,
        breakfast=meals[0],
        lunch=meals[1],
        dinner=meals[2],
        tip1=tipset[0],
        tip2=tipset[1],
        tip3=tipset[2],
        keyword=kw.replace(" ", "")
    )

    with open(f"pages/{slug}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("Pages generated successfully")
