nuke.pluginAddPath("./NukeSurvivalToolkit")
nuke.pluginAddPath("./Gizmos")


import autosave

# Project Settings > Default format
#nuke.knobDefault("Root.format", "HD_1080")
nuke.knobDefault("Root.format", "UHD_4K")

# Project Settings > Default frame rate
nuke.knobDefault("Root.fps", "23.976")


