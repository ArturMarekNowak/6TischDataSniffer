using System.Collections.Generic;

namespace DataScrapper.Helpers;

public static class Dewhitener
{
    public static IEnumerable<int> Lsfr(int seed, int polynomial)
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