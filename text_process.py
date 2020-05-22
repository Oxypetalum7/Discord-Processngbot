
def writecontent(msg):
    lines = msg
    lines = lines.split('\n')
    lines = lines[1:]
    lines.insert(-1, "  if((frameCount <= 600)&&(frameCount % 15 == 0))saveFrame(\"####.png\");")
    lines.insert(-1, "  if(frameCount > 600) exit();")
    [print(i) for i in lines]
    f = open('sketch/sketch.pde','w',encoding="utf_8")
    f.write('\n'.join(lines))
    f.close()