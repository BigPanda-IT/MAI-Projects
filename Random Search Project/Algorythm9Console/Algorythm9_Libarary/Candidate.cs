using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorythm9_Libarary
{
    public class Candidate
    {
        public Candidate(Func<double, double> yFromX, string asText)
        {
            YfromX = yFromX;
            _asText= asText;
        }

        private string _asText;

        public override string ToString()
        {
            return _asText;
        }

        public readonly Func<double, double> YfromX;
        public double Quality(List<Point> source)
        {
            //double[] Ys = new double[source.Length]

            double sumOfOtklon = 0;
            for (int i = 0; i < source.Count; i++)
            {
                //Ys[i] = YfromX(source[i].X);
                var y = YfromX(source[i].X);

                sumOfOtklon += Math.Abs(y - source[i].Y);
            }

            if (sumOfOtklon == 0)
                return 1;

            double sredOtklon = sumOfOtklon / source.Count;

            double quality = 1 / sredOtklon;

            //double quality = maxOtklon / sredOtklon;
            return quality;
        }

        static public Candidate RandomSearch(List<Point> source, List<Candidate> candidates, TimeSpan deltaTime)
        {
            Random random = new Random(DateTime.Now.Millisecond);
            var Best = candidates[random.Next(0, candidates.Count)];

            DateTime endTime = DateTime.Now.Add(deltaTime);

            while (Best.Quality(source) < 1 && DateTime.Now < endTime)
            {
                Candidate S = candidates[random.Next(0, candidates.Count)];

                Console.WriteLine("now quality: " + S.Quality(source));

                if (S.Quality(source) > Best.Quality(source))
                {
                    Best = S;
                }
            }

            return Best;
        }

        static public List<Candidate> GenerateCandidates()
        {
            List<Candidate> candidates = new List<Candidate>();

            candidates.Add(new Candidate((double x) => x * x, "f(x) = x*x"));
            candidates.Add(new Candidate((double x) => x + 2, "f(x) = x+2"));
            candidates.Add(new Candidate((double x) => x * x - 50, "f(x) = x*x - 50"));
            candidates.Add(new Candidate((double x) => x + 2 + x * x, "f(x) = x+2 + x*x"));
            candidates.Add(new Candidate((double x) => x * 2 * x, "f(x) = x*x * 2"));
            candidates.Add(new Candidate((double x) => x + 2 - 999, "f(x) = x + 2 - 999"));

            return candidates;
        }
    }

   
}
