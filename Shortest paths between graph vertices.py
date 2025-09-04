import pydot
import heapq
import dijkstra

import sys

from PyQt6.QtWidgets import (QDialog, QApplication, 
    QPushButton, QVBoxLayout,
    QHBoxLayout, QTextEdit, QSpinBox,
    QListWidget, QListWidgetItem, QDialogButtonBox,
    QLabel, QComboBox, QLineEdit, QSlider, QTableWidget,
    QTableWidgetItem, QMainWindow, QWidget, QMenuBar,
    QFileDialog, QHeaderView
    )
from PyQt6.QtGui import QAction
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtCore import (Qt, QSize)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import networkx as nx


def main():
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    main.resize(1000, 800)
    
    # showing the window
    main.show()

    # loop
    sys.exit(app.exec())


class QMySvgWidget(QSvgWidget):
    def sizeHint(self):
        return QSize(600, 600)

class AdjacencyMatrix(QDialog):
    def __init__(self, parent, graph):
        super().__init__(parent)

        self.G = graph

        self.setWindowTitle("Adjacency Matrix")

        QBtn = (QDialogButtonBox.StandardButton.Ok 
            | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()

        n = graph.number_of_nodes()
        self.tableWidget = QTableWidget()    

        self.tableWidget.setRowCount(n)
        self.tableWidget.setColumnCount(n)

        for ev in graph.edges.data():
            self.tableWidget.setItem(ev[0], ev[1], 
                QTableWidgetItem(str(ev[2]['weight'])))

        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)        

        
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        for i in range(n):
            self.tableWidget.setHorizontalHeaderItem(i, 
                QTableWidgetItem(str(i)))
            self.tableWidget.setVerticalHeaderItem(i, 
                QTableWidgetItem(str(i)))


    def update(self):
        # self.toVertice = self.toComboBox.currentData()
        # self.fromVertice = self.fromComboBox.currentData()        
        # self.weight = float(self.weightTextEdit.text())        
        pass

    def accept(self):
        self.G.clear_edges()
        n = self.G.number_of_nodes()
        for i in range(n):
            for j in range(n):
                if i >= j:
                    continue
                it = self.tableWidget.item(i, j)
                if it is None:
                    continue
                t = it.text()
                print(i, j, t)
                self.G.add_edge(i, j, weight=float(t))
        super().accept()

    def reject(self):
        super().reject()



