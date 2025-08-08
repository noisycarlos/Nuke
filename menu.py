#nuke.knobDefault('Read.colorspace', 'Utility - Raw')

#import W_hotbox, W_hotboxManager
import carlos_loom_utils


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
AddedNodes = toolbar.addMenu('AE Inspired', icon='MENU ICON.png')

AddedNodes.addCommand('Color Blend', 'nuke.createNode(\'ColorBlend\')')
AddedNodes.addCommand('Roughen Edges', 'nuke.createNode(\'RoughenEdges\')')

my_menu = toolbar.addMenu("Carlos Loom Utils")
my_menu.addCommand("Open Comp", "carlos_loom_utils.open_loom_comp()", "ctrl+shift+o")
my_menu.addCommand("Create read from write node", "carlos_loom_utils.create_read_from_write()", "ctrl+shift+r")

#AddedNodes.addCommand('Readd from write', 'read_from_write.create_read_from_write()')
#my_menu.addCommand("Open Comp", "read_from_write.create_read_from_write()", "ctrl+shift+r")