using System;
using System.Diagnostics;
using System.IO;
using System.Text;

namespace DataScrapper
{
    class HexDumpHelper
    {
        private readonly string[] _demodulatedPacketsFiles = Directory.GetFiles("../../../../../Files/DemodulatedPackets");
        private readonly string[] _outputDirectory = Directory.GetFiles("../../../../../Files/DemodulatedPacksAsBinaryStrings");
        
        private string RemoveEvenIndexCharacters(string s)
        {
            var sb = new StringBuilder();
  
            for(int i = 0; i < s.Length; i++)
            {
                if (i % 2 == 0) continue;
                sb.Append(s[i]);
            }
            
            return sb.ToString(); 
        } 
        
        public void DumpCapturedPacketsAsSingleString()
        {
            foreach (var file in _demodulatedPacketsFiles)
            {
                var process = Process.Start("CMD.exe", $"/C xxd -p {Path.GetFullPath(file)} > ..\\..\\..\\..\\..\\Files\\DemodulatedPacksAsBinaryStrings\\{Path.GetFileNameWithoutExtension(file)}.txt");
                process.WaitForExit();
            }

            foreach (var file in _outputDirectory)
            {
                var fileContent = File.ReadAllText(file);
                fileContent = fileContent.Replace("\r", "");
                fileContent = fileContent.Replace("\n", "");
                fileContent = RemoveEvenIndexCharacters(fileContent);
                File.WriteAllText(file, fileContent);
            }
        }
    }

    class DataScrapper
    {
        private string[] _demodulatedBinaryStringFiles = Directory.GetFiles("../../../../../Files/DemodulatedPacksAsBinaryStrings");
        private string sfd = "1001000001001110";

        public void SfdsConunt()
        {
            foreach (var file in _demodulatedBinaryStringFiles)
            {
                var fileContent = File.ReadAllText(file);
                var packets = fileContent.Split(sfd);
                Console.WriteLine($"SFD's found in {file}: {packets.Length}");
            }
        }
    }
    
    class Program
    {
        public static void Main()
        {
            var hexDump = new HexDumpHelper();
            hexDump.DumpCapturedPacketsAsSingleString();

            var datascrapper = new DataScrapper();
            datascrapper.SfdsConunt();
        }
    }
}

