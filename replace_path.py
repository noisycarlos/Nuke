import nuke
original_dir='/kpnas/vfx/KPVFX/The Keeper/NukeEdit/../Outputs/mov/'
new_dir='/kpnas/vfx/Keeper Tom/Footage/'

for node in nuke.selectedNodes():
    new_file_path=node['file'].value().replace(original_dir, new_dir)
    node['file'].setValue(new_file_path)