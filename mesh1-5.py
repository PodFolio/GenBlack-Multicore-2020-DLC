#interface
#as a vob 1
#contains main (mesh1), steering wheel mesh (mesh2), front brake caliper (mesh3), rear brake caliper (mesh4), central rearview mirror mesh (mesh5)

import compiler
import config
compiler.compileFile(config.blackwood)
compiler.compileFile(config.gen_black)

import os
import gen_black

os.chdir( config.base_dir)
gen_black.process( config.file_command+"mesh1-5.txt", config.file_input+"xr_main.vob" )

print "DONE"
