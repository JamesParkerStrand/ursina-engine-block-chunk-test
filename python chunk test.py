from ursina import *

app = Ursina()


blocks = dict()

xRange = 25

yRange = 25

zRange = 25

#this is initialzing an array storing coordinates like to be able to index the blocks array by a y-axis, then all the x and z coordinates are then just scattered around
for x in range(xRange):
    for z in range(zRange):
        for y in range(yRange):
            blocks.update({(x,y,z) : 1})

# test to see if blocks modify correctly as it should.
#blocks.update({(0,0,0): 0})
#blocks.update({(0,1,0): 0})
#blocks.update({(0,2,0): 0})
#blocks.update({(1,2,0): 0})
#blocks.update({(0,4,0): 0})

def generateVertTOP(x, y, z):
    return [
    Vec3(x, y+1, z),  # Top-left
    Vec3(1+x, y+1, z),   # Top-right
    Vec3(x, y+1, 1+z), # Bottom-left
    Vec3(1+x,y+1,1+z),
    Vec3(x,y+1,1+z),
    Vec3(1+x,y+1,z)
    ]

def generateVertBOTTOM(x, y, z):
    return [
        Vec3(1 + x, y, z),  # Top-right
        Vec3(x, y, z),  # Top-left
        Vec3(x, y, 1 + z),  # Bottom-left
        Vec3(x, y, 1 + z),
        Vec3(1 + x, y, 1 + z),
        Vec3(1 + x, y, z)
    ]

def generateVertFRONT(x, y, z):
    return [
        Vec3(x, y, z),  # Bottom-left front
        Vec3(1 + x, y, z),  # Bottom-right front
        Vec3(x, 1 + y, z),  # Top-left front
        Vec3(1 + x, 1 + y, z),  # Top-right front
        Vec3(x, 1 + y, z),  # Top-left front (duplicate for triangle strip)
        Vec3(1 + x, y, z)  # Bottom-right front (duplicate for triangle strip)
    ]

def generateVertBACK(x, y, z):
    return [
        Vec3(x, y, 1 + z),  # Bottom-left back
        Vec3(x, 1 + y, 1 + z),  # Top-left back
        Vec3(1 + x, y, 1 + z),  # Bottom-right back
        Vec3(1 + x, 1 + y, 1 + z),  # Top-right back
        Vec3(1 + x, y, 1 + z),  # Bottom-right back (duplicate for triangle strip)
        Vec3(x, 1 + y, 1 + z)  # Top-left back (duplicate for triangle strip)
    ]

def generateVertRIGHT(x, y, z):
    return [
        Vec3(1 + x, y, z),      # Bottom-left
        Vec3(1 + x, y, 1 + z),  # Bottom-right
        Vec3(1 + x, 1 + y, z),  # Top-left
        Vec3(1 + x, 1 + y, 1 + z),  # Top-right
        Vec3(1 + x, 1 + y, z),  # Top-left (Duplicate for triangle strip)
        Vec3(1 + x, y, 1 + z)   # Bottom-right (Duplicate for triangle strip)
    ]

def generateVertLEFT(x, y, z):
    return [
        Vec3(x, y, z),      # Bottom-left
        Vec3(x, 1 + y, z),  # Top-left
        Vec3(x, y, 1 + z),  # Bottom-right
        Vec3(x, 1 + y, 1 + z),  # Top-right
        Vec3(x, y, 1 + z),  # Bottom-right (Duplicate for triangle strip)
        Vec3(x, 1 + y, z)  # Top-left (Duplicate for triangle strip)
    ]

def generateUv(x,y):
    return [
    Vec2(x, y),  # Top-left
    Vec2(1+x, y),  # Top-right
    Vec2(x, 1+y),  # Bottom-left
    Vec2(1+x, 1+y),   # Bottom-right
    Vec2(x,1+y),
    Vec2(1+x,y)
    ]

verts = []

uvs = []

mesh = Mesh(vertices=verts, uvs=uvs, mode='triangle')

quad_entity = Entity(
model = mesh,
texture = 'white_cube',
color = color.azure)


def generate():

    for x in range(xRange):
        for z in range(zRange):
            for y in range(yRange):

                current = blocks.get((x, y, z))
                up = blocks.get((x, y + 1, z))
                down = blocks.get((x, y - 1, z))
                forward = blocks.get((x, y, z - 1))
                backward = blocks.get((x, y, z + 1))
                right = blocks.get((x + 1, y, z))
                left = blocks.get((x - 1, y, z))

                if current == 0:
                    continue

                if down == 0 or down == None:
                    verts.extend(generateVertBOTTOM(x, y, z))
                    uvs.extend(generateUv(x, y))

                if up == 0 or up == None:
                    verts.extend(generateVertTOP(x, y, z))
                    uvs.extend(generateUv(x, y))

                if forward == 0 or forward == None:
                    verts.extend(generateVertFRONT(x, y, z))
                    uvs.extend(generateUv(x, y))

                if backward == 0 or backward == None:
                    verts.extend(generateVertBACK(x, y, z))
                    uvs.extend(generateUv(x, y))

                if right == 0 or right == None:
                    verts.extend(generateVertRIGHT(x, y, z))
                    uvs.extend(generateUv(x, y))

                if left == 0 or left == None:
                    verts.extend(generateVertLEFT(x, y, z))
                    uvs.extend(generateUv(x, y))

def deleteTest():
    mesh.generate()

'''
mesh2 = Mesh(vertices=generateVertBACK(1,3,1), uvs=generateUv(0,0), mode='triangle')

# Create the quad entity
quad_entity = Entity(
    model=mesh2,
    texture='white_cube',
    color=color.azure
)
'''

def input(key):
    if key == "g":
        generate()
        mesh.generate()
    if key == "r":
        deleteTest()


EditorCamera()

app.run()