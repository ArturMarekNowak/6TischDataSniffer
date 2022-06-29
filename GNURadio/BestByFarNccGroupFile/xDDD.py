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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class xDDD(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "xDDD")

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
        self.sps = sps = samp_rate // 500000
        self.number_of_samples = number_of_samples = 10000000
        self.seed = seed = 0x00
        self.number_of_samples_after_decimation = number_of_samples_after_decimation = number_of_samples // sps
        self.mask = mask = 0x110
        self.length = length = 9
        self.centre_freq = centre_freq = 863.042e6

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1_1_0_0_1_0_1 = qtgui.time_sink_f(
            number_of_samples, #size
            samp_rate, #samp_rate
            'analog', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_update_time(0.01)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_1_0_0_1_0_1.enable_tags(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_1_0_0_1_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_1_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_1_0_1_win)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0 = qtgui.time_sink_f(
            number_of_samples_after_decimation, #size
            samp_rate, #samp_rate
            'before descrambling', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_1_0_0_1_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_1_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_1_0_0_win)
        self.qtgui_time_sink_x_1_1_0_0_1_0 = qtgui.time_sink_f(
            number_of_samples_after_decimation, #size
            samp_rate, #samp_rate
            'symbol suync', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_1_0.set_update_time(0.01)
        self.qtgui_time_sink_x_1_1_0_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_1_0_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_1_0_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_1_0.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_1_0_0_1_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_1_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_1_0_win)
        self.qtgui_time_sink_x_1_1_0_0_1 = qtgui.time_sink_f(
            number_of_samples_after_decimation, #size
            samp_rate, #samp_rate
            'after descrambling', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_1.set_update_time(0.01)
        self.qtgui_time_sink_x_1_1_0_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_1_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_1_0_0_1.enable_tags(True)
        self.qtgui_time_sink_x_1_1_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_1.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1_1_0_0_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_1_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_1_win)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(
            digital.TED_MUELLER_AND_MULLER,
            sps,
            0.045,
            1.0,
            1.0,
            1.5,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_descrambler_bb_0_0_0 = digital.descrambler_bb(mask, seed, length)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.blocks_uchar_to_float_0_0_0_1_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0_0_1 = blocks.uchar_to_float()
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(5, 1, 4000, 1)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, number_of_samples)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'C:\\Users\\artur\\OneDrive\\Desktop\\6TSCH_ID65535.raw', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(-37, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_1_1_0_0_1_0_1, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_1, 0), (self.qtgui_time_sink_x_1_1_0_0_1, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_1_0, 0), (self.qtgui_time_sink_x_1_1_0_0_1_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.blocks_uchar_to_float_0_0_0_1_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_descrambler_bb_0_0_0, 0))
        self.connect((self.digital_descrambler_bb_0_0_0, 0), (self.blocks_uchar_to_float_0_0_0_1, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.qtgui_time_sink_x_1_1_0_0_1_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "xDDD")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(self.samp_rate // 500000)
        self.qtgui_time_sink_x_1_1_0_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0_0_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0_0_1_0_1.set_samp_rate(self.samp_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_number_of_samples_after_decimation(self.number_of_samples // self.sps)

    def get_number_of_samples(self):
        return self.number_of_samples

    def set_number_of_samples(self, number_of_samples):
        self.number_of_samples = number_of_samples
        self.set_number_of_samples_after_decimation(self.number_of_samples // self.sps)
        self.blocks_head_0.set_length(self.number_of_samples)

    def get_seed(self):
        return self.seed

    def set_seed(self, seed):
        self.seed = seed

    def get_number_of_samples_after_decimation(self):
        return self.number_of_samples_after_decimation

    def set_number_of_samples_after_decimation(self, number_of_samples_after_decimation):
        self.number_of_samples_after_decimation = number_of_samples_after_decimation

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





def main(top_block_cls=xDDD, options=None):

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
