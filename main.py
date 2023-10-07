import tkinter as tk
from tkinter import ttk
import numpy as np
import threading

class GeoExploreApp:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("GeoExplore")

        # Create a custom theme
        self.style = ttk.Style()
        self.style.theme_create("custom_theme", parent="alt", settings={
            "TNotebook": {"configure": {"background": "#34495E"}},
            "TNotebook.Tab": {
                "configure": {"padding": [10, 5], "background": "#2C3E50", "foreground": "white"},
                "map": {"background": [("selected", "#E74C3C")]}
            }
        })
        self.style.theme_use("custom_theme")

        self.notebook = ttk.Notebook(self.root)

        self.create_earth_processes_analysis_tab()
        self.create_disaster_prediction_tab()

        self.notebook.pack(padx=10, pady=10, fill="both", expand=True)

    def create_earth_processes_analysis_tab(self):
        earth_tab = ttk.Frame(self.notebook)
        self.notebook.add(earth_tab, text="Earth Processes Analysis")

        map_label = ttk.Label(earth_tab, text="Earth Processes Map", font=("Arial", 14))
        map_label.pack(pady=10)

        start_button = ttk.Button(earth_tab, text="Start Monitoring", command=self.start_monitoring)
        start_button.pack(pady=10)

        self.monitoring_label = ttk.Label(earth_tab, text="", font=("Arial", 12))
        self.monitoring_label.pack(pady=10)

    def create_disaster_prediction_tab(self):
        disaster_tab = ttk.Frame(self.notebook)
        self.notebook.add(disaster_tab, text="Disaster Prediction and Response")

        predict_button = ttk.Button(disaster_tab, text="Predict Disaster", command=self.predict_disaster)
        predict_button.pack(pady=10)

        self.predicted_disaster_listbox = tk.Listbox(disaster_tab, height=10, width=50, font=("Arial", 12))
        self.predicted_disaster_listbox.pack(pady=10)

    def start_monitoring(self):
        self.monitoring_thread = threading.Thread(target=self._monitor_data)
        self.monitoring_thread.start()

    def _monitor_data(self):
        while True:
            # Replace with actual data retrieval logic
            plate_tectonics_data = np.random.rand()
            earthquake_data = np.random.rand()
            self.monitoring_label.config(text=f"Plate Tectonics: {plate_tectonics_data:.2f}, Earthquake: {earthquake_data:.2f}")
            self.root.update()
            self.root.after(1000)

    def predict_disaster(self):
        # Replace with actual disaster prediction logic
        disaster_likelihood = np.random.rand()
        self.predicted_disaster_listbox.delete(0, tk.END)
        self.predicted_disaster_listbox.insert(tk.END, f"Disaster Likelihood: {disaster_likelihood:.2f}")

if _name_ == "_main_":
    app = GeoExploreApp()
    app.root.mainloop()
