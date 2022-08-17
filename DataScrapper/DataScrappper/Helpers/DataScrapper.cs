using System.Text;

namespace DataScrapper.Helpers;

class DataScrapper
{
    private string[] _demodulatedBinaryStringFiles = Directory.GetFiles("../../../../../Files/DemodulatedPacksAsBinaryStrings");
    private string _sfd = "1001000001001110";
    private List<int> _lsfr = new()
    {
        0, 0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0 ,1,1,1,0,0,0,1,0 ,
        1,0,1,1,1,0,0,0, 0,1,1,0,0,0,1,0, 0,1,1,1,0,1,0,0, 0,0,0,0,1,1,1,0,
        1,1,1,0,0,1,1,1, 1,1,1,0,1,0,1,0, 1,0,1,1,0,1,0,0, 1,0,1,0,0,1,0,0,
        1,0,1,1,1,1,0,1, 0,0,1,1,0,0,0,0, 1,0,1,0,0,0,1,0, 1,1,0,1,1,1,1,0,
        0,1,0,1,0,1,0,0, 0,0,1,1,1,1,0,1, 1,1,1,1,1,1,0,0, 1,1,0,0,1,1,1,0,
        0,1,0,0,1,1,0,1, 1,0,1,1,0,0,0,0, 0,1,1,0,1,1,1,0, 1,0,1,1,0,0,1,0
    };

    public void SfdsConunt()
    {
        foreach (var file in _demodulatedBinaryStringFiles)
        {
            var fileContent = File.ReadAllText(file);
            var packets = fileContent.Split(_sfd);
            Console.WriteLine($"SFD's found in {file}: {packets.Length}");
        }
    }

    public void ExtractPayloads(string filePath, int packetLength, bool includeLengthFieldInDewhitening = true)
    {
        var fileContent = File.ReadAllText(filePath);
        var splitted = fileContent.Split(_sfd);
        var offset = 0;

        if (!includeLengthFieldInDewhitening) offset = 8;
        
        var sb = new StringBuilder();

        for (var index = 1; index < splitted.Length; index++)
        {
            var originalPacket = string.Concat(splitted[index].Skip(offset).Take(packetLength * 8));
            var packet = "";
            var lsfr = Dewhitener.Lsfr(0x100, 0x110).Take(packetLength * 8).ToList();

            for (int i = 0; i < packetLength * 8; i++)
            {
                var foo = (int)Char.GetNumericValue(originalPacket[i]) ^ lsfr[i];

                packet = string.Concat(packet, foo);
            }

            if (includeLengthFieldInDewhitening)
            {
                sb.Append($"{index}. {StringHelper(packet, 0, 4)} {StringHelper(packet, 4, 4)}   " +
                          $"{StringHelper(packet, 8, 4)} {StringHelper(packet, 12, 4)} {StringHelper(packet, 16, 4)} {StringHelper(packet, 20, 4)}   " +
                          $"{StringHelper(packet, 24, 4)} {StringHelper(packet, 28, 4)} {StringHelper(packet, 32, 4)} {StringHelper(packet, 36, 4)}" +
                          $" {StringHelper(packet, 40, 4)} {StringHelper(packet, 44, 4)} {StringHelper(packet, 48, 4)} {StringHelper(packet, 52, 4)}" +
                          $"   {StringHelper(packet, 56, 4)} {StringHelper(packet, 60, 4)} {StringHelper(packet, 64, 4)} {StringHelper(packet, 68, 4)}" +
                          $"   {StringHelper(packet, 72, 4)} {StringHelper(packet, 76, 4)} {StringHelper(packet, 80, 4)} {StringHelper(packet, 84, 4)}\n");
            }
            else
            {
                sb.Append($"{index}. {StringHelper(packet, 0, 4)} {StringHelper(packet, 4, 4)} " +
                          $"{StringHelper(packet, 8, 4)} {StringHelper(packet, 12, 4)}   {StringHelper(packet, 16, 4)} {StringHelper(packet, 20, 4)} " +
                          $"{StringHelper(packet, 24, 4)} {StringHelper(packet, 28, 4)} {StringHelper(packet, 32, 4)} {StringHelper(packet, 36, 4)}" +
                          $" {StringHelper(packet, 40, 4)} {StringHelper(packet, 44, 4)}   {StringHelper(packet, 48, 4)} {StringHelper(packet, 52, 4)}" +
                          $" {StringHelper(packet, 56, 4)} {StringHelper(packet, 60, 4)}   {StringHelper(packet, 64, 4)} {StringHelper(packet, 68, 4)}" +
                          $" {StringHelper(packet, 72, 4)} {StringHelper(packet, 76, 4)}\n");

            }
        }
        
        using (StreamWriter writer = new StreamWriter($"../../../../../Files/ScrappedPayloads\\{Path.GetFileNameWithoutExtension(filePath)}"+"ScrappedPayload.txt"))
        {
            if (!includeLengthFieldInDewhitening) 
                writer.WriteLine("Number\tCurrent packet number\t\ttestId\t\t\t\ttotal packet count\tpayload data length");
            else
                writer.WriteLine("Number\tLength\tCurrent packet number\t\ttestId\t\t\t\ttotal packet count\tpayload data length");
            writer.WriteLine(sb);
        }
    }
    
    private string StringHelper(string packet, int skip, int take)
    {
        return string.Concat(packet.Skip(skip).Take(take));
    }
}