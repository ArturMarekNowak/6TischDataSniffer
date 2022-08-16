using DataScrapper.Helpers;

namespace DataScrapper
{
    class Program
    {
        public static void Main()
        {
            var hexDump = new HexDumpHelper();
            hexDump.DumpCapturedPacketsAsSingleString();

            var datascrapper = new Helpers.DataScrapper();
            datascrapper.SfdsConunt();
        }
    }
}

