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
            name='Packet parser IEEE',   
            in_sig=[np.byte],
            out_sig=[np.byte]
        )
        
        self.channel = channel
        self.conn = sqlite3.connect("C:/Users/artur/OneDrive/Desktop/Workspace/6tschDataSniffer/Database/Database.db", check_same_thread=False)
        self.conn.execute("PRAGMA synchronous=OFF")
        
    def __del__(self):
        self.conn.close()
        
        

    def work(self, input_items, output_items):
        
        #for i in range(len(input_items[0]) - 88):
        for i in range(len(input_items[0]) - 140):
                   
            if input_items[0][i] == 2 and i > 16:  
                timestamp = str(datetime.datetime.now())
                input_items[0][i] = 0
                               
                self.conn.execute(f"INSERT INTO LogIEEE (Timestamp,Channel,SFD,MiddleBytes,Address) VALUES ('{timestamp}', '{self.channel}', '{self.getBytesInHex(input_items[0][i-16:i])}', '{self.getBytesInHex(input_items[0][i:i+64])}', '{self.getBytesInHex(input_items[0][i+64:i+128])}')");
        
        output_items[0][:] = input_items[0][:]
        self.conn.commit()
        return len(output_items[0])

    def getBytesInHex(self, foo):
        
        rc = ""
        for i in range(0, len(foo), 8):
            rc += str("0x{:02x}".format(np.packbits(foo[i:i+8])[0])[2:])
        
        return rc