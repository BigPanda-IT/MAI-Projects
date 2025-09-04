namespace Algorythm9_Gui
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.Calculate = new System.Windows.Forms.Button();
            this.PointsAddButton = new System.Windows.Forms.Button();
            this.DeltaTimeTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Calculate
            // 
            this.Calculate.Location = new System.Drawing.Point(16, 287);
            this.Calculate.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Calculate.Name = "Calculate";
            this.Calculate.Size = new System.Drawing.Size(493, 116);
            this.Calculate.TabIndex = 0;
            this.Calculate.Text = "Найти лучшую функцию и показать графики";
            this.Calculate.UseVisualStyleBackColor = true;
            this.Calculate.Click += new System.EventHandler(this.button1_Click);
            // 
            // PointsAddButton
            // 
            this.PointsAddButton.Location = new System.Drawing.Point(16, 15);
            this.PointsAddButton.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.PointsAddButton.Name = "PointsAddButton";
            this.PointsAddButton.Size = new System.Drawing.Size(365, 101);
            this.PointsAddButton.TabIndex = 1;
            this.PointsAddButton.Text = "Добавить точки";
            this.PointsAddButton.UseVisualStyleBackColor = true;
            this.PointsAddButton.Click += new System.EventHandler(this.button2_Click);
            // 
            // DeltaTimeTextBox
            // 
            this.DeltaTimeTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.DeltaTimeTextBox.Location = new System.Drawing.Point(168, 217);
            this.DeltaTimeTextBox.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.DeltaTimeTextBox.Name = "DeltaTimeTextBox";
            this.DeltaTimeTextBox.Size = new System.Drawing.Size(213, 30);
            this.DeltaTimeTextBox.TabIndex = 2;
            this.DeltaTimeTextBox.TextChanged += new System.EventHandler(this.DeltaTimeTextBox_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 138);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(383, 16);
            this.label1.TabIndex = 3;
            this.label1.Text = "Сколько секунд ожидать нахождения лучшего кандидата:";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(692, 434);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.DeltaTimeTextBox);
            this.Controls.Add(this.PointsAddButton);
            this.Controls.Add(this.Calculate);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Calculate;
        private System.Windows.Forms.Button PointsAddButton;
        private System.Windows.Forms.TextBox DeltaTimeTextBox;
        private System.Windows.Forms.Label label1;
    }
}

