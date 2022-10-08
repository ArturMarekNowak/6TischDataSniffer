#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: artur
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

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
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.ctrlport.monitor import *
import DataSniffer_epy_block_0_0_0_0_0_0_0_4 as epy_block_0_0_0_0_0_0_0_4  # embedded python block
import DataSniffer_epy_block_0_0_0_0_0_0_0_4_0 as epy_block_0_0_0_0_0_0_0_4_0  # embedded python block
import DataSniffer_epy_block_0_0_0_0_0_0_0_4_0_0 as epy_block_0_0_0_0_0_0_0_4_0_0  # embedded python block
import DataSniffer_epy_block_0_0_0_0_0_0_0_4_0_0_0 as epy_block_0_0_0_0_0_0_0_4_0_0_0  # embedded python block
import DataSniffer_epy_block_0_0_0_0_0_0_0_4_1 as epy_block_0_0_0_0_0_0_0_4_1  # embedded python block
import osmosdr
import time



from gnuradio import qtgui

class DataSniffer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
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

        self.settings = Qt.QSettings("GNU Radio", "DataSniffer")

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
        self.samp_rate = samp_rate = 2000000
        self.threshold = threshold = -37
        self.samp_rate_divide = samp_rate_divide = samp_rate
        self.omega = omega = samp_rate // 50000
        self.numpoints = numpoints = 10240
        self.filterFIR = filterFIR =  firdes.low_pass(1,samp_rate,150000,70000)

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(869.1e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(0, 0)
        self.rtlsdr_source_0.set_if_gain(0, 0)
        self.rtlsdr_source_0.set_bb_gain(0, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self.qtgui_waterfall_sink_x_1 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_1.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_1_win)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0 = qtgui.time_sink_f(
            102400, #size
            samp_rate, #samp_rate
            "Channel 62", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0 = qtgui.time_sink_f(
            102400, #size
            samp_rate, #samp_rate
            "Channel 64", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_2_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_2_0_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0 = qtgui.time_sink_f(
            102400, #size
            samp_rate, #samp_rate
            "Channel 56", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_2_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_2_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_2_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0_2 = qtgui.time_sink_f(
            102400, #size
            samp_rate, #samp_rate
            "Channel 68", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0_2.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0_0_0_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_2.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_2.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0_2.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_2_win)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
            102400, #size
            samp_rate, #samp_rate
            "Channel 52", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0 = filter.freq_xlating_fir_filter_ccc(1, filterFIR, 200000, samp_rate_divide)
        self.freq_xlating_fir_filter_xxx_0_0_0_0 = filter.freq_xlating_fir_filter_ccc(1, filterFIR, 400000, samp_rate_divide)
        self.freq_xlating_fir_filter_xxx_0_0_0 = filter.freq_xlating_fir_filter_ccc(1, filterFIR, -400000, samp_rate_divide)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(1, filterFIR, 800000, samp_rate_divide)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, filterFIR, -800000, samp_rate_divide)
        self.epy_block_0_0_0_0_0_0_0_4_1 = epy_block_0_0_0_0_0_0_0_4_1.blk(channel='868.3MHz')
        self.epy_block_0_0_0_0_0_0_0_4_0_0_0 = epy_block_0_0_0_0_0_0_0_4_0_0_0.blk(channel='869.1MHz')
        self.epy_block_0_0_0_0_0_0_0_4_0_0 = epy_block_0_0_0_0_0_0_0_4_0_0.blk(channel='869.5MHz')
        self.epy_block_0_0_0_0_0_0_0_4_0 = epy_block_0_0_0_0_0_0_0_4_0.blk(channel='868.7MHz')
        self.epy_block_0_0_0_0_0_0_0_4 = epy_block_0_0_0_0_0_0_0_4.blk(channel='869.9MHz')
        self.digital_correlate_access_code_tag_xx_0_0_2 = digital.correlate_access_code_tag_bb('1001000001001110', 0, 'foo')
        self.digital_correlate_access_code_tag_xx_0_0_1 = digital.correlate_access_code_tag_bb('1001000001001110', 0, 'foo')
        self.digital_correlate_access_code_tag_xx_0_0_0 = digital.correlate_access_code_tag_bb('1001000001001110', 0, 'foo')
        self.digital_correlate_access_code_tag_xx_0_0 = digital.correlate_access_code_tag_bb('1001000001001110', 0, 'foo')
        self.digital_correlate_access_code_tag_xx_0 = digital.correlate_access_code_tag_bb('1001000001001110', 0, 'foo')
        self.digital_clock_recovery_mm_xx_0_0_0_0_0_0 = digital.clock_recovery_mm_ff(omega, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0_0_0_0 = digital.clock_recovery_mm_ff(omega, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0_0_0 = digital.clock_recovery_mm_ff(omega, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0_0 = digital.clock_recovery_mm_ff(omega, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(omega, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0_0_0_0_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0_0_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_uchar_to_float_0_0_0_0_0_0_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0_0_0_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0_0_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0_0_0 = blocks.uchar_to_float()
        self.blocks_moving_average_xx_0_0_0_0_0_0 = blocks.moving_average_ff(15, 1, 4000, 1)
        self.blocks_moving_average_xx_0_0_0_0 = blocks.moving_average_ff(15, 1, 4000, 1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(15, 1, 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(15, 1, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(15, 1, 4000, 1)
        self.blocks_ctrlport_monitor_performance_0 = not False or monitor("gr-perf-monitorx")
        self.analog_simple_squelch_cc_0_0_0_0_0_0 = analog.simple_squelch_cc(threshold, 1)
        self.analog_simple_squelch_cc_0_0_0_0 = analog.simple_squelch_cc(threshold, 1)
        self.analog_simple_squelch_cc_0_0_0 = analog.simple_squelch_cc(threshold, 1)
        self.analog_simple_squelch_cc_0_0 = analog.simple_squelch_cc(threshold, 1)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(threshold, 1)
        self.analog_quadrature_demod_cf_0_0_0_0_0_0_0 = analog.quadrature_demod_cf(1)
        self.analog_quadrature_demod_cf_0_0_0_0_0 = analog.quadrature_demod_cf(1)
        self.analog_quadrature_demod_cf_0_0_0_0 = analog.quadrature_demod_cf(1)
        self.analog_quadrature_demod_cf_0_0_0 = analog.quadrature_demod_cf(1)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0_0_0_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0_0_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0, 0), (self.analog_quadrature_demod_cf_0_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_0, 0), (self.analog_quadrature_demod_cf_0_0_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_0_0, 0), (self.analog_quadrature_demod_cf_0_0_0_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_0_0_0_0, 0), (self.analog_quadrature_demod_cf_0_0_0_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0_0_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0_0_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_2, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_2_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_2_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0_0_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_correlate_access_code_tag_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_correlate_access_code_tag_xx_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0_0, 0), (self.digital_correlate_access_code_tag_xx_0_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0_0_0, 0), (self.digital_correlate_access_code_tag_xx_0_0_1, 0))
        self.connect((self.digital_binary_slicer_fb_0_0_0_0_0_0, 0), (self.digital_correlate_access_code_tag_xx_0_0_2, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0_0, 0), (self.digital_binary_slicer_fb_0_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0_0_0, 0), (self.digital_binary_slicer_fb_0_0_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0_0_0_0_0, 0), (self.digital_binary_slicer_fb_0_0_0_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.epy_block_0_0_0_0_0_0_0_4_1, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0, 0), (self.epy_block_0_0_0_0_0_0_0_4, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_0, 0), (self.epy_block_0_0_0_0_0_0_0_4_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_1, 0), (self.epy_block_0_0_0_0_0_0_0_4_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_2, 0), (self.epy_block_0_0_0_0_0_0_0_4_0_0_0, 0))
        self.connect((self.epy_block_0_0_0_0_0_0_0_4, 0), (self.blocks_uchar_to_float_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_0_0_0_0_0_0_4_0, 0), (self.blocks_uchar_to_float_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_0_0_0_0_0_0_4_0_0, 0), (self.blocks_uchar_to_float_0_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_0_0_0_0_0_0_4_0_0_0, 0), (self.blocks_uchar_to_float_0_0_0_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_0_0_0_0_0_0_4_1, 0), (self.blocks_uchar_to_float_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_simple_squelch_cc_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0, 0), (self.analog_simple_squelch_cc_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0, 0), (self.analog_simple_squelch_cc_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0, 0), (self.analog_simple_squelch_cc_0_0_0_0_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_waterfall_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DataSniffer")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_filterFIR( firdes.low_pass(1,self.samp_rate,150000,70000))
        self.set_omega(self.samp_rate // 50000 )
        self.set_samp_rate_divide(self.samp_rate )
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0_0_2_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.analog_simple_squelch_cc_0.set_threshold(self.threshold)
        self.analog_simple_squelch_cc_0_0.set_threshold(self.threshold)
        self.analog_simple_squelch_cc_0_0_0.set_threshold(self.threshold)
        self.analog_simple_squelch_cc_0_0_0_0.set_threshold(self.threshold)
        self.analog_simple_squelch_cc_0_0_0_0_0_0.set_threshold(self.threshold)

    def get_samp_rate_divide(self):
        return self.samp_rate_divide

    def set_samp_rate_divide(self, samp_rate_divide):
        self.samp_rate_divide = samp_rate_divide

    def get_omega(self):
        return self.omega

    def set_omega(self, omega):
        self.omega = omega
        self.digital_clock_recovery_mm_xx_0.set_omega(self.omega)
        self.digital_clock_recovery_mm_xx_0_0.set_omega(self.omega)
        self.digital_clock_recovery_mm_xx_0_0_0.set_omega(self.omega)
        self.digital_clock_recovery_mm_xx_0_0_0_0.set_omega(self.omega)
        self.digital_clock_recovery_mm_xx_0_0_0_0_0_0.set_omega(self.omega)

    def get_numpoints(self):
        return self.numpoints

    def set_numpoints(self, numpoints):
        self.numpoints = numpoints

    def get_filterFIR(self):
        return self.filterFIR

    def set_filterFIR(self, filterFIR):
        self.filterFIR = filterFIR
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.filterFIR)
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(self.filterFIR)
        self.freq_xlating_fir_filter_xxx_0_0_0.set_taps(self.filterFIR)
        self.freq_xlating_fir_filter_xxx_0_0_0_0.set_taps(self.filterFIR)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0.set_taps(self.filterFIR)




def main(top_block_cls=DataSniffer, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
