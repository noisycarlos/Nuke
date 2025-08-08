import nuke

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

# Run the function
create_read_from_write()