import numpy as np
from gnuradio import gr
import datetime
import sqlite3
import uuid
import _thread
import numpy
import time
import pmt

class blk(gr.sync_block):

    def __init__(self, channel='channel'):

        gr.sync_block.__init__(
            self,
            name='Packet parser',
            in_sig=[np.byte],
            out_sig=[np.byte]
        )

        self.channel = channel
        self.conn = sqlite3.connect("/home/artur/Desktop/Workspace/6tschDataSniffer/Database/Database.db", check_same_thread=False)
        self.conn.execute("PRAGMA synchronous=OFF")

        self.buffer = []
        self.bufferTimestamp = str(datetime.datetime.now())

    def __del__(self):
        self.conn.close()


    def work(self, input_items, output_items):

        if len(self.buffer) != 0:

            if len(self.buffer) + len(input_items[0]) < 88:
                #print("DEBUG 3" + str(len(self.buffer)))
                self.buffer.extend(input_items[0])
                #print("DEBUG 4" + str(len(self.buffer)))
                return len(output_items[0])

            if len(self.buffer) + len(input_items[0]) >= 88:
                #print("DEBUG 5" + str(len(self.buffer)))
                self.buffer.extend(input_items[0][:(88 - len(self.buffer))])
                #print("DEBUG 6" + str(len(self.buffer))) 
                length, currentPacketNumber, testId, totalPacketCount, payloadDataLength = self.formData(self.buffer)
                self.conn.execute(f"INSERT INTO Log (Timestamp,Channel,Length,CurrentPacketNumber,TestId,TotalPacketCount,PayloadDataLength) VALUES ('{self.bufferTimestamp}', '{self.channel}', '{length}', '{currentPacketNumber}','{testId}', '{totalPacketCount}', '{payloadDataLength}' )");
                self.buffer = []
                #print("DEBUG 7" + str(len(self.buffer))) 
        
        tags = self.get_tags_in_window(0, 0, len(input_items[0]))
        for tag in tags:

            timestamp = str(datetime.datetime.now())
            offset = tag.offset - self.nitems_read(0)

            if len(input_items[0]) - offset >= 88:
                length, currentPacketNumber, testId, totalPacketCount, payloadDataLength = self.formData(input_items[0][offset:offset+88])
                self.conn.execute(f"INSERT INTO Log (Timestamp,Channel,Length,CurrentPacketNumber,TestId,TotalPacketCount,PayloadDataLength) VALUES ('{timestamp}', '{self.channel}', '{length}', '{currentPacketNumber}','{testId}', '{totalPacketCount}', '{payloadDataLength}' )");

            else:
                #print("DEBUG 1" + str(len(self.buffer)))
                self.bufferTimestamp = str(datetime.datetime.now())
                self.buffer.extend(input_items[0][offset:len(input_items[0])])
                #print("DEBUG 2" + str(len(self.buffer)))

        self.conn.commit()
        output_items[0][:] = input_items[0][:]
        return len(output_items[0])

    def formData(self, input_buffer):
        length = np.array(input_buffer[:8])
        length = np.packbits(length, bitorder='big')
        length.dtype = np.uint8

        currentPacketNumber = np.array(input_buffer[8:24])
        currentPacketNumber = np.packbits(currentPacketNumber, bitorder='big')
        currentPacketNumber.dtype = np.uint16

        testId = np.array(input_buffer[24:56])
        testId = np.packbits(testId, bitorder='big')
        testId.dtype = np.uint32

        totalPacketCount = np.array(input_buffer[56:72])
        totalPacketCount = np.packbits(totalPacketCount, bitorder='big')
        totalPacketCount.dtype = np.uint16

        payloadDataLength = np.array(input_buffer[72:88])
        payloadDataLength = np.packbits(payloadDataLength, bitorder='big')
        payloadDataLength.dtype = np.uint16
        return str(length), str(currentPacketNumber), str(testId), str(totalPacketCount), str(payloadDataLength)

