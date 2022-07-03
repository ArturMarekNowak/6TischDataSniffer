#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: artur
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
import math
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class DataSniffer6TSCHDataSniffer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "DataSniffer6TSCHDataSniffer")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4000000
        self.sps = sps = samp_rate // 200000
        self.skip_points = skip_points = 2202000
        self.seed = seed = 0x00
        self.points = points = 7000
        self.mask = mask = 0x110
        self.length = length = 9
        self.centre_freq = centre_freq = 863.042e6

        ##################################################
        # Blocks
        ##################################################
        self.digital_descrambler_bb_0_0_0 = digital.descrambler_bb(mask, seed, length)
        self.digital_correlate_access_code_bb_0 = digital.correlate_access_code_bb('1001000001001110', 0)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(sps*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_points)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(2, 1, 4000, 1)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, points)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'C:\\Users\\artur\\OneDrive\\Desktop\\Workspace\\6tschDataSniffer\\Files\\6TSCH_ID65535.raw', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\artur\\OneDrive\\Desktop\\repacked.dat', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\artur\\OneDrive\\Desktop\\scrambled.dat', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\artur\\OneDrive\\Desktop\\notscrambled', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(-37, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_head_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_head_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_correlate_access_code_bb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.digital_correlate_access_code_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_correlate_access_code_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_correlate_access_code_bb_0, 0), (self.digital_descrambler_bb_0_0_0, 0))
        self.connect((self.digital_descrambler_bb_0_0_0, 0), (self.blocks_file_sink_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DataSniffer6TSCHDataSniffer")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(self.samp_rate // 200000)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps*(1+0.0))

    def get_skip_points(self):
        return self.skip_points

    def set_skip_points(self, skip_points):
        self.skip_points = skip_points

    def get_seed(self):
        return self.seed

    def set_seed(self, seed):
        self.seed = seed

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points
        self.blocks_head_0.set_length(self.points)

    def get_mask(self):
        return self.mask

    def set_mask(self, mask):
        self.mask = mask

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_centre_freq(self):
        return self.centre_freq

    def set_centre_freq(self, centre_freq):
        self.centre_freq = centre_freq





def main(top_block_cls=DataSniffer6TSCHDataSniffer, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
