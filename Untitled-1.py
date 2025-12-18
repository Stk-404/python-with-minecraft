import time
from mcpi.minecraft import Minecraft
from mcpi import block


mc = Minecraft.create()

def build_simple_house(x, y, z, width, length, height):
    #block we will use
    FLOOR_BLOCK = block.WOOD_PLANKS.id
    WALL_BLOCK = block.BRICK_BLOCK.id
    ROOF_BLOCK = block.WOOD_PLANKS.id
    GLASS_BLOCK = block.GLASS.id

# 1) floor
    for dx in range(width):
        for dz in range(length):
            mc.setBlock(x + dx, y, z + dz, FLOOR_BLOCK)
    
# 2) solid outer box ( wall + roof )
    for dx in range(width):
        for dy in range(1, height + 1):
            for dz in range(length):
                mc.setBlock(x + dx, y + dy, z + dz, WALL_BLOCK)

# 3) hollow the inside (air inside the walls)    
    for dx in range(1, width - 1):
        for dy in range(2, height):
            for dz in range(1, length - 1):
                mc.setBlock(x + dx, y + dy, z + dz, block.AIR.id)

# 4) flat roof on top
    roof_y = y + height
    for dx in range(width):
        for dz in range(length):
            mc.setBlock(x + dx, roof_y, z + dz, ROOF_BLOCK)

    door_x = x + width // 2
    door_z = z
    
    mc.setBlock(door_x, y + 1, door_z, block.AIR.id)
    mc.setBlock(door_x, y + 2, door_z, block.AIR.id)
    mc.setBlock(door_x, y + 3, door_z, block.AIR.id)

    window_y = y + height // 2

    for dz in range(2, length - 2):
        mc.setBlock(x, window_y, z + dz, GLASS_BLOCK)
    
    for dz in range(2, length - 2):
        mc.setBlock(x + width - 1, window_y, z + dz, GLASS_BLOCK)

x, y ,z = mc.player.getTilePos()
build_simple_house(x + 2, y, z, width=12, length=15, height=23)