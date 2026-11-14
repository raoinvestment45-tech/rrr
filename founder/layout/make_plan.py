S=17; OX=40; OY=60  # px per metre, origin
W,H=40,37.5
out=[]
def r(x,y,w,h,fill,label="",sub="",stroke="#333",sw=1.5,dash=None,fs=13,ly=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    out.append(f'<rect x="{OX+x*S}" y="{OY+y*S}" width="{w*S}" height="{h*S}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    if label:
        cx=OX+(x+w/2)*S; cy=OY+((y+h/2) if ly is None else ly)*S
        out.append(f'<text x="{cx}" y="{cy-(6 if sub else 0)}" font-size="{fs}" font-weight="700" text-anchor="middle">{label}</text>')
        if sub: out.append(f'<text x="{cx}" y="{cy+10}" font-size="11" text-anchor="middle">{sub}</text>')
def t(x,y,s,fs=11,a="middle",c="#333",b=False):
    out.append(f'<text x="{OX+x*S}" y="{OY+y*S}" font-size="{fs}" text-anchor="{a}" fill="{c}"{" font-weight=\"700\"" if b else ""}>{s}</text>')
def tab(x,y,n=4,round_=False):
    if round_:
        out.append(f'<circle cx="{OX+x*S}" cy="{OY+y*S}" r="{0.45*S}" fill="#c9a26b" stroke="#6b4f2a"/>')
    else:
        out.append(f'<rect x="{OX+(x-0.45)*S}" y="{OY+(y-0.45)*S}" width="{0.9*S}" height="{0.9*S}" fill="#c9a26b" stroke="#6b4f2a"/>')
    for dx,dy in [(-0.75,0),(0.75,0),(0,-0.75),(0,0.75)][:n]:
        out.append(f'<circle cx="{OX+(x+dx)*S}" cy="{OY+(y+dy)*S}" r="{0.22*S}" fill="#fff" stroke="#6b4f2a"/>')
def tree(x,y,rad=0.9):
    out.append(f'<circle cx="{OX+x*S}" cy="{OY+y*S}" r="{rad*S}" fill="#7cbf6b" stroke="#3d7a2f" opacity="0.85"/>')

# plot + green base
r(0,0,W,H,"#e8f3df",stroke="#000",sw=3)
# road
out.append(f'<rect x="{OX-20}" y="{OY+H*S+4}" width="{W*S+40}" height="{2.6*S}" fill="#888"/>')
t(W/2,H+1.9,"MAIN ROAD (frontage 40 m)",12,c="#fff",b=True)

# ---- parking y 21.5-37.5
r(0,21.5,W,16,"#d9d9d9",stroke="#555")
t(W/2,29.9,"DRIVE AISLE 6 m  (two-way)",12,b=True)
out.append(f'<path d="M {OX+3*S} {OY+29.5*S} h {6*S} m -10 -6 l 10 6 l -10 6" stroke="#333" fill="none" stroke-width="2"/>')
out.append(f'<path d="M {OX+37*S} {OY+29.5*S} h {-6*S} m 10 -6 l -10 6 l 10 6" stroke="#333" fill="none" stroke-width="2"/>')
n=0
def stall(x,y,w=2.5,acc=False):
    global n; n+=1
    r(x,y,w,5,"#f4f4f4" if not acc else "#cfe3ff",stroke="#555",sw=1)
    t(x+w/2,y+2.9,("♿" if acc else "")+f"P{n}",10)
for i in range(7): stall(i*2.5,21.5)
stall(22,21.5,3.6,True)
for i in range(5): stall(25.6+i*2.5,21.5)
for i in range(12): stall(5+i*2.5,32.5)
r(0,32.5,5,5,"#bdbdbd","IN",stroke="#555",fs=12)
r(35,32.5,5,5,"#bdbdbd","OUT",stroke="#555",fs=12)
# pedestrian path / drop-off
r(17.5,20,4.5,6.5,"#f6e7c1","",stroke="#a07c2c",dash="4 3")
t(19.75,24,"Walkway &amp;",9.5); t(19.75,25,"drop-off",9.5)
# hedge buffer
r(0,20,17.5,1.5,"#5a9e4b",stroke="none"); r(22,20,18,1.5,"#5a9e4b",stroke="none")
t(8.75,21.05,"green hedge buffer",9,c="#fff")

# ---- cafe zone y 0-20
r(0,0,14,13,"#fde9c9","MEMBERS DINING","40 seats · indoor / AC",fs=14,ly=11.4)
for cx in [2.3,5.9,9.5]:
    for cy in [1.8,4.9,8.0]:
        tab(cx,cy)
tab(12.3,4.9);  # 10 tables x4 = 40
r(0,13.5,11,6.5,"#ffd6d6","NON-MEMBERS · 25 seats",fs=11,ly=14.5)
for cx in [1.8,4.7,7.6]: tab(cx,15.8)
tab(9.95,15.8,2)
for cx in [1.8,4.7]: tab(cx,18.9)
tab(7.6,18.9,3)
t(9.9,19.7,"door ↓",9)
r(11,13.5,3,3.25,"#dbe7f5","MALE","WC",fs=9.5)
r(11,16.75,3,3.25,"#dbe7f5","FEMALE","WC",fs=9.5)
r(14,0,7,6,"#dbe7f5","MEMBERS' TOILETS","M · W · ♿ · baby",fs=11.5)
r(21,0,12,6,"#e6e6e6","KITCHEN + STORE","~72 m² · dishwash",fs=13)
r(21,6,12,2,"#c7a27c","CAFÉ BAR + CARD TOP-UP",fs=10)
r(33,0,7,6,"#d4d4c4","BACK OF HOUSE","staff · bins · compost",fs=11)
r(37,6,3,14,"#efefe6",stroke="#888",dash="4 3")
out.append(f'<text x="{OX+38.6*S}" y="{OY+13*S}" font-size="10" text-anchor="middle" transform="rotate(-90 {OX+38.6*S} {OY+13*S})">service path to kitchen</text>')
r(14,6,7,2,"#e8f3df",stroke="#888",dash="4 3"); t(17.5,7.3,"corridor to toilets",9)
r(14,8,18,7,"#fff6b8","MEMBERS CAFÉ GARDEN LOUNGE · 35 seats","open deck · sofas · swings · counter stools",fs=12,ly=14.15)
for cx in [16,19.5,26.5,30]: tab(cx,10.4,4,True)
for cx in [23]: tab(cx,10.4,3,True)
for cx in [16,30]: tab(cx,12.0,4,True)
 # 6x4+3=27
# counter bar stools along lounge top
for i in range(8): out.append(f'<circle cx="{OX+(21.6+i*1.4)*S}" cy="{OY+8.6*S}" r="{0.25*S}" fill="#fff" stroke="#6b4f2a"/>')
r(32,6,5,14,"#b9dcae","","",stroke="#3d7a2f",sw=2); tree(34.5,9,1.5); tree(34.5,17.3,1.3)
t(34.5,12.6,"GARDEN 1",11,b=True); t(34.5,13.6,"SMOKING",11,b=True); t(34.5,14.6,"open-air",9.5)
r(14,15,10,5,"#f6e7c1","ENTRY PLAZA · card tap",fs=11.5,ly=16)
out.append(f'<rect x="{OX+18*S}" y="{OY+16.8*S}" width="{2*S}" height="{0.9*S}" fill="#8b5e34"/>')
t(19,18.6,"reception",9,c="#333")
t(14.3,19.5,"← non-members",9.5,a="start"); t(23.7,19.5,"members ↑",9.5,a="end")
r(24,15,8,5,"#cfe8c4",stroke="#3d7a2f",sw=2)
for (x,y) in [(25.3,18.4),(30.7,18.4)]: tree(x,y,1.0)
t(28,16.3,"GARDEN 2 · GREEN",10.5,b=True); t(28,17.4,"no smoking",9); t(28,18.6,"water feature",9); t(28,19.5,"+ herbs",9)
for (x,y) in [(1,1),(13,12.4)]: pass

# north arrow + scale
out.append(f'<g transform="translate({OX+W*S+40},{OY+20})"><path d="M0 30 L10 0 L20 30 L10 22 Z" fill="#333"/><text x="10" y="45" font-size="12" text-anchor="middle">N (rear)</text></g>')
out.append(f'<line x1="{OX}" y1="{OY-20}" x2="{OX+10*S}" y2="{OY-20}" stroke="#000" stroke-width="3"/>')
t(0,-1.6,"0",10,a="start"); t(10,-1.6,"10 m",10,a="end")
t(W/2,-2.4,"DRAFT SITE PLAN v3 — 40 m × 37.5 m plot (≈1,500 m² ≈ 1,800 sq yd) · not to construction standard",13,b=True)
# legend
L=[("Members dining","#fde9c9"),("Members café lounge","#fff6b8"),("Non-member dine-in","#ffd6d6"),("Kitchen / BOH","#e6e6e6"),("Toilets","#dbe7f5"),("Garden 1 (smoking)","#b9dcae"),("Garden 2 (green)","#cfe8c4"),("Parking","#d9d9d9")]
lx=OX+W*S+30; ly=OY+90
for i,(k,c) in enumerate(L):
    out.append(f'<rect x="{lx}" y="{ly+i*22}" width="16" height="14" fill="{c}" stroke="#333"/><text x="{lx+22}" y="{ly+i*22+12}" font-size="12">{k}</text>')
summ=["SEATS: 40 + 35 members","          + 25 non-members = 100","CARS: 25 (incl. 1 accessible)","Stall 2.5×5 m · aisle 6 m","Covered build ≈ 450 m²","Parking ≈ 640 m²","Toilets: members + non-member M/F"]
for i,s in enumerate(summ):
    out.append(f'<text x="{lx}" y="{ly+200+i*18}" font-size="12"{" font-weight=\"700\"" if i<3 else ""}>{s}</text>')
CW=OX+W*S+250; CH=OY+H*S+70
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}" font-family="Arial, Helvetica, sans-serif"><rect width="100%" height="100%" fill="#fff"/>'+"".join(out)+'</svg>'
open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),"site-plan.svg"),"w").write(svg)
print("stalls",n)
