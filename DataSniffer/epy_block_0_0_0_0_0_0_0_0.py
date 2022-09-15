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
        self.buffer = []
        self.bufferTimestamp = str(datetime.datetime.now())
        
    def __del__(self):
        self.conn.close()

    def work(self, input_items, output_items):
        
        for i in range(len(input_items[0])):            
            
            if input_items[0][i] == 2 and len(self.buffer) == 0:  
                self.bufferTimestamp = str(datetime.datetime.now())
                self.buffer.append(0)
                continue
                
            if input_items[0][i] == 3 and len(self.buffer) == 0:  
                self.bufferTimestamp = str(datetime.datetime.now())
                self.buffer.append(1)
                continue
                
            if len(self.buffer) > 0 and len(self.buffer) < 88: 
                self.buffer.append(input_items[0][i])
            
            if len(self.buffer) == 88:
                                
                length = np.array(self.buffer[i:i+8], dtype=np.int)
                length = np.packbits(length, bitorder='big')
                length.dtype = np.uint8
                            
                currentPacketNumber = np.array(self.buffer[i+8:i+24], dtype=np.int)
                currentPacketNumber = np.packbits(currentPacketNumber, bitorder='big')
                currentPacketNumber.dtype = np.uint16
                                      
                testId = np.array(self.buffer[i+24:i+56], dtype=np.int)
                testId = np.packbits(testId, bitorder='big')
                testId.dtype = np.uint32
                                       
                totalPacketCount = np.array(self.buffer[i+56:i+72], dtype=np.int)
                totalPacketCount = np.packbits(totalPacketCount, bitorder='big')
                totalPacketCount.dtype = np.uint16
                                        
                payloadDataLength = np.array(self.buffer[i+72:i+88], dtype=np.int)
                payloadDataLength = np.packbits(payloadDataLength, bitorder='big')
                payloadDataLength.dtype = np.uint16
                    
                self.conn.execute(f"INSERT INTO Log (Timestamp,Channel,Length,CurrentPacketNumber,TestId,TotalPacketCount,PayloadDataLength) VALUES ('{timestamp}', '{self.channel}', '{length}', '{currentPacketNumber}','{testId}', '{totalPacketCount}', '{payloadDataLength}' )");
                self.buffer = []
        
        self.conn.commit()
        output_items[0][:] = input_items[0][:]
        return len(output_items[0])