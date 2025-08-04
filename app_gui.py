import tkinter as tk
from tkinter import ttk, messagebox
from services import CRMService  # Import absoluto

crm = CRMService()

# ========================
# Funciones de la interfaz
# ========================

def registrar_usuario():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    email = entry_email.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    
    resultado = crm.registrar_usuario(nombre, apellidos, email, telefono, direccion)
    messagebox.showinfo("Resultado", resultado)
    listar_usuarios()

def listar_usuarios():
    lista_usuarios.delete(*lista_usuarios.get_children())
    for u in crm.repo.usuarios:
        lista_usuarios.insert("", "end", values=(u.id, u.nombre, u.apellidos, u.email))

def crear_factura():
    email = entry_factura_email.get()
    descripcion = entry_factura_desc.get()
    try:
        monto = float(entry_factura_monto.get())
    except ValueError:
        messagebox.showerror("Error", "Monto inválido")
        return
    estado = combo_factura_estado.get()
    
    resultado = crm.crear_factura(email, descripcion, monto, estado)
    messagebox.showinfo("Resultado", resultado)

def mostrar_facturas_usuario():
    email = entry_factura_email.get()
    facturas = crm.repo.facturas_por_email(email)
    
    lista_facturas.delete(*lista_facturas.get_children())
    for f in facturas:
        lista_facturas.insert("", "end", values=(f.numero, f.descripcion, f.monto, f.estado))

def mostrar_resumen():
    lista_resumen.delete(*lista_resumen.get_children())
    for nombre, total, pagadas, pendientes in crm.resumen_financiero():
        lista_resumen.insert("", "end", values=(nombre, total, pagadas, pendientes))

# ========================
# Ventana principal
# ========================

root = tk.Tk()
root.title("CRM - Gestión de Clientes")
root.geometry("800x500")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ========= TAB USUARIOS =========
frame_usuarios = ttk.Frame(notebook)
notebook.add(frame_usuarios, text="Usuarios")

tk.Label(frame_usuarios, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_usuarios)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_usuarios, text="Apellidos").grid(row=1, column=0)
entry_apellidos = tk.Entry(frame_usuarios)
entry_apellidos.grid(row=1, column=1)

tk.Label(frame_usuarios, text="Email").grid(row=2, column=0)
entry_email = tk.Entry(frame_usuarios)
entry_email.grid(row=2, column=1)

tk.Label(frame_usuarios, text="Teléfono").grid(row=3, column=0)
entry_telefono = tk.Entry(frame_usuarios)
entry_telefono.grid(row=3, column=1)

tk.Label(frame_usuarios, text="Dirección").grid(row=4, column=0)
entry_direccion = tk.Entry(frame_usuarios)
entry_direccion.grid(row=4, column=1)

tk.Button(frame_usuarios, text="Registrar Usuario", command=registrar_usuario).grid(row=5, column=0, columnspan=2, pady=5)

# Lista de usuarios
cols_usuarios = ("ID", "Nombre", "Apellidos", "Email")
lista_usuarios = ttk.Treeview(frame_usuarios, columns=cols_usuarios, show="headings")
for col in cols_usuarios:
    lista_usuarios.heading(col, text=col)
lista_usuarios.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=5)
frame_usuarios.grid_columnconfigure(1, weight=1)

# ========= TAB FACTURAS =========
frame_facturas = ttk.Frame(notebook)
notebook.add(frame_facturas, text="Facturas")

tk.Label(frame_facturas, text="Email usuario").grid(row=0, column=0)
entry_factura_email = tk.Entry(frame_facturas)
entry_factura_email.grid(row=0, column=1)

tk.Label(frame_facturas, text="Descripción").grid(row=1, column=0)
entry_factura_desc = tk.Entry(frame_facturas)
entry_factura_desc.grid(row=1, column=1)

tk.Label(frame_facturas, text="Monto").grid(row=2, column=0)
entry_factura_monto = tk.Entry(frame_facturas)
entry_factura_monto.grid(row=2, column=1)

tk.Label(frame_facturas, text="Estado").grid(row=3, column=0)
combo_factura_estado = ttk.Combobox(frame_facturas, values=["Pendiente", "Pagada", "Cancelada"])
combo_factura_estado.grid(row=3, column=1)
combo_factura_estado.current(0)

tk.Button(frame_facturas, text="Crear Factura", command=crear_factura).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(frame_facturas, text="Mostrar Facturas", command=mostrar_facturas_usuario).grid(row=5, column=0, columnspan=2, pady=5)

# Lista de facturas
cols_facturas = ("Número", "Descripción", "Monto", "Estado")
lista_facturas = ttk.Treeview(frame_facturas, columns=cols_facturas, show="headings")
for col in cols_facturas:
    lista_facturas.heading(col, text=col)
lista_facturas.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=5)

# ========= TAB RESUMEN =========
frame_resumen = ttk.Frame(notebook)
notebook.add(frame_resumen, text="Resumen Financiero")

tk.Button(frame_resumen, text="Actualizar Resumen", command=mostrar_resumen).pack(pady=5)

cols_resumen = ("Usuario", "Total", "Pagadas", "Pendientes")
lista_resumen = ttk.Treeview(frame_resumen, columns=cols_resumen, show="headings")
for col in cols_resumen:
    lista_resumen.heading(col, text=col)
lista_resumen.pack(fill="both", expand=True, pady=5)

root.mainloop()