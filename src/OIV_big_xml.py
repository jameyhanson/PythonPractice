'''
Created on Sep 12, 2017

@author: jphanso
'''
# import _testbuffer
# from ctypes.test import test_frombuffer
# from test import test_univnewlines

import xml.etree.cElementTree as ET

'''
Read output from Hadoop OIV (Offline Image Viewer), which analyzes the fsimage
file and creates a VERY large XML file output.  Create three files:
    1. hierarchy file
        [parentID, [childID1, childID2, childIDn]]
    2. directory file
        [directoryID, '<directory_name>']
    3. file list file
        [fileID, {'name': '<file_name>', 
                        'mtime':<mtime>, 
                        'atime':<atime>,
                        'numbytes':<num_bytes>'}]
                        
The XML file contains 7 sections
    1. version                  not used
        OIV version information
    2. NameSection              not used
    3. INodeSection             used
        name and attributes of all INodes
        directories and files
        matches ID to name
    4. SnapshotSection          not used
    5. INodeDirectorySection    used
        parent-child relationships by ID
    6. SecretManagerSection     not used
    7. CacheManagerSection      not used
  
                        
Written with the assumption the the source file does not fit in memory.

Taken from: http://enginerds.craftsy.com/blog/2014/04/parsing-large-xml-files-in-python-without-a-billion-gigs-of-ram.html
'''

def process_buffer(buf):
    # see https://docs.python.org/3.6/library/xml.etree.elementtree.html
    tnode = ET.fromstring(buf)

    print(len(tnode)) # [0] is parent, rest are children 

    for inodeID in tnode:
        pass
#         print(inodeID.text)

def shred_INodeSection(line):
    pass

def shred_INodeDirectorySection(line):
    print(line)
    tnode = ET.fromstring(line)
    
    for node in tnode:
        print(node.text)

def main():
    XML_FILE='fsimage.xml'
    
    INodeSection = False
    in_INodeSection = False
    INodeSection_start = '<INodeSection>'
    INodeSection_end = '</INodeSection>'
    
    
    INodeDirectorySection = False
    in_INodeDirectorySection = False
    INodeDirectorySection_start = '<INodeDirectorySection>'
    INodeDirectorySection_end = '</INodeDirectorySection>'
    
#     i=False
    with open(XML_FILE, 'r') as inputfile:
        for line in inputfile: 
            if not INodeDirectorySection:
            # check each line for start of INodeSection
                if INodeDirectorySection_start in line:
                    # only the first line should be trimmed
                    if not in_INodeDirectorySection:
                        line = line[len(INodeDirectorySection_start):]
                        shred_INodeDirectorySection(line)
                        in_INodeDirectorySection = True
                    shred_INodeDirectorySection(line)
                
#             if '<directory>' in line:
#                 if i: process_buffer(line)
#                 i = True
#             else:
#                 pass
    
if __name__ == '__main__':
    main()