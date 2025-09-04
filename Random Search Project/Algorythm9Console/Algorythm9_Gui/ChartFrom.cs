using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using Algorythm9_Libarary;
namespace Algorythm9_Gui
{
    public partial class ChartFrom : Form
    {
        public ChartFrom(List<Algorythm9_Libarary.Point> points, Candidate candidate)
        {
            InitializeComponent();

            ChartPoints.ChartAreas.Add("Chart");

            Series seriesSource = new Series("f(x) = ?");
            seriesSource.ChartType = SeriesChartType.Line;
            foreach (var point in points)
            {
                seriesSource.Points.AddXY(point.X, point.Y);
            }

            Series seriesCandidate = new Series(candidate.ToString());
            seriesCandidate.ChartType = SeriesChartType.Line;
            foreach (var point in points)
            {
                seriesCandidate.Points.AddXY(point.X, candidate.YfromX(point.X));
            }

            ChartPoints.Series.Add(seriesSource);
            ChartPoints.Series.Add(seriesCandidate);

            ChartPoints.Legends.Add("f(x) = ?");
            ChartPoints.Legends.Add(candidate.ToString());
        }
    }
}
