namespace Algorythm9_Gui
{
    partial class ChartFrom
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.ChartPoints = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.ChartPoints)).BeginInit();
            this.SuspendLayout();
            // 
            // ChartPoints
            // 
            this.ChartPoints.Location = new System.Drawing.Point(12, 12);
            this.ChartPoints.Name = "ChartPoints";
            this.ChartPoints.Size = new System.Drawing.Size(776, 426);
            this.ChartPoints.TabIndex = 0;
            this.ChartPoints.Text = "chart1";
            // 
            // ChartFrom
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.ChartPoints);
            this.Name = "ChartFrom";
            this.Text = "Chart_From";
            ((System.ComponentModel.ISupportInitialize)(this.ChartPoints)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart ChartPoints;
    }
}