class AddEdgeDialog(QDialog):
    def __init__(self, parent, vertices):
        super().__init__(parent)

        self.setWindowTitle("New Edge")

        QBtn = (QDialogButtonBox.StandardButton.Ok 
            | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()

        fromHBox = QHBoxLayout()
        fromHBox.addWidget(QLabel("From: "))
        self.fromComboBox = QComboBox(self)         
        for v in vertices:
            self.fromComboBox.addItem(str(v), v)
        fromHBox.addWidget(self.fromComboBox)


        toHBox = QHBoxLayout()
        toHBox.addWidget(QLabel("To: "))
        self.toComboBox = QComboBox(self)          
        for v in vertices:
            self.toComboBox.addItem(str(v), v)            
        toHBox.addWidget(self.toComboBox)

        weightHBox = QHBoxLayout()
        weightHBox.addWidget(QLabel("Weight: "))
        self.weightTextEdit = QLineEdit(self)     
        self.weightTextEdit.setText("1")  
        weightHBox.addWidget(self.weightTextEdit)
        

        self.layout.addLayout(fromHBox)
        self.layout.addLayout(toHBox)
        self.layout.addLayout(weightHBox)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.accepted.connect(self.update)

    def update(self):
        self.toVertice = self.toComboBox.currentData()
        self.fromVertice = self.fromComboBox.currentData()        
        self.weight = float(self.weightTextEdit.text())        

class Window(QWidget):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        menubar = QMenuBar()
        layout.addWidget(menubar)
        actionFile = menubar.addMenu("File")
        self.openAction = QAction("&Open", self)
        actionFile.addAction(self.openAction)
        self.openAction.triggered.connect(self.openActionSlot)
        # actionFile.addAction("Open")

        self.saveAction = QAction("&Save", self)
        actionFile.addAction(self.saveAction)
        self.saveAction.triggered.connect(self.save)

        self.adjacencyMatrixAction = QAction("&Adj Matrix", self)
        actionFile.addAction(self.adjacencyMatrixAction)
        self.adjacencyMatrixAction.triggered.connect(self.show_adjacency_matrix)

        topHBox = QHBoxLayout()        
        
        controlVBox = QVBoxLayout()
        
        self.spinBoxVertices = QSpinBox()
        self.spinBoxVertices.valueChanged.connect(self.spinBoxVertices_changed)
        controlVBox.addWidget(self.spinBoxVertices)        

        self.start = 0

        self.listEdges = QListWidget()
        

        controlVBox.addWidget(self.button)

        startHBox = QHBoxLayout()
        startHBox.addWidget(QLabel("Start: "))
        self.startComboBox = QComboBox(self)
        self.startComboBox.currentIndexChanged.connect(self.update_start)            

        startHBox.addWidget(self.startComboBox)

        controlVBox.addLayout(startHBox)


        controlVBox.addWidget(self.listEdges)


        edgesButtonsHBox = QHBoxLayout()

        self.buttonAddEdge = QPushButton('Add Edge')
        self.buttonAddEdge.clicked.connect(lambda x: self.add_edge())
        edgesButtonsHBox.addWidget(self.buttonAddEdge)

        self.buttonRemoveEdge = QPushButton('Remove Edge')
        self.buttonRemoveEdge.clicked.connect(self.remove_edge)
        edgesButtonsHBox.addWidget(self.buttonRemoveEdge)

        controlVBox.addLayout(edgesButtonsHBox)


        topHBox.addLayout(controlVBox)
        
        topHBox.addWidget(self.canvas)

        bottomHBox = QHBoxLayout()
        self.runButton = QPushButton("Run")
        self.stepSlider = QSlider()  
        self.stepSlider.setOrientation(Qt.Orientation.Horizontal)      
        bottomHBox.addWidget(self.runButton)
        bottomHBox.addWidget(self.stepSlider)

        self.runButton.clicked.connect(self.run)        
        
        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        layout.addLayout(topHBox)

        algorithmHBox = QHBoxLayout()

        self.verticesDistanceTable = QTableWidget()
        self.verticesDistanceTable.setColumnCount(2)
        self.verticesDistanceTable.currentCellChanged.connect(self.vdt_cell_selected)

        algorithmHBox.addWidget(self.verticesDistanceTable)
        self.algorithmTextEdit = QTextEdit(self)
        algorithmHBox.addWidget(self.algorithmTextEdit)

        layout.addLayout(algorithmHBox)        
        layout.addLayout(bottomHBox)


        # setting layout to the main window
        self.setLayout(layout)

        self.G = nx.Graph()

        self.spinBoxVertices.setValue(1)

        self.open('g1.txt')

    def redraw_graph(self):
        self.plot()


    def update_edgelist(self):
        self.listEdges.clear()

        for ev in self.G.edges.data():
            fv = ev[0]
            tv = ev[1]
            w = ev[2]['weight']
            txt = f"{fv}-{tv}: {w}"
            lwi = QListWidgetItem(txt)
            lwi.setData(Qt.ItemDataRole.UserRole, (fv, tv))
            self.listEdges.addItem(lwi)

    def openActionSlot(self):
        self.open()
    def open(self, filename=None):
        if filename is None:
            filename = QFileDialog.getOpenFileName(self, 'Open File')
            print(filename[0])
            filename = filename[0]

        # filename = "graph.txt"
        
        
        with open(filename, "r") as f:
            nn = int(f.readline())
            ne = int(f.readline())
            print(nn, ne)

            self.spinBoxVertices.setValue(0)

            self.spinBoxVertices.setValue(nn)
            for _ in range(ne):
                ev = [int(x) for x in f.readline().split()]
                print(ev)
                self.add_edge(ev, False)
        self.redraw_graph()        

    def save(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        print(filename[0])

        # filename = "graph.txt"
        
        with open(filename[0], "w") as f:
            f.write(str(self.G.number_of_nodes()))
            f.write('\n')
            f.write(str(self.G.number_of_edges()))
            f.write('\n')
            for ev in self.G.edges.data():
                f.write(f"{ev[0]} {ev[1]} {ev[2]['weight']}")
                f.write('\n')

    def update_start(self, x):
        self.start = self.startComboBox.itemData(x)

    def vdt_cell_selected(self, cr, cl, pr, pc):
        # print(cr, cl)
        v = self.verticesDistanceTable.item(cr, 0)
        if v is None:
            return
        
        v = self.verticesDistanceTable.item(cr, 0).data(Qt.ItemDataRole.UserRole)        
        self.algorithmTextEdit.clear()
        el = []
        path = [v]
        while v != self.start:
            u = self.prev[v]
            path.append(u)        
            el.append((u, v))
            v = u
        path.reverse()

        self.algorithmTextEdit.setText(str(path))

        self.plot(False)
        nx.draw_networkx_labels(self.G, 
            {v:(x, y + 10) for v, (x, y) in self.G_layout.items()}, self.distances)


        nx.draw_networkx_edges(self.G, self.G_layout,
            edgelist=el, edge_color="red", width=3.0)


    def run(self):
        res, distances, prev = dijkstra.dijkstra(self.G, self.start)

        self.distances = distances
        self.prev = prev

        self.verticesDistanceTable.clear()
        self.verticesDistanceTable.setRowCount(len(distances))
        i = 0
        for d in distances:
            twi = QTableWidgetItem(str(d))
            twi.setData(Qt.ItemDataRole.UserRole, d)
            self.verticesDistanceTable.setItem(i, 0, twi)
            self.verticesDistanceTable.setItem(i, 1, QTableWidgetItem(str(distances[d])))
            i += 1

        nx.draw_networkx_labels(self.G, 
            {v:(x, y + 10) for v, (x, y) in self.G_layout.items()}, distances)  

        self.algorithmTextEdit.clear()
        self.algorithmTextEdit.setPlainText(res)


    def show_adjacency_matrix(self):
        dlg = AdjacencyMatrix(self, self.G)

        if dlg.exec():   
            self.update_edgelist()
            self.redraw_graph()
        else:
            return

    def add_edge(self, edge=None, redraw=True):
        # print(edge)
        if edge is None:
            dlg = AddEdgeDialog(self, self.G.nodes())

            if dlg.exec():   
                fv = dlg.fromVertice
                tv = dlg.toVertice
                w = dlg.weight        
            else:
                return
        else:
            fv, tv, w = edge
        
        
        # graph (model)
        self.G.add_edge(fv, tv, w)

        txt = f"{fv}-{tv}: {w}"
        lwi = QListWidgetItem(txt)
        lwi.setData(Qt.ItemDataRole.UserRole, (fv, tv))
        self.listEdges.addItem(lwi)

        if redraw:            
            self.redraw_graph()
        

    def remove_edge(self, redraw=True):
        (fv, tv) = self.listEdges.currentItem().data(Qt.ItemDataRole.UserRole)
        self.G.remove_edge(fv, tv)
        self.listEdges.takeItem(self.listEdges.currentRow())

        if redraw:
            self.redraw_graph()

    def spinBoxVertices_changed(self):
        n_vertices = self.spinBoxVertices.value()
        self.listEdges.clear()

        self.startComboBox.clear()
        for v in range(n_vertices):
            self.startComboBox.addItem(str(v), v)

        self.G = nx.Graph() 
        for i in range(n_vertices):
            self.G.add_node(i, label=f"{i}")
        
        self.plot()

    def print_graph(self, graph, recalculateLayout=True):
        """ prints the graph"""

        # stores the nodes and their name attributes in a dictionary        
        plt.ion()

        if recalculateLayout:
            H = nx.convert_node_labels_to_integers(graph, label_attribute='node_label')
            # H_layout = nx.nx_pydot.graphviz_layout(graph, prog='fdp')
            H_layout = nx.nx_pydot.graphviz_layout(graph, prog='circo')
            # H_layout = nx.circular_layout(H)
            self.G_layout = {H.nodes[n]['node_label']: p for n, p in H_layout.items()}

        nx.draw(graph, self.G_layout)

        nodes_names = nx.get_node_attributes(graph, "label")
        labels = nx.draw_networkx_labels(graph, self.G_layout, nodes_names)  
        edge_labels = nx.get_edge_attributes(graph, "weight")      
        nx.draw_networkx_edge_labels(graph, self.G_layout, edge_labels)

    # action called by the push button
    def plot(self, recalculateLayout=True):
        
        self.figure.clear()

        self.print_graph(self.G, recalculateLayout)

        # refresh canvas
        self.canvas.draw()

# driver code
if __name__ == '__main__':
    
    main()

