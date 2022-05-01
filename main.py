from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.1, exposure=1)
scene.set_floor(-63, (1.0,1.0,1.0))
scene.set_background_color((0.01, 0.01, 0.05)) # 天空颜色
scene.set_directional_light((1, 1, -1), 0.2, (0.8, 0.8, 1))

@ti.func
def create_revolute(pos, length, radii, color, dir):
    for i in range(length):
        radius = radii[0] + i / length * (radii[1] - radii[0])
        for j, k in ti.ndrange((-radius, radius), (-radius, radius)):
            if (j * j + k * k < radius * radius):
                if dir == 1:    scene.set_voxel(pos + vec3(i,j,k), 2, color)
                elif dir == 2:  scene.set_voxel(pos + vec3(j,i,k), 2, color)
                else:   scene.set_voxel(pos + vec3(j,k,i), 1, color)

@ti.func
def create_box(pos,size,color):
    for i, j, k in ti.ndrange((0,size[0]),(0,size[1]),(0,size[2])):
        scene.set_voxel(pos + vec3(i,j,k),2,color)

@ti.kernel
def initialize_voxels():

    # mast
    create_box(vec3(-55, -62, -18), vec3(1, 124, 1), vec3(0.3, 0.3, 0.3))
    create_box(vec3(54, -62, -18), vec3(1, 124, 1), vec3(0.3, 0.3, 0.3))
    create_box(vec3(-62, 8, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(-62, -9, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(47, 8, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(47, -9, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(-62, 61, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(-62, -62, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(47, 61, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(47, -62, -18), vec3(15, 1, 1), vec3(1,1,0.2))
    create_box(vec3(-6, -29, -18), vec3(3, 1, 1), vec3(0.3, 0.3, 0.3))
    create_box(vec3(4, -29, -18), vec3(3, 1, 1), vec3(0.3, 0.3, 0.3))
    create_box(vec3(-30, 0, 0), vec3(60, 1, 1), vec3(0.3,0.3,0.3))
    create_box(vec3(-30, 0, -4), vec3(1, 1, 9), vec3(1,1,0.2))
    create_box(vec3(30, 0, -4), vec3(1, 1, 9), vec3(1,1,0.2))
    create_box(vec3(-10, 0, -4), vec3(1, 1, 9), vec3(1,1,0.2))
    create_box(vec3(10, 0, -4), vec3(1, 1, 9), vec3(1,1,0.2))

    # solar array
    create_box(vec3(-62, 10, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(-53, 10, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(-53, 10, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(-62, -60, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(-53, -60, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(56, 10, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(47, 10, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(56, -60, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(47, -60, -18), vec3(6, 50, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(-28, 0, -4), vec3(17, 1, 3), vec3(0.2, 0.2, 1))
    create_box(vec3(-28, 0, 2), vec3(17, 1, 3), vec3(0.2, 0.2, 1))
    create_box(vec3(12, 0, -4), vec3(17, 1, 3), vec3(0.2, 0.2, 1))
    create_box(vec3(12, 0, 2), vec3(17, 1, 3), vec3(0.2, 0.2, 1))
    create_box(vec3(-23, -32, -18), vec3(17, 7, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(7, -32, -18), vec3(17, 7, 1), vec3(0.2, 0.2, 1))
    create_box(vec3(-14, 0, 54), vec3(29, 1, 5), vec3(0.2, 0.2, 1))
    create_box(vec3(-14, 0, -58), vec3(29, 1, 5), vec3(0.2, 0.2, 1))

    # section
    create_revolute(vec3(-52, 0, -18),18,vec2(5,8),vec3(0.8,0.8,0.8),1)
    create_revolute(vec3(-34, 0, -18),25,vec2(8,8),vec3(0.5, 0.5, 0.5),1)
    create_revolute(vec3(-9, 0, -18),5,vec2(8,4),vec3(0.8,0.8,0.8),1)
    create_revolute(vec3(-9, 0, -18),5,vec2(8,4),vec3(0.8,0.8,0.8),1)
    create_revolute(vec3(-4, 0, -18),4,vec2(2,5),vec3(0.3, 0.3, 0.5),1)
    create_revolute(vec3(0, 0, -18),4,vec2(5,2),vec3(0.3, 0.3, 0.5),1)
    create_revolute(vec3(4, 0, -18),5,vec2(4,8),vec3(0.8, 0.8, 0.8),1)
    create_revolute(vec3(9, 0, -18),13,vec2(8,8),vec3(0.5, 0.5, 0.5),1)
    create_box(vec3(22, -6, -24), vec3(12, 12, 12), vec3(0.2, 0.2, 0.3))
    create_revolute(vec3(34, 0, -18),18,vec2(8,5),vec3(0.8,0.8,0.8),1)
    create_revolute(vec3(0, 0, -55),16,vec2(4,5),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, -39),6,vec2(4,2),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, -34),6,vec2(2,4),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, -29),6,vec2(4,4),vec3(0.5,0.5,0.5),3)
    create_revolute(vec3(0, 0, -23),5,vec2(4,2),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, -13),5,vec2(2,4),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, -8),12,vec2(4,4),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, 4),25,vec2(6,6),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, 29),5,vec2(6,4),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, 0, 34),5,vec2(3,5),vec3(0.5,0.5,0.5),3)
    create_revolute(vec3(0, 0, 39),5,vec2(5,5),vec3(0.5,0.5,0.5),3)
    create_revolute(vec3(0, 0, 44),5,vec2(5,3),vec3(0.5,0.5,0.5),3)
    create_revolute(vec3(0, 0, 49),12,vec2(4,4),vec3(0.8,0.8,0.8),3)
    create_revolute(vec3(0, -36, -18),16,vec2(5,5),vec3(0.8,0.8,0.8),2)
    create_revolute(vec3(0, -20, -18),4,vec2(5,3),vec3(0.8,0.8,0.8),2)
    create_revolute(vec3(0, -16, -18),4,vec2(3,5),vec3(0.8,0.8,0.8),2)
    create_revolute(vec3(0, -12, -18),8,vec2(5,5),vec3(0.8,0.8,0.8),2)
    create_revolute(vec3(0, -4, -18),4,vec2(5,3),vec3(0.8,0.8,0.8),2)
initialize_voxels()

scene.finish()