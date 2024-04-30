import pygame
import pygame.mouse
import math
import time
import random

def Nangle(x):
    return ((x+180) % 360) - 180

def zto(x):
    h = round(x,3)
    n = 0
    if x > 1:
        n += 1
        h = 0
    elif x < 0:
        n += 1
        h = 1
    return round(h,3),n

def pon(nb):
    sn = 1
    if nb > 0:
        sn = 1
    elif nb < 0:
        sn = -1
    return sn

def raycast(map_data, position, angle_degrees, step_size=0.1, offset_x=0.5, offset_y=0.5, pt=False):
    angle_radians = math.radians(angle_degrees)
    x, y = position[1] + offset_x, position[0] + offset_y
    distance = 0
    path = []
    bb = -1
    mpi = 0
    pvs = []
    map_y, map_x = position
    
    while True:
        pvs = [map_y,map_x]
        x_next = x + step_size * math.cos(angle_radians)
        y_next = y + step_size * math.sin(angle_radians)
        map_x = int(x_next)
        map_y = int(y_next)
        
        distance += 0.1
        if distance > 50:
            path.append(map_data[mpi][map_y][map_x])
            break

        
        bx = math.tan(math.radians(1)) * distance / 2
        for e in range(len(Entities)):
            ex, ey = Entities[e]["p"]
            if bb == -1 and abs(x_next - ex - offset_x) < bx and abs(y_next - ey - offset_y) < bx:
                if e == 0:
                    if distance > 1:
                        bb = [e,distance]
                else:
                    bb = [e,distance]

        if (map_x < 0
            or map_x >= len(map_data[mpi][0])
            or map_y < 0
            or map_y >= len(map_data[mpi])):
            break
        
        if (
            map_x < 0
            or map_x >= len(map_data[mpi][0])
            or map_y < 0
            or map_y >= len(map_data[mpi])
            or map_data[mpi][map_y][map_x] in [1]
        ):
            path.append(map_data[mpi][map_y][map_x])
            break

        if (
            map_x < 0
            or map_x >= len(map_data[mpi][0])
            or map_y < 0
            or map_y >= len(map_data[mpi])
            or map_data[mpi][map_y][map_x] in [3,4,2]
        ):
            if (x_next - int(x_next) < 0.1 or x_next - int(x_next) > 0.9) and (y_next - int(y_next) < 0.1 or y_next - int(y_next) > 0.9):
                path.append(map_data[mpi][map_y][map_x])
                break

        if pt:
            if (
                map_x < 0
                or map_x >= len(map_data[mpi][0])
                or map_y < 0
                or map_y >= len(map_data[mpi])
                or map_data[mpi][map_y][map_x] == 2
            ):
                y_next,x_next = (y_next-int(y_next)+1),(x_next-int(x_next)+1)
                mpi += 1
            if (
                map_x < 0
                or map_x >= len(map_data[mpi][0])
                or map_y < 0
                or map_y >= len(map_data[mpi])
                or map_data[mpi][map_y][map_x] == 3
            ):
                y_next,x_next = (y_next-int(y_next)+tp2[0]),(x_next-int(x_next)+tp2[1])
                
                DY1 = p2[0] - tp2[0] 
                DX1 = p2[1] - tp2[1]
                DY2 = p1[0] - tp1[0]
                DX2 = p1[1] - tp1[1]
                if [DY2,DX2,DY1,DX1] in [[0, -1, 1, 0],[1, 0, 0, 1],[0, 1, -1, 0],[-1, 0, 0, -1]]:
                    calc = 1
                    if [DY2,DX2,DY1,DX1] in [[0,-1,1,0],[0,1,-1,0]]:
                        x_next, y_next = int(x_next) + (y_next-int(y_next)),int(y_next) + (x_next-int(x_next))
                    else:
                        x_next, y_next = int(x_next) + 1 - (y_next-int(y_next)),int(y_next) + 1 - (x_next-int(x_next))
                elif [DY2,DX2,DY1,DX1] in [[1, 0, 0, -1],[0, -1, -1, 0],[-1, 0, 0, 1],[0, 1, 1, 0]]:
                    calc = -1
                    if [DY2,DX2,DY1,DX1] in [[1,0,0,-1],[-1,0,0,1]]:
                        x_next, y_next = int(x_next) + (y_next-int(y_next)),int(y_next) + (x_next-int(x_next))
                    else:
                        x_next, y_next = int(x_next) + 1 - (y_next-int(y_next)),int(y_next) + 1 - (x_next-int(x_next))
                elif [DY2,DX2,DY1,DX1] in [[0, 1, 0, 1],[1, 0, 1, 0],[0, -1, 0, -1],[-1, 0, -1, 0]]:
                    calc = 2
                    x_next, y_next = int(x_next) + 1 - (x_next-int(x_next)),int(y_next) + 1 - (y_next-int(y_next))
                else:
                    calc = 0

                angle_degrees += calc * 90
                angle_radians = math.radians(angle_degrees)
            if (
                map_x < 0
                or map_x >= len(map_data[mpi][0])
                or map_y < 0
                or map_y >= len(map_data[mpi])
                or map_data[mpi][map_y][map_x] == 4
            ):
                y_next,x_next = (y_next-int(y_next)+tp1[0]),(x_next-int(x_next)+tp1[1])
                DY1 = p2[0] - tp2[0] 
                DX1 = p2[1] - tp2[1]
                DY2 = p1[0] - tp1[0]
                DX2 = p1[1] - tp1[1]
                if [DY1,DX1,DY2,DX2] in [[0, -1, 1, 0],[1, 0, 0, 1],[0, 1, -1, 0],[-1, 0, 0, -1]]:
                    calc = 1
                    if [DY1,DX1,DY2,DX2] in [[0,-1,1,0],[0,1,-1,0]]:
                        x_next, y_next = int(x_next) + (y_next-int(y_next)),int(y_next) + (x_next-int(x_next))
                    else:
                        x_next, y_next = int(x_next) + 1 - (y_next-int(y_next)),int(y_next) + 1 - (x_next-int(x_next))
                elif [DY1,DX1,DY2,DX2] in [[1, 0, 0, -1],[0, -1, -1, 0],[-1, 0, 0, 1],[0, 1, 1, 0]]:
                    calc = -1
                    if [DY1,DX1,DY2,DX2] in [[1,0,0,-1],[-1,0,0,1]]:
                        x_next, y_next = int(x_next) + (y_next-int(y_next)),int(y_next) + (x_next-int(x_next))
                    else:
                        x_next, y_next = int(x_next) + 1 - (y_next-int(y_next)),int(y_next) + 1 - (x_next-int(x_next))
                elif [DY1,DX1,DY2,DX2] in [[0, 1, 0, 1],[1, 0, 1, 0],[0, -1, 0, -1],[-1, 0, -1, 0]]:
                    calc = 2
                    x_next, y_next = int(x_next) + 1 - (x_next-int(x_next)),int(y_next) + 1 - (y_next-int(y_next))
                else:
                    calc = 0
                angle_degrees += calc * 90
                angle_radians = math.radians(angle_degrees)

        x, y = x_next, y_next
        path.append(map_data[mpi][map_y][map_x])            
        
    return [map_y,map_x,y_next-int(y_next),x_next-int(x_next)], pvs, path[-1], round(distance, 3), bb

