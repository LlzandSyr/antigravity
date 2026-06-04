import xml.etree.ElementTree as ET

proj_path = r'd:\project_stm32\1.homework\demo8_oled_gif\DEMO.uvprojx'

# Parse the XML file
tree = ET.parse(proj_path)
root = tree.getroot()

# Find the group with GroupName = image
image_group = None
for group in root.findall('.//Group'):
    group_name_elem = group.find('GroupName')
    if group_name_elem is not None and group_name_elem.text == 'image':
        image_group = group
        break

if image_group is not None:
    # Check if Files element already exists
    files_elem = image_group.find('Files')
    if files_elem is None:
        files_elem = ET.SubElement(image_group, 'Files')
    
    # Files to add
    new_files = [
        ('gif_a_frame_0_mono.c', '.\\image\\gif_a_frame_0_mono.c'),
        ('gif_a_frame_7_mono.c', '.\\image\\gif_a_frame_7_mono.c'),
        ('gif_a_frame_12_mono.c', '.\\image\\gif_a_frame_12_mono.c'),
    ]
    
    # Check existing files to avoid duplicates
    existing_filepaths = {f.find('FilePath').text for f in files_elem.findall('.//File') if f.find('FilePath') is not None}
    
    for filename, filepath in new_files:
        if filepath not in existing_filepaths:
            file_elem = ET.SubElement(files_elem, 'File')
            
            filename_sub = ET.SubElement(file_elem, 'FileName')
            filename_sub.text = filename
            
            filetype_sub = ET.SubElement(file_elem, 'FileType')
            filetype_sub.text = '1' # 1 represents .c source file in Keil
            
            filepath_sub = ET.SubElement(file_elem, 'FilePath')
            filepath_sub.text = filepath
            
            print(f'Added {filename} to image group.')
        else:
            print(f'{filename} already exists in image group.')
            
    # Save the XML file
    tree.write(proj_path, encoding='utf-8', xml_declaration=True)
    print('DEMO.uvprojx saved successfully!')
else:
    print('Error: Could not find image group in DEMO.uvprojx')
