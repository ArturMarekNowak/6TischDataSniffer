using System.Collections.Generic;

namespace DataScrapper.Helpers;

public class PacketsHelper
{
    private int _packetsLength { get; set; }

    public PacketsHelper(int packetsLength)
    {
        _packetsLength = packetsLength;
    }
    
    IEnumerable<int> lsfr(int seed, int polynomial)
    {
        while (true)
        {
            var lsb = seed & 1;
            seed = seed >> 1;
            if (lsb != 0)
            {
                seed = seed ^ polynomial;
                yield return 1;
            }
            else
            {
                yield return 0;
            }
        }
    }
    
    
}