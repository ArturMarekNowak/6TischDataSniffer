using System.Diagnostics;
using System.IO;
using System.Text;

namespace DataScrapper.Helpers;

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