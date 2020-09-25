#interface

import compiler
import config
compiler.compileFile(config.blackwood)
compiler.compileFile(config.gen_black)

import os
import gen_black

os.chdir( config.base_dir)
gen_black.process( config.file_command+"template.txt", config.file_template_source+"XR.vob" )

print "DONE"
