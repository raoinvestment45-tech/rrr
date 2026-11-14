"""Draft site plan v2 for Green Card Cafe. Run: python3 make_plan.py -> site-plan.svg"""
import os
S=16; OX=40; OY=70
W,H=42,39.5
out=[]
def r(x,y,w,h,fill,label="",sub="",stroke="#333",sw=1.5,dash=None,fs=13,ly=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    out.append(f'<rect x="{OX+x*S}" y="{OY+y*S}" width="{w*S}" height="{h*S}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    if label:
        cx=OX+(x+w/2)*S; cy=OY+((y+h/2) if ly is None else ly)*S
        out.append(f'<text x="{cx}" y="{cy-(6 if sub else 0)}" font-size="{fs}" font-weight="700" text-anchor="middle">{label}</text>')
        if sub: out.append(f'<text x="{cx}" y="{cy+10}" font-size="10.5" text-anchor="middle">{sub}</text>')
def t(x,y,s,fs=10,a="middle",c="#333",b=False,rot=0):
    tr=f' transform="rotate({rot} {OX+x*S} {OY+y*S})"' if rot else ''
    out.append(f'<text x="{OX+x*S}" y="{OY+y*S}" font-size="{fs}" text-anchor="{a}" fill="{c}"{" font-weight=\"700\"" if b else ""}{tr}>{s}</text>')
seats={"dining":0,"lounge":0,"nm":0}
def tab(x,y,n=4,round_=False,zone=None):
    if zone: seats[zone]+=n
    if round_: out.append(f'<circle cx="{OX+x*S}" cy="{OY+y*S}" r="{0.45*S}" fill="#c9a26b" stroke="#6b4f2a"/>')
    else: out.append(f'<rect x="{OX+(x-0.45)*S}" y="{OY+(y-0.45)*S}" width="{0.9*S}" height="{0.9*S}" fill="#c9a26b" stroke="#6b4f2a"/>')
    for dx,dy in [(-0.75,0),(0.75,0),(0,-0.75),(0,0.75)][:n]:
        out.append(f'<circle cx="{OX+(x+dx)*S}" cy="{OY+(y+dy)*S}" r="{0.22*S}" fill="#fff" stroke="#6b4f2a"/>')
def sofa(x,y,zone):  # L-sofa set: 5 seats around a coffee table
    seats[zone]+=5
    out.append(f'<path d="M {OX+x*S} {OY+y*S} h {3*S} v {0.7*S} h {-2.3*S} v {1.6*S} h {-0.7*S} Z" fill="#9fb8d9" stroke="#4a6688"/>')
    out.append(f'<rect x="{OX+(x+1.1)*S}" y="{OY+(y+1.1)*S}" width="{1.2*S}" height="{0.8*S}" fill="#c9a26b" stroke="#6b4f2a"/>')
def stool(x,y,zone): seats[zone]+=1; out.append(f'<circle cx="{OX+x*S}" cy="{OY+y*S}" r="{0.25*S}" fill="#fff" stroke="#6b4f2a"/>')
def tree(x,y,rad=0.9): out.append(f'<circle cx="{OX+x*S}" cy="{OY+y*S}" r="{rad*S}" fill="#7cbf6b" stroke="#3d7a2f" opacity="0.85"/>')

r(0,0,W,H,"#e8f3df",stroke="#000",sw=3)
out.append(f'<rect x="{OX-20}" y="{OY+H*S+4}" width="{W*S+40}" height="{2.4*S}" fill="#888"/>')
t(W/2,H+1.8,"MAIN ROAD (frontage 42 m)",12,c="#fff",b=True)

# ---------- PARKING  y 23.5-39.5  (solar carport roof over stalls)
r(0,23.5,W,16,"#d9d9d9",stroke="#555")
t(W/2,32.9,"DRIVE AISLE 6 m · two-way · solar-panel carport roofs over all stalls",11.5,b=True)
n=[0]
def stall(x,y,w=2.5,acc=False):
    n[0]+=1; r(x,y,w,5,"#cfe3ff" if acc else "#f4f4f4",stroke="#555",sw=1); t(x+w/2,y+2.9,("♿" if acc else "")+f"P{n[0]}",9.5)
for i in range(6): stall(i*2.5,23.5)
stall(21,23.5,3.6,True)
for i in range(5): stall(24.6+i*2.5,23.5)
for i in range(13): stall(4.5+i*2.5,34.5)
r(0,34.5,4.5,5,"#bdbdbd","IN",stroke="#555",fs=12)
r(37.5,34.5,4.5,5,"#bdbdbd","OUT",stroke="#555",fs=12)
r(37.1,23.5,4.9,5,"#f1d9a8","LOADING",stroke="#a07c2c",fs=9.5,sub="deliveries")
r(15,23.5,2,5,"#d9d9d9",stroke="#555",sw=1); t(16,26.4,"bikes ↑",8.5,rot=-90)
r(17,21,4,7.5,"#f6e7c1",stroke="#a07c2c",dash="4 3"); t(19,25.4,"Walkway &amp;",9); t(19,26.4,"drop-off",9)
# 2-wheeler bay + hedge band y 21-23.5
r(0,21,17,2.5,"#cfcfcf","",stroke="#777")
for i in range(20): out.append(f'<rect x="{OX+(0.3+i*0.83)*S}" y="{OY+21.4*S}" width="{0.3*S}" height="{1.7*S}" fill="#666"/>')
out.append(f'<rect x="{OX+5*S}" y="{OY+21.75*S}" width="{7*S}" height="{1*S}" fill="#555" rx="3"/>'); t(8.5,22.55,"2-WHEELERS ~20",9,c="#fff",b=True)
r(21,21,16.1,2.5,"#5a9e4b",stroke="none")
for x in [23,26.5,30,33.5]: tree(x,22.25,0.9)
t(29,23.3,"tree + hedge buffer",8.5,c="#fff")

# ---------- CAFE ZONE y 0-21
# members garden lounge (back, quietest)
r(0,0,20,9,"#fff6b8","MEMBERS CAFÉ GARDEN LOUNGE · 35 seats","sofas · swings · round tables · counter stools",fs=12,ly=8.0)
sofa(1,0.8,"lounge"); sofa(5.2,0.8,"lounge"); sofa(9.4,0.8,"lounge")
for cx in [2.5,6.5,10.5,14.5]: tab(cx,4.6,4,True,"lounge")
# creative lawn
r(20,0,10,9,"#cfe8c4","CREATIVE LAWN","workshops · music · movie nights",fs=11.5,ly=7.6)
tree(22.5,2.2,1.3); tree(27.5,2.6,1.1)
# garden buffer + smoking
r(30,0,7,6,"#cfe8c4",stroke="#888"); tree(33.5,3,1.5); t(33.5,5.6,"garden buffer",9)
r(37,0,5,6,"#e0e0e0","SMOKING","open-air",stroke="#555",fs=10.5)
r(30,6,7,3,"#cfe8c4",stroke="#888"); t(33.5,7.9,"rainwater pit · compost",8.5)
# members dining
r(0,9,13,12,"#fde9c9","MEMBERS DINING","40 seats · indoor AC",fs=13,ly=19.3)
for cx in [2.2,5.6,9.0]:
    for cy in [10.6,13.6,16.6]: tab(cx,cy,4,False,"dining")
tab(11.6,13.6,4,False,"dining")
# green walk (members route from plaza to lounge)
r(13,9,2,7,"#e8f3df",stroke="#888",dash="4 3"); t(14.1,12.6,"members' green walk ↑",8.5,rot=-90)
# kitchen block with café bar on north face
r(15,9,12,1.6,"#c7a27c","CAFÉ BAR + CARD TOP-UP",fs=10)
for i in range(4): stool(17.5+i*2.3,8.55,"lounge")
r(15,10.6,12,5.4,"#e6e6e6","KITCHEN","~65 m² · passes to all 3 zones",fs=12)
t(15.3,13.4,"◀",10,a="start"); t(26.7,14.8,"▶",10,a="end")
r(27,9,10,4,"#d4d4c4","BACK OF HOUSE","store · cold room · dishwash",fs=10.5)
r(37,6,5,17.5,"#efefe6",stroke="#888",dash="4 3"); t(39.6,13.5,"service lane → loading bay",9.5,rot=-90)
# entry plaza + toilets
r(13,16,8,5,"#f6e7c1","ENTRY PLAZA · card tap","",fs=10.5,ly=16.9)
out.append(f'<rect x="{OX+15.6*S}" y="{OY+17.6*S}" width="{2.6*S}" height="{0.9*S}" fill="#8b5e34"/>'); t(16.9,19.2,"reception",8.5)
t(13.3,20.6,"↖ members",8.5,a="start"); t(20.8,20.6,"non-members →",8.5,a="end")
r(21,16,6,5,"#dbe7f5","TOILETS","M · W · ♿ · baby",fs=11)
# non-members
r(27,13,10,8,"#ffd6d6","NON-MEMBERS · 25 seats","own door from front porch",fs=11,ly=13.9)
for cx in [29,32,35]: tab(cx,16.0,4,False,"nm")
for cx in [29,32]: tab(cx,19.2,4,False,"nm")
tab(35,19.2,3,False,"nm")
tab(36.0,17.6,2,False,"nm")

# legend & stats
lx=OX+W*S+30; ly=OY+80
out.append(f'<g transform="translate({lx+10},{OY+10})"><path d="M0 30 L10 0 L20 30 L10 22 Z" fill="#333"/><text x="10" y="45" font-size="12" text-anchor="middle">N (rear)</text></g>')
L=[("Members dining","#fde9c9"),("Members café lounge","#fff6b8"),("Non-member dine-in","#ffd6d6"),("Kitchen","#e6e6e6"),("Back of house","#d4d4c4"),("Toilets","#dbe7f5"),("Smoking","#e0e0e0"),("Garden / lawn","#cfe8c4"),("Parking","#d9d9d9")]
for i,(k,c) in enumerate(L):
    out.append(f'<rect x="{lx}" y="{ly+i*21}" width="16" height="14" fill="{c}" stroke="#333"/><text x="{lx+22}" y="{ly+i*21+12}" font-size="12">{k}</text>')
tot=seats["dining"]+seats["lounge"]+seats["nm"]
summ=[f"SEATS: {seats['dining']} dining + {seats['lounge']} lounge",f"  + {seats['nm']} non-members = {tot}",f"CARS: {n[0]} (1 accessible)","+ ~20 two-wheelers","+ loading bay","Plot 42 × 39.5 m","= 1,659 m² ≈ 1,984 sq yd","Stall 2.5×5 m · aisle 6 m"]
for i,s in enumerate(summ):
    out.append(f'<text x="{lx}" y="{ly+205+i*18}" font-size="12"{" font-weight=\"700\"" if i<3 else ""}>{s}</text>')
out.append(f'<line x1="{OX}" y1="{OY-22}" x2="{OX+10*S}" y2="{OY-22}" stroke="#000" stroke-width="3"/>')
t(0,-1.7,"0",10,a="start"); t(10,-1.7,"10 m",10,a="end")
t(W/2,-2.9,"DRAFT SITE PLAN v2 — 42 m × 39.5 m (≈1,984 sq yd) · concept only, not for construction",13,b=True)
CW=OX+W*S+260; CH=OY+H*S+60
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}" font-family="Arial, Helvetica, sans-serif"><rect width="100%" height="100%" fill="#fff"/>'+"".join(out)+'</svg>'
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"site-plan.svg"),"w").write(svg)
print(seats,tot,"cars",n[0])
