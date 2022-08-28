import numpy as np
from gnuradio import gr
import datetime
import sqlite3
import uuid


class blk(gr.sync_block): 

    def __init__(self, path='C:/Users/artur/OneDrive/Desktop/foo.txt', channel='channel'):  

        gr.sync_block.__init__(
            self,
            name='Packet parser',   
            in_sig=[np.byte],
            out_sig=[]
        )
        
        self.path = path
        self.channel = channel
        
    def work(self, input_items, output_items):
        
        #conn = sqlite3.connect("C:/Users/artur/OneDrive/Desktop/Workspace/6tschDataSniffer/Database/Database.db")
        file = open(self.path, 'a')
        file.write("executed")
        
        for i in range(len(input_items[0])):
        
            if input_items[0][i] == 2:
            
                timestamp = str(datetime.datetime.now())
                file.write(timestamp)
                input_items[0][i] = 0
   
                length, currentPacketNumber, testId, totalPacketCount, payloadDataLength = self.decodePacketPayload(input_items[0][i:i+8], input_items[0][i+8:i+24], input_items[0][i+24:i+56], input_items[0][i+56:i+72], input_items[0][i+72:i+88])
                file.write("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}\n".format(self.channel, length, currentPacketNumber, testId, totalPacketCount, payloadDataLength))
                #conn.execute(f"INSERT INTO Log (Guid,Timestamp,Channel,Length,CurrentPacketNumber,TestId,TotalPacketCount,PayloadDataLength) VALUES ('{uuid.uuid4()}', '{timestamp}', '{self.channel}', '{length}', '{currentPacketNumber}','{testId}', '{totalPacketCount}', '{payloadDataLength}' )");
                
            if input_items[0][i] == 3:
                
                timestamp = str(datetime.datetime.now())
                file.write(timestamp)
                input_items[0][i] = 1
                
                length, currentPacketNumber, testId, totalPacketCount, payloadDataLength = self.decodePacketPayload(input_items[0][i:i+8], input_items[0][i+8:i+24], input_items[0][i+24:i+56], input_items[0][i+56:i+72], input_items[0][i+72:i+88])
                file.write("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}\n".format(self.channel, length, currentPacketNumber, testId, totalPacketCount, payloadDataLength))
    
                #conn.execute(f"INSERT INTO Log (Guid,Timestamp,Channel,Length,CurrentPacketNumber,TestId,TotalPacketCount,PayloadDataLength) VALUES ('{uuid.uuid4()}', '{timestamp}', '{self.channel}', '{length}', '{currentPacketNumber}','{testId}', '{totalPacketCount}', '{payloadDataLength}' )");
                
        file.close()
        #conn.commit()
        #conn.close()
        return 0
        
    def decodePacketPayload(self, lengthBits, currentPacketNumberBits, testIdBits, totalPacketCountBits, payloadDataLengthBits):
    
        try:
            array = np.array(lengthBits)
            array = np.packbits(array, bitorder='big')
            
            length = array[0]
            
            array = np.array(currentPacketNumberBits)
            array = np.packbits(array, bitorder='big')
            
            currentPacketNumber = array[0]
            
            array = np.array(testIdBits)
            array = np.packbits(array, bitorder='big')
            
            testId = array[0]
            
            array = np.array(totalPacketCountBits)
            array = np.packbits(array, bitorder='big')
            
            totalPacketCount = array[0]
            
            array = np.array(payloadDataLengthBits)
            array = np.packbits(array, bitorder='big')
            
            payloadDataLength = array[0]
            
        except:
            return 0, 0, 0, 0, 0
    
        return length, currentPacketNumber, testId, totalPacketCount, payloadDataLength
        
        
    def inputBitsToString(self, array):
        resultString = ""
        
        for digit in array:
            resultString += str(digit)

        return resultString