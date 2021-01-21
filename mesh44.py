#interface

import compiler
import config
compiler.compileFile(config.blackwood)
compiler.compileFile(config.gen_black)

import os
import gen_black

os.chdir( config.base_dir)
gen_black.process( config.file_command+"mesh44.txt", config.file_input+"mesh_off.vob" )

print "DONE"
