# __GenBlack Multicore 2020 DLC__
by __[EvolutionBG](https://www.youtube.com/channel/UCaqpQhZLBMO8V1bdW9bTgXQ)__ and __[Draggo](https://podfolio.eu/)__<br>
*Big thanks for testing to* __[DMN'](https://dmnmods.blogspot.com/)__

[![GitHub release](https://img.shields.io/github/release/PodFolio/GenBlack-Multicore-2020-DLC.svg?logo=github)](https://github.com/PodFolio/GenBlack-Multicore-2020-DLC/releases/latest)

- [Download](https://github.com/PodFolio/GenBlack-Multicore-2020-DLC/releases/latest)

## Movies
[![GenBlack 2020 DLC](https://img.youtube.com/vi/APL2Di4R_jw/0.jpg)](https://www.youtube.com/watch?v=APL2Di4R_jw)

1st implementation by EvolutionBG<br>
[![1st implementation by EvolutionBG](https://img.youtube.com/vi/CIBI8bXLHqk/0.jpg)](https://www.youtube.com/watch?v=CIBI8bXLHqk)

pypy vs python comparsion<br>
[![pypy vs python comparsion](https://img.youtube.com/vi/YnjJE7KdSGs/0.jpg)](https://www.youtube.com/watch?v=YnjJE7KdSGs)

## Instructions
Instalation tutorial by __[DMN'](https://dmnmods.blogspot.com/)__<br>
[![Instalation tutorial by DMN'](https://img.youtube.com/vi/e5ig4Th8moU/0.jpg)](https://www.youtube.com/watch?v=e5ig4Th8moU)

Extract to gen_black main directory

Use config.py to set default working directories

Edit mesh6-24.py to chose what type of mesh you want to use mirror_fix.vob (mirror fix enabled mesh [for example this mod use this type of mesh](https://dmnmods.blogspot.com/2020/07/nissan-skyline-r33-gt-r-vspec-97-rhd-10v.html)) or mesh_off.vob (mirror fix disabled mesh).
mesh1-5.py use main.vob that contains main mesh, steering wheel mesh, front brake caliper mesh, rear brake caliper mesh, central rearview mirror mesh

Edit path destinations to mesh .py files in "run.bat" and "run without stops.bat", and python directory in "run with IDLE.bat"

Right click on "run.bat" or "run without stops.bat" and use "Run as a Administrator" to avoid Windows UAC spam (if UAC is enabled in your system). You can also make shortcut to bat files and in shortcut properties in Advanced button chose "Run as a Administrator" and start bat files from that shortcut. You do not do all of that for "run with IDLE.bat"

You can also make shortcuts to mesh .py files and run them manualy one by one ;)

Use "join files.bat" to join files into XR.vob

Sadly render_template command cause errors when two or more mesh .py files try to render template using this same jpg file. For render_template you can use template.py file, but as we all know gen_black has a problem with reading through own generated files so it will be not always work, so you can edit one of "run" bat files for example:

all files below start at once<br>
start C:\Python27\Lib\idlelib\idle.pyw -r F:\LFS\gen_black\dist\mesh8.py<br>
start C:\Python27\Lib\idlelib\idle.pyw -r F:\LFS\gen_black\dist\mesh7.py<br>
every file below start separately<br>
C:\Python27\Lib\idlelib\idle.pyw -r F:\LFS\gen_black\dist\mesh6.py<br>
C:\Python27\Lib\idlelib\idle.pyw -r F:\LFS\gen_black\dist\mesh1-5.py<br>

## VOB Parts
| FILE | CONTAINS |
|:--:| -- |
| main.vob| main (mesh1) |
| | steering wheel mesh (mesh2) |
| | front brake caliper (mesh3) |
| | rear brake caliper (mesh4) |
| | central rearview mirror mesh (mesh5) |
| mesh_fix.vob | one default mirror fix enabled mesh (mesh1) |
| mesh_off.vob | one default mirror fix disabled mesh (mesh1) |

