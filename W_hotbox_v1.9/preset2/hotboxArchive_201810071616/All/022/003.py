#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Retouch
# COLOR: #999999
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

nuke.createNode('BackdropNode')
r = 0.36
g = 0.36
b = 0.48
hexColour = int('%02x%02x%02x%02x' % (r*255,g*255,b*255,1),16)

for i in nuke.selectedNodes():
    i.knob('label').setValue("<img src='CornerPin.png'>Retouch")
    i['note_font_size'].setValue(30)
    i['tile_color'].setValue(hexColour)
    