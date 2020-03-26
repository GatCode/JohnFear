#!/usr/bin/env python
# coding: utf-8

# # Read PGN/SPN csv file
# 
# Hello verybody, finally we will dive into the package analysis.
# This is your first shot, so we decided to go with python due to simpliness.
# Please find the PGN/SPN csv list in your repository. First we will just read it into a dataframe, which we will use later for decoding the stream. The module pandas does actually all the work for us, we just need to pass the proper parameters.

# In[1]:


import pandas as pd
from pathlib import Path


# In[2]:


# set file path and read into pandas dataframe
# sorry guys, but currently we are not sure if we are allowed to publish your pgn spn list
pgnSpnPath = Path('/home/akarner/Downloads/JohnFearData/pgnSpn/pgn_spn.csv') 
# make sure to pass the pipe as delimiter and remove all NaN fields
psDf = pd.read_csv(pgnSpnPath, sep='|', na_filter=False)


# In[3]:


psDf


# # Read Wireshark (pcapng) file
# We are going to use scapy module for package analysis in python

# In[4]:


from scapy.all import *


# In[5]:


# read your capture file
capturePath = '/home/akarner/tulocal/JohnFear/captures/13Feb2020.pcapng'
capture = rdpcap(capturePath)


# In[6]:


# get some information from a random package 
#   -> this will be 2712 package in wireshark
pack = capture[2711]

# general about the package
print(pack)

# package fields
print(pack.fields)

# value from a field
print(pack.fields['src'])

# get raw payload
print(pack.payload)


# In[7]:


# custom poc j1939 class, which will dissect { canId, pgn and data }
class j1939():
    def __init__(self, bdata):
        self.bdata = bdata
        self.canId = None
        self.pgn = None
        self.data = None
        
        self._readCanId()
        self._readPgn()
        self._readData()
    
    def _readCanId(self):
        canId = bytearray(4)
        # pack canId bytes
        for idx in range(0, 4):
            struct.pack_into('!B', canId, 4 - (idx+1), self.bdata[idx])
        
        # remove first 3 bits from msb -> 0x1f and mask
        canId[0] &= 0x1f
        self.canId = bytes(canId)
    
    def _readPgn(self):
        # remove last byte
        pgn = bytearray(self.canId[:-1])
        # reserve just first two bits from first byte
        pgn[0] &= 0x03
        self.pgn = int.from_bytes(pgn, byteorder='big')        
    
    def _readData(self):
        self.data = self.bdata[8:]
    
    @staticmethod
    def getHexString(bytearr):
        return '0x' + ''.join('%02x' % b for b in bytearr)
        
    def __str__(self):
        return 'j1939[canId: %s, pgn: %i, data: %s]' % (j1939.getHexString(self.canId), self.pgn, j1939.getHexString(self.data))
        


# Finally we have prepared your poc j1939 class which extracts all the information out of the raw payload.
# Further all the pgn and spns are loaded to your pandas dataframe, so everything is prepared for linking them together.
# 
# Because pandas supports joining dataframes, we will transform the captured data into a dataframe and join by pgn the information to it.

# In[8]:


# initiate new dataframe, seems like this takes very very long :)
capDf = pd.DataFrame(None, columns=['ccanid', 'cpgn', 'cdata'])
for cap in capture:
    m = j1939(cap.payload.load)
    capDf = capDf.append({'ccanid':m.canId, 'cpgn': m.pgn, 'cdata': m.data}, ignore_index=True)


# In[9]:


capDf


# In[10]:


# let's start the join fun
result = pd.merge(capDf, psDf, left_on='cpgn', right_on='PGN#')

print(result)

# dump the result as csv
result.to_csv('result.csv', sep='|')


# In[ ]:




