"""Aplicación principal Tkinter — TC1038 Movilidad Inteligente."""
from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.app.win_home import open_win_home
from src.app.win_form import open_win_form
from src.app.win_table import open_win_table
from src.app.win_dashboard import open_win_dashboard
from src.app.win_external import open_win_external
from src.app.win_canvas import open_win_canvas


def main():
    root = tk.Tk()
    root.title("TC1038 — SafeStride")
    root.geometry("520x420")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="SafeStride", font=("Segoe UI", 16, "bold")).pack(pady=(0, 6))
    ttk.Label(frame, text="Starter App — Para un ciclismo mas seguro").pack(pady=(0, 18))
    buttons = [
        ("🏠 Inicio: ¿Que es Ruta Segura?", open_win_home),
        ("📝 Reporte en formularios", open_win_form),
        ("👥 Reportes de la comunidad", open_win_table),
        ("Análisis / dashboard", open_win_dashboard),
        ("Datos externos / API", open_win_external),
        ("Canvas con API", open_win_canvas),
    ]
    for text, fn in buttons:
        ttk.Button(frame, text=text, command=lambda f=fn: f(root)).pack(fill="x", pady=5)
    ttk.Separator(frame).pack(fill="x", pady=12)
    ttk.Button(frame, text="Salir", command=root.destroy).pack()
    root.mainloop()

if __name__ == "__main__":
    main()
