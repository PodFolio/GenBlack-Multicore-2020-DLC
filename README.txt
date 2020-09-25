GenBlack Multicore by
- EvolutionBG https://www.youtube.com/channel/UCaqpQhZLBMO8V1bdW9bTgXQ
- Draggo https://podfolio.eu/

Extract to gen_black main directory

Use config.py to set default working directories

Edit mesh6-24.py to chose what type of mesh you want to use mirror_fix.vob (mirror fix enabled mesh [for example this mod use this type of mesh https://dmnmods.blogspot.com/2020/07/nissan-skyline-r33-gt-r-vspec-97-rhd-10v.html]) or mesh_off.vob (mirror fix disabled mesh).
main.py use main.vob that contains main mesh, steering wheel mesh, front brake caliper mesh, rear brake caliper mesh, central rearview mirror mesh

Edit path destinations to mesh .py files in "run.bat" and "run without stops.bat"

Right click on "run.bat" or "run without stops.bat" and use "Run as a Administrator" to avoid Windows UAC spam (if UAC is enabled in your system). You can also make shortcut to bat files and in shortcut properties in Advanced button chose "Run as a Administrator" and start bat files from that shortcut.

Ypu can also make shortcuts to mesh .py files and run them manualy one by one ;)

Use "join files.bat" to join files into XR.vob

Sadly render_template command cause errors when two or more mesh .py files try to render template using this same jpg file

-----------------------------------------------------------------------
|    FILE		|		CONTAINS									  |
-----------------------------------------------------------------------
|main.vob		| main (mesh1)                                        |
|				| steering wheel mesh (mesh2)                         |
|				| front brake caliper (mesh3)                         |
|				| rear brake caliper (mesh4)                          |
|				| central rearview mirror mesh (mesh5)                |
|---------------|-----------------------------------------------------|
|mesh_fix.vob	| one default mirror fix enabled mesh (mesh1)         |
|---------------|-----------------------------------------------------|
|mesh_off.vob	| one default mirror fix disabled mesh (mesh1)        |
-----------------------------------------------------------------------