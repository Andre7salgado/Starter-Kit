import tkinter as tk
from tkinter import ttk, messagebox

TITULO = "Ruta Segura León"
LEMA = "La ruta más segura, no la más rápida"

SECCIONES = [
    ("El problema",
     "Peatones, ciclistas y usuarios de monopatín eléctrico en León circulan sin saber "
     "qué zonas son peligrosas. Las apps de mapas muestran la ruta más rápida, no la más segura."),
    ("Usuario objetivo",
     "Personas que se mueven a pie, en bici o en monopatín eléctrico por León y quieren "
     "llegar sin exponerse a cruces o calles peligrosas."),
    ("Propuesta de valor",
     "Una comunidad digital donde los vecinos reportan riesgos (casi accidentes, cruces sin "
     "semáforo, banquetas dañadas). Con esos reportes la app clasifica cada zona en riesgo "
     "bajo, medio o alto, muestra a qué hora es más peligrosa y avisa si tu ruta pasa por "
     "una zona de riesgo alto."),
]

MENSAJE_IMPACTO = (
    "Dato de la OMS: Según la OMS (Informe sobre la situación mundial de la seguridad vial, 2023)los accidentes de tránsito causan 1.19 millones de muertes al año y más de la mitad (53%) son peatones, ciclistas y otros usuarios vulnerables.\n\n"
    "El 80% de los vecinos debe correr para cruzar.\n\n"
    "Cada reporte ayuda a que otra persona elija una ruta más segura."
)


def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Inicio")
    win.geometry("520x470")
    win.resizable(False, False)

    frm = ttk.Frame(win, padding=18)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text=TITULO, font=("Segoe UI", 18, "bold")).pack(anchor="w")
    ttk.Label(frm, text=LEMA, font=("Segoe UI", 11), foreground="#64748B").pack(anchor="w", pady=(0, 12))

    for titulo, texto in SECCIONES:
        caja = ttk.LabelFrame(frm, text=titulo, padding=10)
        caja.pack(fill="x", pady=5)
        ttk.Label(caja, text=texto, wraplength=440, justify="left").pack(anchor="w")

    def ir_a_reportar():
        from src.app.win_form import open_win_form 
        win.destroy()
        open_win_form(parent)

    botones = ttk.Frame(frm)
    botones.pack(anchor="w", pady=(14, 0))
    ttk.Button(botones, text="¿Por qué importa?",
               command=lambda: messagebox.showinfo("¿Por qué importa?", MENSAJE_IMPACTO, parent=win)
               ).pack(side="left")
    ttk.Button(botones, text="Reportar un riesgo", command=ir_a_reportar).pack(side="left", padx=8)