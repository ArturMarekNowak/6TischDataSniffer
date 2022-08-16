using System;
using System.IO;

namespace DataScrapper.Helpers;

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