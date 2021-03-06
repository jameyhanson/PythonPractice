'''
Created on Sep 14, 2017

@author: jphanso

ref: https://docs.python.org/3.6/library/xml.etree.elementtree.html

root.tag (inode | directory)
ignore all other root tags

directory root
    parentID and (0 to many) child IDs
    flat_output:
        parentID1, childID1
        parentID1, childID2
        parentID2, childID1
    list_output:
        {parentID1:[childID1, childID2]}
        {parentID2:[chileID2]}
inode root
    ID and attributes (type, name, mtime, atime, numBytes)

'''

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from sys import exit
from tkinter import _support_default_root

def shred_line(line, output_flat):
    def shred_directory(root, output_flat):
        # print(root.tag)
        item_list = list(root) # convert iterable to list
        if output_flat:
            for i in range(1, len(item_list)):
                print(item_list[0].text + ', ' + item_list[i].text)
        else:
            children = []
            for i in range(1, len(item_list)):
                children.append(item_list[i].text)
            print('{' + item_list[0].text + ': ' + str(children) + '}')
    
    def shred_inode(root, output_flat):
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
    except ParseError as e:
        print(e, e.code, '\n', line)
        if e.code == 3:  # no element found.  Strip off first <*>
            print('no element found.  Strip off first <*>')
            line = line[line.find('>') + 1:]
            print(line)
            if len(line) > 14:  
                shred_line(line)
        if (e.code == 4 or e.code == 9): # not well formed
            # remove the first tag and re-parse.
            line = line[line.find('>') + 1:]
            print(line)
            if len(line) > 14:  
                shred_line(line) 
        else:
            print(e)   
    else:
        if root.tag == 'directory': # parent, child by ID
            shred_directory(root, output_flat)
        if root.tag == 'inode': # attributes, including name
#             shred_inode(root, output_flat)
            pass
        else:
            pass

def main():
    OUTPUT_FLAT = False
    XML_FILE='fsimage.xml'
    
#     with open(XML_FILE, 'r') as input_file:
#         for line in input_file:
#             shred_line(line, OUTPUT_FLAT)
            
#     line = '<?xml version="1.0"?>'
#     line = '<fsimage><version><layoutVersion>-60</layoutVersion><onDiskVersion>1</onDiskVersion><oivRevision>520d8b072e666e9f21d645ca6a5219fc37535a52</oivRevision></version>'
#     line = '<version><layoutVersion>-60</layoutVersion><onDiskVersion>1</onDiskVersion><oivRevision>520d8b072e666e9f21d645ca6a5219fc37535a52</oivRevision></version>'
#     line = '<layoutVersion>-60</layoutVersion><onDiskVersion>1</onDiskVersion><oivRevision>520d8b072e666e9f21d645ca6a5219fc37535a52</oivRevision></version>'
#     line = '-60</layoutVersion><onDiskVersion>1</onDiskVersion><oivRevision>520d8b072e666e9f21d645ca6a5219fc37535a52</oivRevision></version>'
    line = '<onDiskVersion>1</onDiskVersion><oivRevision>520d8b072e666e9f21d645ca6a5219fc37535a52</oivRevision></version>'
#     line = '<inode><id>16432</id><type>FILE</type><name>apache-log4j-extras-1.2.17.jar</name><replication>3</replication><mtime>1504280150137</mtime><atime>150428014965</atime><preferredBlockSize>134217728</preferredBlockSize><permission>oozie:oozie:0775</permission><blocks><block><id>1073741834</id><genstamp>1010</genstamp><numBytes>448794</numBytes></block></blocks><storagePolicyId>0</storagePolicyId></inode>'
#     line = '<directory><parent>16390</parent><child>16392</child><child>16393</child></directory>'
#     line = '<directory><parent>16428</parent><child>16429</child><child>16431</child><child>16539</child><child>16654</child><child>16781</child><child>16783</child><child>16791</child><child>16859</child><child>16860</child><child>17042</child></directory>'
#     line = '<INodeDirectorySection><directory><parent>16385</parent><child>17451</child><child>16386</child><child>16389</child></directory>'
#     line = '</INodeDirectorySection>'
#     line = '<FileUnderConstructionSection></FileUnderConstructionSection>'
#     line = '<INodeSection><lastInodeId>19541</lastInodeId><numInodes>2540</numInodes><inode><id>16385</id><type>DIRECTORY</type><name></name><mtime>1504282402845</mtime><permission>hdfs:supergroup:0755</permission><nsquota>9223372036854775807</nsquota><dsquota>-1</dsquota></inode>'
#     line = '<lastInodeId>19541</lastInodeId><numInodes>2540</numInodes><inode><id>16385</id><type>DIRECTORY</type><name></name><mtime>1504282402845</mtime><permission>hdfs:supergroup:0755</permission><nsquota>9223372036854775807</nsquota><dsquota>-1</dsquota></inode>'
#     line = '<SecretManagerSection><currentId>0</currentId><tokenSequenceNumber>0</tokenSequenceNumber><numDelegationKeys>0</numDelegationKeys><numTokens>0</numTokens></SecretManagerSection><CacheManagerSection><nextDirectiveId>1</nextDirectiveId><numDirectives>0</numDirectives><numPools>0</numPools></CacheManagerSection>'
#     line = 'fsdafdsfdsa'
    shred_line(line, OUTPUT_FLAT)

if __name__ == '__main__':
    main()