import numpy as np
from gnuradio import gr
import datetime
import sqlite3
import uuid
import _thread 
import numpy
import time

class blk(gr.sync_block): 

    def __init__(self, channel='channel'):  

        gr.sync_block.__init__(
            self,
            name='Packet parser',   
            in_sig=[np.byte],
            out_sig=[np.byte]
        )
        
        self.channel = channel
        self.conn = sqlite3.connect("C:/Users/artur/OneDrive/Desktop/Workspace/6tschDataSniffer/Database/Database.db", check_same_thread=False)
        self.conn.execute("PRAGMA synchronous=OFF")
        self.SQL_QUERY = """
                            INSERT INTO Log (
                                 Timestamp, Channel, Length, CurrentPacketNumber, TestId, TotalPacketCount, PayloadDataLength
                                 )
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        """
        
    def __del__(self):
        self.conn.close()

    def work(self, input_items, output_items):
        
        for i in range(len(input_items[0]) - 88):
                   
            if input_items[0][i] == 2:  
                timestamp = str(datetime.datetime.now())
                length, currentPacketNumber, testId, totalPacketCount, payloadDataLength = self.littleEndianToBig(input_items[0][i+1:i+8], input_items[0][i+8:i+24], input_items[0][i+24:i+56], input_items[0][i+56:i+72], input_items[0][i+72:i+88])
                self.conn.execute(f"INSERT INTO Log (Timestamp,Channel,Length,CurrentPacketNumber,TestId,TotalPacketCount,PayloadDataLength) VALUES ('{timestamp}', '{self.channel}', '{length}', '{currentPacketNumber}','{testId}', '{totalPacketCount}', '{payloadDataLength}' )");
        
        output_items[0][:] = input_items[0][:]
        self.conn.commit()
        return len(output_items[0])

        
    def littleEndianToBig(self, length, currentPacketNumber, testId, totalPacketCount, payloadDataLength):
    
        array = np.array(length)
        array = np.packbits(array, bitorder='big')
        array.dtype = np.uint8
        
        length = array[0]
            
        array = np.array(currentPacketNumber)
        array = np.packbits(array, bitorder='big')
        array.dtype = np.uint16
          
        currentPacketNumber = array[0]
            
        array = np.array(testId)
        array = np.packbits(array, bitorder='big')
        array.dtype = np.uint32
           
        testId = array[0]
            
        array = np.array(totalPacketCount)
        array = np.packbits(array, bitorder='big')
        array.dtype = np.uint16
            
        totalPacketCount = array[0]
            
        array = np.array(payloadDataLength)
        array = np.packbits(array, bitorder='big')
        array.dtype = np.uint16
            
        payloadDataLength = array[0]
            
        return length, currentPacketNumber, testId, totalPacketCount, payloadDataLength