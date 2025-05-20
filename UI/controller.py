import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._listCountry = self._model.getAllNazioni()
        for c in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))

        for i in range(2015, 2019):
            self._listYear.append(i)
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))



    def handle_graph(self, e):
        nazione = self._view.ddcountry.value
        anno = self._view.ddyear.value
        self._model.buildGraph(nazione, anno)
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()}  Numero di archi: {self._model.getNumArchi()}"))
        self._view.update_page()


    def handle_volume(self, e):
        volumi = self._model.getVolumi()
        for v in volumi:
            self._view.txtOut2.controls.append(ft.Text(f"{v[0]} --> {v[1]}"))
        self._view.update_page()


    def handle_path(self, e):
        pass
