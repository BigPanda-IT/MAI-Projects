using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorythm9
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Candidate> candidates = new List<Candidate>();

            candidates.Add(new Candidate((double x) => x * x));
            candidates.Add(new Candidate((double x) => x+2));
            candidates.Add(new Candidate((double x) => x * x - 50));
            candidates.Add(new Candidate((double x) => x + 2 + x*x));
            candidates.Add(new Candidate((double x) => x* 2 * x));
            candidates.Add(new Candidate((double x) => x + 2 - 999));

            List<Point> sourcePoints = new List<Point>();
            sourcePoints.Add(new Point(1, 1));
            sourcePoints.Add(new Point(2, 4));
            sourcePoints.Add(new Point(3, 9));

            var best = RandomSearch(sourcePoints.ToArray(), candidates.ToArray(), new TimeSpan(0, 0, 2));

            //List<double> YsFromBest = new List<double>();
            foreach(Point point in sourcePoints)
            {
                //YsFromBest.Add(best.YfromX(point.X));
                Console.Write(best.YfromX(point.X) + " ");
           
            }
            Console.WriteLine();

            Console.WriteLine(string.Join(" ", sourcePoints.Select(p => p.Y)));

            Console.ReadLine();
        }

        class Candidate
        {
            public Candidate(Func<double, double> yFromX)
            {
                YfromX = yFromX;
            }

            public readonly Func<double, double> YfromX;
            public double Quality(Point[] source)
            {
                //double[] Ys = new double[source.Length]

                double sumOfOtklon = 0;
                for (int i = 0; i<source.Length; i++)
                {
                    //Ys[i] = YfromX(source[i].X);
                    var y = YfromX(source[i].X);

                    sumOfOtklon += Math.Abs(y - source[i].Y);
                }

                if (sumOfOtklon == 0)
                    return 1;

                double sredOtklon = sumOfOtklon / source.Length;
                
                double quality = 1 / sredOtklon;

                //double quality = maxOtklon / sredOtklon;
                return quality;
            }
        }

        struct Point
        {
            public Point(double x, double y)
            {
                X = x;
                Y = y;
            }
            public double X;
            public double Y;
        }

        static Candidate RandomSearch(Point[] source, Candidate[] candidates, TimeSpan deltaTime)
        {
            Random random = new Random(DateTime.Now.Millisecond);
            var Best = candidates[random.Next(0, candidates.Length)];

            DateTime endTime = DateTime.Now.Add(deltaTime);

            while(Best.Quality(source) < 1 && DateTime.Now < endTime)
            {
                Candidate S = candidates[random.Next(0, candidates.Length)];

                Console.WriteLine("now quality: " + S.Quality(source));

                if(S.Quality(source) > Best.Quality(source))
                {
                    Best = S;
                }
            }

            return Best;
        }
    }
}
