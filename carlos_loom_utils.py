import nuke
import os
import nukescripts

def open_loom_comp():
    # List of projects - modify this as needed
    #projects = ["POS-30608-Love_Language", "POS-30633-Lolavie - DC", "POS-30633-Lolavie"]
    comp_names = {"POS-30608-Love_Language":"LOV",
                  "POS-30633-Lolavie - DC":"LOL",
                  "POS-30633-Lolavie":"LOL"  }
    
    escaped_projects = ['"{}"'.format(p) for p in comp_names.keys()]

    # Create a dropdown panel
    p = nuke.Panel("Open New Project")
    p.addEnumerationPulldown("Project", " ".join(escaped_projects))
    p.addSingleLineInput("Sequence (sq)", "")
    p.addSingleLineInput("Shot", "")
    p.addSingleLineInput("Version (e.g. 01)", "1")
    p.addSingleLineInput("Artist", "CA")

    # Show the panel and get values
    if not p.show():
        return  # Cancelled

    project = p.value("Project")
    sq = p.value("Sequence (sq)").zfill(4)
    shot = p.value("Shot").zfill(4)
    version = p.value("Version (e.g. 01)").zfill(3)  # Zero-pad version
    artist = p.value("Artist")
    shot_name = f"{comp_names[project]}_Sq{sq}_Sh{shot}"

    # Construct path
    file_path = f"v:/{project}/050_Production/020_Comps/Sq{sq}/{shot_name}/020_Projects/060_FinalComp/{shot_name}_v{version}_{artist}.nk"
    #V:/POS-30608-Love_Language/050_Production/020_Comps/Sq0069/LOV_Sq0069_Sh0007/020_Projects/060_FinalComp/LOV_Sq0069_Sh0007_v001_CA.nk

    if not os.path.exists(file_path):
        nuke.message(f"File not found:\n{file_path}")
        return

    if nuke.root().modified():
        if nuke.ask("Save current script before closing?"):
            nukescripts.scriptSave()

    nuke.scriptClose()
    nuke.scriptOpen(file_path)

def create_read_from_write():
    # Get selected nodes
    selected_nodes = nuke.selectedNodes()
    
    if not selected_nodes:
        nuke.message("Please select a Write node.")
        return

    write_node = None
    for node in selected_nodes:
        if node.Class() == 'Write':
            write_node = node
            break
    
    if not write_node:
        nuke.message("No Write node selected.")
        return

    # Get file path and colorspace from Write node
    file_path = write_node['file'].value().replace('/Volumes/VFX/', 'v:/')
    colorspace = write_node['colorspace'].value()

    if not file_path:
        nuke.message("Selected Write node has no file path.")
        return

    # Create Read node
    read_node = nuke.createNode('Read')
    read_node['file'].setValue(file_path)
    read_node['colorspace'].setValue(colorspace)
    read_node['first'].setValue(nuke.root().firstFrame())
    read_node['last'].setValue(nuke.root().lastFrame())

    # Position read node under the write node
    read_node.setXpos(write_node.xpos())
    read_node.setYpos(write_node.ypos() + 100)

#open_new_project()