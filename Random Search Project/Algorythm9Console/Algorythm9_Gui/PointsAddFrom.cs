using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Algorythm9_Libarary;

namespace Algorythm9_Gui
{
    public partial class PointsAddFrom : Form
    {
        private List<Algorythm9_Libarary.Point> _points;
        public PointsAddFrom(List<Algorythm9_Libarary.Point> points)
        {
            InitializeComponent();
            _points = points;
        }

        private void AddPoint_Click(object sender, EventArgs e)
        {
            var point = new Algorythm9_Libarary.Point();
            point.X = double.Parse(XTextBox.Text);
            point.Y = double.Parse(YTextBox.Text);

            _points.Add(point);
        }
    }
}
