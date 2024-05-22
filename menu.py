#nuke.knobDefault('Read.colorspace', 'Utility - Raw')

#import W_hotbox, W_hotboxManager



def toggleBW():
    selectedNode = None
    try:
        selectedNode = nuke.selectedNode()
    except:    
        nuke.message("select a RotoPaint node!")
        return
    if selectedNode.Class() == 'RotoPaint':
        if not selectedNode.knob('toolbar_paint_color').value(1):
            selectedNode.knob('toolbar_paint_color').setValue(1)
        else:
            selectedNode.knob('toolbar_paint_color').setValue(0)
    else:
        nuke.message("select a RotoPaint node!")
        return

viewer = nuke.menu('Viewer')
viewer.addCommand('RotoPaint/toggle b\/w', 'toggleBW()', 'shift+d')


try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()

toolbar = nuke.toolbar('Nodes')
AddedNodes = toolbar.addMenu('AddedNodes', icon='MENU ICON.png')

AddedNodes.addCommand('edgeNoise', 'nuke.createNode(\'edgeNoise\')')