def display(src,ent,fm=24,fi=0):
    cell_width = screen_width // len(src[0])
    cell_height = screen_height // len(src)

##    screen.fill((50,56,128))
##    ceiling_height = screen_height // 4
##    pygame.draw.rect(screen, (77, 81, 130), (0, 0, screen_width, ceiling_height))
    BG = pygame.transform.scale(pygame.image.load("bg.png"), (screen_width, screen_height))
    screen.blit(BG, (0,0))
    
    for y, row in enumerate(src):
        for x, color_index in enumerate(row):
            if color_index != 0:
                #print(color_index)
                if color_index not in [1,2,3,4]:
                    color = color_index    
                else:
                    color = colors[color_index]
                pygame.draw.rect(screen, color, (x * cell_width, y * cell_height, cell_width, cell_height))

    for BB in range(len(ent)):
        if ent[BB] != -1:
            e = Entities[ent[BB][0]]
            dst = 400/ent[BB][1]
            lw = e["s"][0]/50 * dst
            lh = e["s"][1]/50 * dst
            pygame.draw.rect(screen, (255, 255, 255), (int(BB*cell_width-lw/2), int(screen_height//4 - lw/2), lw, lh))
            ##tt = pygame.transform.scale(e["t"], (lw, lh))
            ##screen.blit(tt, (BB*cell_width-lh/2,screen_height//4))
            
    XG = [abs(i)-100 for i in range(-200,200,5)]
    YG = [abs(i)-50 for i in range(-100,100,5)]
    xm = fm % len(XG)
    gx = XG[xm]
    ym = fm % len(YG)
    gy = 50-YG[ym]

    sheet = pygame.image.load("GunA.png")
    fi = int(fi % 5)
    frame_x = fi * 184
    frame = sheet.subsurface(pygame.Rect(frame_x, 0, 184, 323))

    gun_image = pygame.transform.scale(frame, (screen_width*184/800, screen_height*323/600))
    screen.blit(gun_image, (gx + screen_width* 3/8,gy + screen_height* 3/6))

    aim = pygame.transform.scale(pygame.image.load("shoot.png"), (screen_width, screen_height))
    screen.blit(aim, (0,-30))

    text = font.render((str(txt)) , True, (55,55,55))
    textRect = text.get_rect()
    screen.blit(text, textRect)
    
    pygame.display.flip()

def Image(src):
    w, h = 100, 30
    out = [["0" for _ in range(w)]for _ in range(h)]
    max_wall_height = 10
    walltxt = pygame.image.load("Tile1.png")

    for a in range(h):
        for b in range(w):
            if 7 + (src[b][0] // 2) >= a >= 7 - (src[b][0] // 2 + (src[b][0] % 2 > 0)):
                wall_height = src[b][0]
                normalized_height = int((wall_height / max_wall_height) * h)
                if a >= 7 - (normalized_height // 2) and a <= 7 + (normalized_height // 2):
                    if int(src[b][1]) != 0:
                        distance = 40*20/float(src[b][0])
                        if int(src[b][1]) == 1:
                            index = int(src[b][2] * 10)
                            ht = (7 + (src[b][0] // 2)) - (7 - (src[b][0] // 2 + (src[b][0] % 2 > 0)))
                            ha = a - (7 - (src[b][0] // 2 + (src[b][0] % 2 > 0)))
                            clc = int((ha/ht)*10)
                            #print(index,clc)
                            out[a][b] = walltxt.get_at((index,clc))
                            out[a][b] = (max(int(out[a][b][0] - distance),20),max(int(out[a][b][1]-distance),20),max(int(out[a][b][2]-distance),20),55)

                        elif int(src[b][1]) == 2:
                            out[a][b] = 1
                        elif int(src[b][1]) == 3:
                            out[a][b] = 2
                        elif int(src[b][1]) == 4:
                            out[a][b] = 3
                        else:
                            out[a][b] = 0
                    else:
                        out[a][b] = 0
                else:
                    out[a][b]= 0
            else:
                out[a][b]= 0
    return out

def frame(fc, fv, p, Mp, ofx, ofy):
    screen = []
    bills = []
    ets = []
    
    fx = ofx
    fy = ofy
    
    st = time.time()
    map_height = len(Mp)
    map_width = len(Mp[0])
    for i in range(int(fc - fv), int(fc + fv + 1)):
        ps,pv,l,d,bl= raycast(Mp, p, i, 0.1, fx, fy,True)
        if bl != -1:
            if bl[0] not in ets:
                bills.append(bl)
                #ets.append(bl[0])
        else:
            bills.append(bl)
        ht =  str(l)[-1]
        dex = 0.1
        if ps[0] - pv[0] != 0:
            dex = round(ps[3],1)
        else:
            dex = round(ps[2],1)
        screen.append([20/d, int(ht), dex])
    #print(len(screen))
    display(Image(screen),bills,sw,frame_index)
    et = time.time()
    return et - st

def generate_maze(width, height):
    maze = [[1] * (2 * width + 1) for _ in range(2 * height + 1)]

    def is_valid(x, y):
        return 0 < x < 2 * width and 0 < y < 2 * height and maze[y][x] == 1

    def connect_cells(x1, y1, x2, y2):
        maze[y1][x1] = 0
        maze[y2][x2] = 0
        maze[y1 + (y2 - y1) // 2][x1 + (x2 - x1) // 2] = 0


    for y in range(2 * height + 1):
        for x in range(2 * width + 1):
            if y % 2 == 0 or x % 2 == 0:
                maze[y][x] = 1


    stack = [(1, 1)]

    while stack:
        x, y = stack[-1]
        maze[y][x] = 0

        neighbors = [(x + dx, y + dy) for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]]
        unvisited_neighbors = [neighbor for neighbor in neighbors if is_valid(*neighbor)]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            connect_cells(x, y, nx, ny)
            stack.append((nx, ny))
        else:
            stack.pop()

    maze[2 * height][2 * width-1] = 2

    return maze

def print_maze(maze,P):
    mp = ""
    for y in range(len(maze)-1,-1,-1):
        for x in range(len(maze[0])):
            if [y,x] == P:
                mp += "X "
            elif maze[y][x] == 1:
                mp += "# "
            elif maze[y][x] == 2:
                mp += "! "
            else:
                mp += ". "
        mp += "\n"
    print(mp)

screen_width = 800
screen_height = 600

pygame.init()
font = pygame.font.Font('pixelart.ttf', 32)
font_size = 24

pygame.display.set_caption("SYED-engine")
fps = 60
clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((screen_width, screen_height))
full = False

colors = [
    (45, 45, 45),    
    (0, 255, 155),
    (15, 199, 255),
    (255, 135, 15),
    (33, 31, 52),
    (63, 63, 116),
    (202, 219, 251),
    (255, 255, 255),
]

lvl = 3
map = [[[1,1,1,1,1],
       [1,0,0,0,1],
       [3,0,0,0,4],
       [1,0,0,0,1],
       [1,1,2,1,1]]]

map.append(generate_maze(lvl,lvl))
map.append(generate_maze(lvl+1,lvl+1))

trn = 4
fov = 60
sw = 12

stp = 0.05
bx = 0.2
txt = ""

wall = [1]

pygame.mouse.set_visible(False) 
center_x = screen_width // 2
center_y = screen_height // 2

pygame.mouse.set_pos(center_x, center_y)

Entities = []
##Entities.append({
##    "p" : [1.5,1.5],
##    "s" : [50,80],
##    "t" : (80,80,80)
##    })
##Entities.append({
##    "p" : [3.5,3.5],
##    "s" : [64,64],
##    "t" : pygame.image.load("enemy.png")
##    })

ang = 90
k = [1,1]
mx, my = 0.5, 0.5

p1 = [2,0]
p2 = [2,4]
tp1 = [2,1]
tp2 = [2,3]

Shoot = True
frame_index = 0
timer = 0

while running:
    txt = "LVL: " + str(lvl-3) + " (X: " + str(k[1]) + " Y: " + str(k[0]) + ")" + " Time: " + str(round(timer,2))
    if map[0][k[0]][k[1]] == 2:
        k = [1,1]
        p1 = [0,0]
        p2 = [0,0]
        tp1 = [1,1]
        tp2 = [1,1]
        lvl += 1
        map.pop(0)
        map.append(generate_maze(lvl+1,lvl+1))
        
    if map[0][k[0]][k[1]] == 4:
        k = [tp1[0],tp1[1]]

        DY1 = p2[0] - tp2[0] 
        DX1 = p2[1] - tp2[1]
        DY2 = p1[0] - tp1[0]
        DX2 = p1[1] - tp1[1]
        if [DY1,DX1,DY2,DX2] in [[0, -1, 1, 0],[1, 0, 0, 1],[0, 1, -1, 0],[-1, 0, 0, -1]]:
            calc = 1
            if [DY1,DX1,DY2,DX2] in [[0,-1,1,0],[0,1,-1,0]]:
                mx, my = my, mx
            else:
                mx,my = 1-my,1-mx
        elif [DY1,DX1,DY2,DX2] in [[1, 0, 0, -1],[0, -1, -1, 0],[-1, 0, 0, 1],[0, 1, 1, 0]]:
            calc = -1
            if [DY1,DX1,DY2,DX2] in [[1,0,0,-1],[-1,0,0,1]]:
                mx, my = my, mx
            else:
                mx,my = 1-my,1-mx
        elif [DY1,DX1,DY2,DX2] in [[0, 1, 0, 1],[1, 0, 1, 0],[0, -1, 0, -1],[-1, 0, -1, 0]]:
            calc = 2
            mx, my = 1-mx,1-my
        else:
            calc = 0
            
        ang += calc * 90
        
    
    elif map[0][k[0]][k[1]] == 3:
        k = [tp2[0], tp2[1]]
        
        DY1 = p2[0] - tp2[0] 
        DX1 = p2[1] - tp2[1]
        DY2 = p1[0] - tp1[0]
        DX2 = p1[1] - tp1[1]
        if [DY2,DX2,DY1,DX1] in [[0, -1, 1, 0],[1, 0, 0, 1],[0, 1, -1, 0],[-1, 0, 0, -1]]:
            calc = 1
            if [DY2,DX2,DY1,DX1] in [[0,-1,1,0],[0,1,-1,0]]:
                mx, my = my, mx
            else:
                mx,my = 1-my,1-mx
        elif [DY2,DX2,DY1,DX1] in [[1, 0, 0, -1],[0, -1, -1, 0],[-1, 0, 0, 1],[0, 1, 1, 0]]:
            calc = -1
            if [DY2,DX2,DY1,DX1] in [[1,0,0,-1],[-1,0,0,1]]:
                mx, my = my, mx
            else:
                mx,my = 1-my,1-mx
        elif [DY2,DX2,DY1,DX1] in [[0, 1, 0, 1],[1, 0, 1, 0],[0, -1, 0, -1],[-1, 0, -1, 0]]:
            calc = 2
            mx, my = 1-mx,1-my
        else:
            calc = 0
            
        ang += calc * 90

        
    ang = Nangle(ang)
    #Entities[0]["p"] = [k[0]+my,k[1]+mx]
    face = [ang,round(math.cos(math.radians(ang)), 5),round(math.sin(math.radians(ang)),5)]

    frame(face[0],fov,k,map,mx,my)

    if Shoot != True:
        frame_index += 0.5
        if frame_index % 5 == 0:
            Shoot = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Shoot:
                    crd,tp,hts,_,_= raycast(map, k, ang-5, 0.1, mx, my, False)
                    if hts == 1:
                        if [crd[0]-tp[0],crd[1]-tp[1]].count(0) == 1:
                            tp1 = tp
                            map[0][p1[0]][p1[1]] = 1
                            p1 = crd
                            map[0][p1[0]][p1[1]] = 3
                    Shoot = False
            if event.button == 3:
                if Shoot:
                    crd,tp,hts,_,_= raycast(map, k, ang-5, 0.1, mx, my, False)
                    if hts == 1:
                        if [crd[0]-tp[0],crd[1]-tp[1]].count(0) == 1:
                            tp2 = tp
                            map[0][int(p2[0])][int(p2[1])] = 1
                            p2 = crd
                            map[0][(p2[0])][int(p2[1])] = 4
                    Shoot = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                running = False
            elif event.key == pygame.K_3:
                pause = True
                pygame.mouse.set_visible(True)
                while pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pause = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_4:
                                running = False
                                pause = False
                            elif event.key == pygame.K_3:
                                pause = False
                pygame.mouse.set_visible(False)

    pygame.mouse.set_pos(center_x, center_y)
    MM = pygame.mouse.get_rel()
    if abs(MM[0]) > 0:
        ang += trn/50 * MM[0]
    
    keys = pygame.key.get_pressed()
    nx = k[1] + mx + stp * face[1]
    ny = k[0] + my + stp * face[2]
    mpx = int(nx + bx * pon(face[1]))
    mpy = int(ny + bx * pon(face[2]))
        
    if keys[pygame.K_w]:
        sw += 2
        if (0 <= mpx < len(map[0][0])
            and map[0][k[0]][int(mpx)] not in wall):
            k[1] = int(nx)
            mx = nx - int(nx)
        if (0 <= mpy < len(map[0])
            and map[0][int(mpy)][k[1]] not in wall):
            k[0] = int(ny)
            my = ny - int(ny)
            
    if keys[pygame.K_a]:
        left_angle = Nangle(ang - 90)
        left_face = [left_angle, round(math.cos(math.radians(left_angle)), 5), round(math.sin(math.radians(left_angle)), 5)]
        nx_left = k[1] + mx + stp * left_face[1]
        ny_left = k[0] + my + stp * left_face[2]
        mpx_left = int(nx_left + bx * pon(left_face[1]))
        mpy_left = int(ny_left + bx * pon(left_face[2]))

        if (
            0 <= mpx_left < len(map[0][0])
            and 0 <= mpy_left < len(map[0])
            and map[0][mpy_left][mpx_left] not in wall
        ):
            k[1] = int(nx_left)
            k[0] = int(ny_left)
            mx = nx_left - int(nx_left)
            my = ny_left - int(ny_left)
            
    if keys[pygame.K_d]:
        right_angle = Nangle(ang + 90)
        right_face = [right_angle, round(math.cos(math.radians(right_angle)), 5), round(math.sin(math.radians(right_angle)), 5)]
        nx_right = k[1] + mx + stp * right_face[1]
        ny_right = k[0] + my + stp * right_face[2]
        mpx_right = int(nx_right + bx * right_face[1])
        mpy_right = int(ny_right + bx * right_face[2])

        if (
            0 <= mpx_right < len(map[0][0])
            and 0 <= mpy_right < len(map[0])
            and map[0][mpy_right][mpx_right] not in wall
        ):
            k[1] = int(nx_right)
            k[0] = int(ny_right)
            mx = nx_right - int(nx_right)
            my = ny_right - int(ny_right)
            
    if keys[pygame.K_s]:
        nx = k[1] + mx + stp *-1* face[1]
        ny = k[0] + my + stp *-1* face[2]
        mpx = int(nx + bx * -1 * pon(face[1]))
        mpy = int(ny + bx * -1 * pon(face[2]))
        if (
            0 <= mpx < len(map[0][0])
            and map[0][k[0]][int(mpx)] not in wall
        ):
            if (
            0 <= mpx < len(map[0][0])
            and 0 <= mpy < len(map[0])
            and map[0][mpy][mpx] not in wall
            ):
                k[1] = int(nx)
                k[0] = int(ny)
                mx = nx - int(nx)
                my = ny - int(ny)

    timer += 1/fps
    clock.tick(fps)

pygame.mouse.set_visible(True)
pygame.quit()
