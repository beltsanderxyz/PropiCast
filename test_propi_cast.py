from mcpi.minecraft import Minecraft
from propi_cast import *

STONE=1
TNT=46
LAVA = 10
WATER=8
WATER_STATIONARY = 9
CHEST = 54

nWide = 6
nLong = nWide
nHigh = 4
nBlocks = 0

blockToBuild = STONE

mc = Minecraft.create()
# build_room(mc, nLong, nHigh, nWide, blockToBuild)

nx = 4
ny = 4
nz = 4

pos = mc.player.getPos()
build_room(mc,pos.x,pos.y,pos.z,nx,ny,nz,STONE)
