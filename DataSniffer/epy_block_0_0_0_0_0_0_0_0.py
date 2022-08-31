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
        
        inp = input_items[0]
        indices = numpy.where(inp[:-96] == 2)
        if indices:
            self.conn.executemany(self.SQL_QUERY,
                                   zip(
                                   [time.time_ns()] * len(indices),
                                   [self.channel] * len(indices),
                                   #[self.littleEndianToBig(inp[i:i+16]) for i in indices],
                                   #[self.littleEndianToBig(inp[i+16:i+32]) for i in indices],
                                   #[self.littleEndianToBig(inp[i+32:i+64]) for i in indices],
                                   #[self.littleEndianToBig(inp[i+64:i+80]) for i in indices],
                                   #[self.littleEndianToBig(inp[i+80:i+96]) for i in indices]
                                   [0],
                                   [0],
                                   [0],
                                   [0],
                                   [0]
                                   ))
      
        return max(0, len(inp) - 96)  

        
    def littleEndianToBig(self, inputBits):
    
        try:
            array = np.array(inputBits)
            array = np.packbits(array, bitorder='big')
            
            outputBits = array[0]

        except:
            print("littleEndianToBig error")
            return 0
            
        return outputBits