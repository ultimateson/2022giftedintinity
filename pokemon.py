Web VPython 3.2
images=['https://cdn.econovill.com/news/photo/201603/285365_95988_038.png','https://cdn.banggooso.com/assets/images/game96/result/ESTJ.png']
g=box(pos=vec(1,0,0), texture=images[1])
p=box(texture=images[0])
a=arrow(pos=vec(0,2,0), axis=vec(0,-1,0), color=color.magenta)
i=0
while True:
    rate(10)
    k=keysdown()
    a.pos.x=i%2
    i=i+1
    if i%2==0:
        p.color=color.white
        g.color=color.magenta
    else:
        p.color=color.magenta
        g.color=color.white
    if ' ' in k:
        label(text = '당첨되셨습니다!', pos = vec(0,1.5,0))
        break
