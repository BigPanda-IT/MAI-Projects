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
    public partial class Form1 : Form
    {
        private List<Algorythm9_Libarary.Point> Points = new List<Algorythm9_Libarary.Point>();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var randomCandidates = Candidate.GenerateCandidates();

            var bestCandidate = Candidate.RandomSearch(Points, randomCandidates, new TimeSpan(0,0, int.Parse(DeltaTimeTextBox.Text)));

            var chartForm = new ChartFrom(Points, bestCandidate);

            chartForm.Show();
        }

        bool pointsAddFormCreated = false;

        private void button2_Click(object sender, EventArgs e)
        {
            if (pointsAddFormCreated)
                return;

            var pointsAddForm = new PointsAddFrom(Points);
            pointsAddFormCreated = true;
            pointsAddForm.FormClosed += PointsAddFrom_FormClosed;
            pointsAddForm.Show();
        }
        private void PointsAddFrom_FormClosed(object sender, FormClosedEventArgs e)
        {
            pointsAddFormCreated = false;
        }

        private void DeltaTimeTextBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
