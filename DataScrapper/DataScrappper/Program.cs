﻿using DataScrapper.Helpers;

namespace DataScrapper
{
    class Program
    {
        public static void Main()
        {
            //var hexDump = new HexDumpHelper();
            //hexDump.DumpCapturedPacketsAsSingleString();

            var datascrapper = new Helpers.DataScrapper();
            //datascrapper.SfdsConunt();
            datascrapper.ExtractPayloads("C:\\Users\\artur\\OneDrive\\Desktop\\Workspace\\6tschDataSniffer\\Files\\DemodulatedPacksAsBinaryStrings\\id123pcktlen20total1000.txt",
                                         24, false);
        }
    }
}

