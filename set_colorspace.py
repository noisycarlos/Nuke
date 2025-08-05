import nuke
for node in nuke.selectedNodes():
    if 'colorspace' in node.knobs() and 'linear' not in node['colorspace'].value().lower():
        node['colorspace'].setValue('rec709')