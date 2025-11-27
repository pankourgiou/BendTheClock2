import math
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# ---------------------------------------------------------
# Utility
# ---------------------------------------------------------

def polar_to_cart(r, theta):
    return r * math.cos(theta), r * math.sin(theta)

def draw_clock(ax, hour_labels, time_dt, title):
    radius = 1.0

    ax.set_aspect('equal')
    ax.set_xlim(-1.15*radius, 1.15*radius)
    ax.set_ylim(-1.15*radius, 1.15*radius)
    ax.axis('off')

    # Circle
    ax.add_artist(plt.Circle((0,0), radius, fill=False, linewidth=1.6))

    # Labels + hour ticks
    label_radius = 0.82 * radius
    for h in range(12):
        angle = (math.pi/2) - (h * (2*math.pi/12))
        outer = polar_to_cart(radius, angle)
        inner = polar_to_cart(radius*0.92, angle)
        ax.plot([outer[0], inner[0]], [outer[1], inner[1]], linewidth=1)

        lx, ly = polar_to_cart(label_radius, angle)
        ax.text(lx, ly, hour_labels[h], ha='center', va='center', fontsize=10)

    # Time calculations
    hour = time_dt.hour % 12
    minute = time_dt.minute
    second = time_dt.second + time_dt.microsecond/1e6

    hour_angle = (math.pi/2) - ((hour + minute/60.0) * (2*math.pi/12))
    minute_angle = (math.pi/2) - (minute * (2*math.pi/60))
    second_angle = (math.pi/2) - (second * (2*math.pi/60))

    hx, hy = polar_to_cart(radius*0.5, hour_angle)
    mx, my = polar_to_cart(radius*0.75, minute_angle)
    sx, sy = polar_to_cart(radius*0.88, second_angle)

    # Hands
    ax.plot([0, hx], [0, hy], linewidth=3)
    ax.plot([0, mx], [0, my], linewidth=2)
    ax.plot([0, sx], [0, sy], linewidth=0.8)

    ax.add_artist(plt.Circle((0,0), 0.03, color='k'))
    ax.set_title(title, fontsize=9, pad=6)

# ---------------------------------------------------------
# YOUR EXACT LABEL SETS FROM YOUR FILE  (UNCHANGED)
# ---------------------------------------------------------

cuneiform = [ "☉Iron","☽so1d","♂dt","♀Contra","☿Mantra","♃Neun","♄Mcl","♅4","♆rb21","♇zzk","⚳zz","⚴z" ]
cuneiform = [cuneiform[11]] + cuneiform[:11]

runes = [ ":):)",":)1@#%",":z",":w","co:(","coo:(","ceo:(","ion:):(","play:)","r0ck:8","+12","+123" ]
runes = [runes[11]] + runes[:11]

alchemy = [ "☉","☽","♂","♀","☿","♃","♄","♅","♆","♇","⚳","⚴" ]
alchemy = [alchemy[11]] + alchemy[:11]

starborn = [ "<N","<I","<C","<K","<O",">O","^A","B^^2","^%^C","42317j%%","010254opap","kali0,89" ]
starborn = [starborn[11]] + starborn[:11]

dev_digits = [ "1☉","1☽","12♂","5♀","7☿","3♃","4♄","3♅","t♆","o♇","o⚳","l⚴" ]
devanagari = []
for i in range(12):
    val = 12 if i == 0 else i
    devanagari.append("".join(dev_digits[int(ch)] for ch in str(val)))

math_ops = [ "∅","∇","∆","∂","∞","≈","⊕","⊗","≡","≥","≤","±" ]
math_ops = [math_ops[11]] + math_ops[:11]

zodiac = [ "Ϸ","ϸ","ע","ד","Ϫ","Ϭ","Ϯ","ϰ","Ͼ","Ҩ","Ҵ","Ҷ" ]
zodiac = [zodiac[11]] + zodiac[:11]

techno = [ "a∅","aa∇","c∆","cba∂","4∞","9≈","a3ca⊕","co⊗","10≡","001≥","4abc≤","0±" ]
techno = [techno[11]] + techno[:11]

geometry = [ "Ϟ","ϟ","Ϡ","ϡ","҉","҈","҂","N9ck҃","҄N0ck","҅N3ck","҆Zer","҇Ekh" ]
geometry = [geometry[11]] + geometry[:11]

spectral = [ "Ϟ","ϟ","Ϡ","ϡ","҉","҈","҂","҃","҄","҅","҆","҇" ]
spectral = [spectral[11]] + spectral[:11]

label_sets = [
    (cuneiform,      "Neo-Cuneiform"),
    (runes,          "Runic Numerals"),
    (alchemy,        "Alchemical Symbols"),
    (starborn,       "Starborn Script"),
    (devanagari,     "Devanagari Exotic"),
    (math_ops,       "Math Operators"),
    (zodiac,         "Zodiac Set"),
    (techno,         "Techno-Alien"),
    (geometry,       "Geometry Script"),
    (spectral,       "Spectral Script")
]

# ---------------------------------------------------------
# REAL-TIME ANIMATION FOR ALL 10 CLOCKS
# ---------------------------------------------------------

fig, axes = plt.subplots(2, 5, figsize=(16, 7))
axes = axes.flatten()

def init():
    """Draw correctly on creation so the FIRST frame is accurate."""
    now = datetime.datetime.now()
    for idx, (labels, title) in enumerate(label_sets):
        ax = axes[idx]
        ax.clear()
        draw_clock(ax, labels, now, title)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    return []

def update(frame):
    """Redraw all 10 clocks every second."""
    now = datetime.datetime.now()
    for idx, (labels, title) in enumerate(label_sets):
        ax = axes[idx]
        ax.clear()
        draw_clock(ax, labels, now, title)
    return []

ani = animation.FuncAnimation(
    fig,
    update,
    init_func=init,
    interval=1000,   # 1 second
    blit=False
)

plt.suptitle("10 Exotic Real-Time Working Clocks", fontsize=14)
plt.show()
