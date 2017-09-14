'''
Created on Sep 14, 2017

@author: jphanso

ref: https://docs.python.org/3.6/library/xml.etree.elementtree.html

root.tag (inode | directory)

'''

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from sys import exit
from tkinter import _support_default_root

def shred_line(line):
    def shred_directory(root):
        print(root.tag)
        for elem in root:
            print(elem.text)
    
    def shred_inode(root):
        print(root.tag)
        for elem in root:
            if elem.text != None:
                print(elem.tag, ': ', elem.text)
            else:
                for blocks in elem:
                    for block in blocks:
                        if block.tag == 'numBytes':
                            print(block.tag, ': ', block.text)
    
    try:
        root = ET.fromstring(line)
        
        if root.tag == 'directory':
            shred_directory(root)
        if root.tag == 'inode':
            shred_inode(root)
        else:
            pass
    except ParseError as e:
        if e.code == 3:  # no element found.  Strip off first <*>
#             print('no element found.  Strip off first <*>')
            line = line[line.find('>') + 1:]
            shred_line(line)
        if (e.code == 4 or e.code == 9): # not well formed
            # remove the first tag and re-parse.
            line = line[line.find('>') + 1:]
            shred_line(line) 
        else:
            pass
#             print(e)   

def main():
    
    line = '<inode><id>16432</id><type>FILE</type><name>apache-log4j-extras-1.2.17.jar</name><replication>3</replication><mtime>1504280150137</mtime><atime>1504280149965</atime><preferredBlockSize>134217728</preferredBlockSize><permission>oozie:oozie:0775</permission><blocks><block><id>1073741834</id><genstamp>1010</genstamp><numBytes>448794</numBytes></block></blocks><storagePolicyId>0</storagePolicyId></inode>'
#     line = '<directory><parent>16390</parent><child>16392</child><child>16393</child></directory>'
#     line = '<INodeDirectorySection><directory><parent>16385</parent><child>17451</child><child>16386</child><child>16389</child></directory>'
#     line = '</INodeDirectorySection>'
#     line = '<FileUnderConstructionSection></FileUnderConstructionSection>'
#     line = '<INodeSection><lastInodeId>19541</lastInodeId><numInodes>2540</numInodes><inode><id>16385</id><type>DIRECTORY</type><name></name><mtime>1504282402845</mtime><permission>hdfs:supergroup:0755</permission><nsquota>9223372036854775807</nsquota><dsquota>-1</dsquota></inode>'
#     line = '<lastInodeId>19541</lastInodeId><numInodes>2540</numInodes><inode><id>16385</id><type>DIRECTORY</type><name></name><mtime>1504282402845</mtime><permission>hdfs:supergroup:0755</permission><nsquota>9223372036854775807</nsquota><dsquota>-1</dsquota></inode>'
#     line = '<SecretManagerSection><currentId>0</currentId><tokenSequenceNumber>0</tokenSequenceNumber><numDelegationKeys>0</numDelegationKeys><numTokens>0</numTokens></SecretManagerSection><CacheManagerSection><nextDirectiveId>1</nextDirectiveId><numDirectives>0</numDirectives><numPools>0</numPools></CacheManagerSection>'
#     line = 'fsdafdsfdsa'
    shred_line(line)

if __name__ == '__main__':
    main()