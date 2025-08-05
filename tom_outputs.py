import nuke
original_dir='/kpnas/vfx/KPVFX/The Keeper/NukeEdit/../Outputs/'
new_dir='/kpnas/vfx/Keeper Tom/Outputs/'


for node in nuke.selectedNodes():
    new_file_path=node['file'].value().replace(original_dir, new_dir)
    node['file'].setValue(new_file_path)
    if 'colorspace' in node.knobs() and 'gamma' in node['colorspace'].value().lower():
        node['colorspace'].setValue('rec709')