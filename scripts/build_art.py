from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random, os
OUT=os.path.join(os.path.dirname(__file__),'..','assets')
random.seed(27)
W,H=960,340
F='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
B='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
font=lambda n,b=False:ImageFont.truetype(B if b else F,n)
small,font13,font16,font22,font50=font(11),font(13),font(16),font(22),font(50,True)
frames=[]
streams=[(random.randint(0,960),random.randint(-280,320),random.uniform(2,9),random.randint(5,17)) for i in range(105)]
for t in range(60):
 im=Image.new('RGB',(W,H),(4,10,8));d=ImageDraw.Draw(im)
 # rails and noise
 for y in range(0,H,4): d.line((0,y,W,y),fill=(6,15,11),width=1)
 for i in range(10):
  x=18+i*100; d.line((x,0,x,H),fill=(8,22,16))
 # code rain soft left and right, fade behind hero
 for i,(x,y0,s,l) in enumerate(streams):
  y=(y0+t*s)%(H+300)-150
  for j in range(l):
   yy=int(y-j*14)
   if 16<yy<H-15:
    strength=max(0,1-j/l)
    if 230<x<780: strength*=0.18
    c=(int(12*strength),int(68*strength+12),int(27*strength+8))
    d.text((x,yy),random.choice('01ABCDEF/:|'),font=small,fill=c)
 # outlines
 green=(88,238,143);dim=(30,101,65)
 d.line((34,30,310,30),fill=dim,width=2);d.line((650,30,926,30),fill=dim,width=2)
 d.text((37,13),'SIGNAL / 001',font=font13,fill=(89,171,119))
 d.text((783,13),'github://danishirfan21',font=small,fill=(85,147,102))
 d.line((34,52,34,288),fill=dim,width=2);d.line((926,52,926,288),fill=dim,width=2)
 d.line((34,308,926,308),fill=dim,width=2)
 # small ring reactor
 cx,cy=480,80
 for rad in (25,18):
  d.arc((cx-rad,cy-rad,cx+rad,cy+rad),start=(t*5)%360,end=(t*5+250)%360,fill=green,width=2)
 d.ellipse((cx-4,cy-4,cx+4,cy+4),fill=green)
 # title types in over opening 2 sec
 name='DANISH IRFAN'
 chars=min(len(name),max(0,int((t-4)*0.9)))
 show=name[:chars]
 if t>=22:show=name
 bb=d.textbbox((0,0),show,font=font50)
 tw=bb[2]-bb[0]
 d.text(((W-tw)/2,121),show,font=font50,fill=(195,255,210))
 if t<22 and t%8<6:
  d.rectangle(((W+tw)/2+5,128,(W+tw)/2+17,172),fill=green)
 # supporting labels fade-in
 if t>=20:
  sub='SOFTWARE ENGINEER  /  SYSTEMS BUILDER'
  sb=d.textbbox((0,0),sub,font=font16);sw=sb[2]
  d.text(((W-sw)/2,206),sub,font=font16,fill=(100,193,132))
 if t>=28:
  caption='BUILD  //  AUTOMATE  //  EXPLORE'
  sb=d.textbbox((0,0),caption,font=font13)
  d.text(((W-sb[2])/2,256),caption,font=font13,fill=(145,194,158))
 # lower signals and ticks
 d.text((42,316),'NO STATIC RESUME. JUST A SIGNAL.',font=small,fill=(75,145,97))
 d.text((825,316),f'FRAME {t:02d} / 60',font=small,fill=(75,145,97))
 for i in range(15):
  x=752+i*10
  h=4+int(10*abs(math.sin(t*.12+i*.7)))
  d.rectangle((x,301-h,x+5,301),fill=(35,140+int(60*abs(math.sin(i+t*.05))),71))
 frames.append(im)
frames[0].save(os.path.join(OUT,'signal.gif'),save_all=True,append_images=frames[1:],duration=105,loop=0,optimize=True,disposal=2)
frames[49].save(os.path.join(OUT,'preview.png'))
# graphical menu cards via svg, clickable through markdown html anchors
for ident,title,subtitle,icon in [('identity','WHO AM I?','THE PERSON BEHIND THE SIGNAL','01'),('activity','READ THE SIGNAL','LIVE ENGINEERING TELEMETRY','02'),('repositories','ENTER THE ARCHIVE','THE CODE SPEAKS FOR ITSELF','03')]:
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="118" viewBox="0 0 960 118"><rect width="960" height="118" rx="6" fill="#07110d"/><rect x="1" y="1" width="958" height="116" rx="6" fill="none" stroke="#245f3a"/><path d="M24 22v74M24 22h21M24 96h21" fill="none" stroke="#52da7d" stroke-width="2"/><text x="63" y="50" font-family="monospace" font-size="15" fill="#5ba574" letter-spacing="3">{icon} / SELECT DESTINATION</text><text x="63" y="82" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="30" fill="#d0ffe0">{title}</text><text x="925" y="53" text-anchor="end" font-family="monospace" font-size="14" fill="#6c9c7b">{subtitle}</text><path d="M878 78h42m-16 -12 16 12-16 12" stroke="#6afe9a" stroke-width="3" fill="none"/></svg>'''
 open(os.path.join(OUT,f'{ident}.svg'),'w').write(svg)
print('created',os.path.getsize(os.path.join(OUT,'signal.gif')))
