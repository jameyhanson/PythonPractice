'''
Created on Sep 12, 2017

@author: jphanso
'''
import _testbuffer
from ctypes.test import test_frombuffer
from test import test_univnewlines

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
                        
Written with the assumption the the source file does not fit in memory.

Taken from: http://enginerds.craftsy.com/blog/2014/04/parsing-large-xml-files-in-python-without-a-billion-gigs-of-ram.html
'''

import xml.etree.cElementTree as ET

def process_buffer(buf):
    # see https://docs.python.org/3.6/library/xml.etree.elementtree.html
    tnode = ET.fromstring(buf)

    print(len(tnode)) # [0] is parent, rest are children 

    for inodeID in tnode:
        pass
#         print(inodeID.text)

def main():
    XML_FILE='fsimage.xml'
    
    i=False
    with open(XML_FILE, 'r') as inputfile:
        for line in inputfile: 
            if '<directory>' in line:
                if i: process_buffer(line)
                i = True
            else:
                pass
    
if __name__ == '__main__':
    main()