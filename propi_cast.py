#from mcpi.minecraft import Minecraft

# basic geometry section
def build_square(mc,x,y,z,my_length, my_height, my_plane, block_type):
    # builds a square, mostly used to create walls for other rooms
    if my_plane == 'xy':
        mc.setBlocks(x, y, z, x+my_length, y+my_height, z,           block_type)

    elif my_plane =='yz':
        mc.setBlocks(x, y, z, x,           y+my_height, z+my_length, block_type)

    elif my_plane == 'xz':
        mc.setBlocks(x, y, z, x+my_length, y,           z+my_length, block_type)

    else:
        # throw an exception if the draw plan is unrecognized
        raise Exception('Unrecognized draw plane: ' + my_plane + '. Must be xy, yz, or xz')

def build_circle(mc,cx,cy,cz,my_radius, my_plane, block_type):
    # build a circle with a given radius in a user defined plane
    # totally borrowed this code from a guy on wordpress
    ii = 0
    radii = my_radius

    vec_x = [cx]*8
    vec_y = [cx]*8
    vec_z = [cx]*8

    # left off here, just need to set the size of the plane not being iterated to zero

    while (radii >= ii):
        if my_plane == 'xy':
            ls_x = [a[i]+b[i] for i in range(len(a))]
            lx_y = [a[i]+b[i] for i in range(len(a))]
            ls_z = [a[i]+b[i] for i in range(len(a))]

            
        elif my_plane =='yz':

       
        elif my_plane == 'xz':
            
        mc.setBlock(cs+x,cy+radii,cz,block_type)
        mc.setBlock(cs+x,cy-radii,cz,block_type)
        mc.setBlock(cs-x,cy-radii,cz,block_type)
        mc.setBlock(cs-x,cy+radii,cz,block_type)
        mc.setBlock(cs+radii,cy+x,cz,block_type)
        mc.setBlock(cs-radii,cy+x,cz,block_type)
        mc.setBlock(cs-radii,cy-x,cz,block_type)
        mc.setBlock(cs+radii,cy-x,cz,block_type)

        y=y+1
        radii = int(round(math.sqrt(my_radius**2-ii**2)))
        
        
def build_cylinder(mc,x,y,z,my_radius, my_height, my_plane, block_type):
    # build a cylinder that is circular in a user defined plane
    from math import sqrt

    raise Exception('build_cylinder not yet implemented. need to finish build_circle')

    

    
    else:
        # throw an exception if the draw plan is unrecognized
        raise Exception('Unrecognized draw plane: ' + my_plane + '. Must be xy, yz, or xz')

    mc.setBlocks(x, y, z, x+my_length, y+my_height, z,           block_type)
# more complicated structures
def build_room(mc,x,y,z,nx,ny,nz,block_type):
    
    mc.postToChat("Building a room")
    # build floor
    # mc.setBlocks(x, y, z, x+my_length, y, z+my_width, block_type)
    build_square(mc,x,y,z,nx,nz,'xz', block_type)

    # build ceiling
    #mc.setBlocks(x, y+my_height, z, x+my_length, y+my_height, z+my_width, block_type)
    build_square(mc,x,y+ny,z,nx,nz,'xz', block_type)

    # build walls
    #mc.setBlocks(x,        y,       z, x, y+my_height, z+my_width, block_type)
    #mc.setBlocks(x,        y,       z, x+my_length, y+my_height, z,       block_type)
    #mc.setBlocks(x,        y,    z+my_width, x+my_length, y+my_height, z+my_width, block_type)
    #mc.setBlocks(x+my_length, y,       z, x+my_length, y+my_height, z+my_width, block_type)
    build_square(mc,x,   y,z,   ny, nz, 'yz', block_type)
    build_square(mc,x,   y,z,   nx, ny, 'xy', block_type)
    build_square(mc,x,   y,z+nz,nx, ny, 'xy', block_type)
    build_square(mc,x+nx,y,z,   ny, nz, 'yz', block_type)

    # fill the room with air
    BLOCK_AIR = 0
    mc.setBlocks(x+1, y+1, z+1, x+nx-1, y+ny-1, z+nz-1, BLOCK_AIR)

def build_tower(mc, x,y,z, my_radius, my_height, block_type):
    # build a tower of a given radius with lower left corner x,z and height y

    raise Exception('build_tower not yet implemented. need to finish build_cylinder')

    # starting position defines the lower left corner
    
    mc.postToChat("Building a tower")

    from math import sqrt

    # build fill a circle on the top
    mc.setBlocks(x, y, z, x+my_length, y, z+my_width, block_type)

    # build ceiling
    mc.setBlocks(x, y+my_height, z, x+my_length, y+my_height, z+my_width, block_type)

    # build walls
    mc.setBlocks(x,        y,       z, x, y+my_height, z+my_width, block_type)
    mc.setBlocks(x,        y,       z, x+my_length, y+my_height, z,       block_type)
    mc.setBlocks(x,        y,    z+my_width, x+my_length, y+my_height, z+my_width, block_type)
    mc.setBlocks(x+my_length, y,       z, x+my_length, y+my_height, z+my_width, block_type)


