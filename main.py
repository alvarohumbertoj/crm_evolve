from .services import CRMService  # Import relativo seguro

def menu():
    print("\n=== SISTEMA CRM ===")
    print("1. Registrar nuevo usuario")
    print("2. Buscar usuario")
    print("3. Crear factura para usuario")
    print("4. Mostrar todos los usuarios")
    print("5. Mostrar facturas de un usuario")
    print("6. Resumen financiero por usuario")
    print("7. Salir")

def main():
    crm = CRMService()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            print(crm.registrar_usuario(nombre, apellidos, email, telefono, direccion))

        elif opcion == "2":
            email = input("Email a buscar: ")
            usuario = crm.repo.buscar_usuario_por_email(email)
            print(usuario if usuario else "❌ Usuario no encontrado.")

        elif opcion == "3":
            email = input("Email del usuario: ")
            descripcion = input("Descripción: ")
            try:
                monto = float(input("Monto: "))
            except ValueError:
                print("❌ Monto inválido.")
                continue
            estado = input("Estado (Pendiente/Pagada/Cancelada): ")
            print(crm.crear_factura(email, descripcion, monto, estado))

        elif opcion == "4":
            for u in crm.repo.usuarios:
                print(u)

        elif opcion == "5":
            email = input("Email: ")
            facturas = crm.repo.facturas_por_email(email)
            if facturas:
                for f in facturas:
                    print(f)
            else:
                print("❌ No tiene facturas.")

        elif opcion == "6":
            for nombre, total, pagadas, pendientes in crm.resumen_financiero():
                print(f"{nombre} - Total: {total}€ | Pagadas: {pagadas}€ | Pendientes: {pendientes}€")

        elif opcion == "7":
            print("👋 Saliendo del CRM...")
            break

if __name__ == "__main__":
    main()