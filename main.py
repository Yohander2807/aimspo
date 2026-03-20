import flet as ft
import random

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE PANTALLA ---
    page.title = "SOPSoft RED v4.7.3"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.window_always_on_top = True
    page.padding = 20
    
    # Colores Neón
    RED = "#FF0000"
    DARK_RED = "#2b0000"

    # --- FUNCIONES ---
    def handle_change(e):
        status.value = f"{e.control.label.upper()} ACTIVADO"
        status.color = "white"
        page.update()

    # --- INTERFAZ ---
    status = ft.Text("SISTEMA OPERATIVO", color=RED, weight="bold")

    menu_container = ft.Container(
        content=ft.Column([
            ft.Text("SOPSoft RED EDITION", size=28, weight="bold", color=RED),
            ft.Divider(color=RED, height=20),
            
            # Mods
            ft.Switch(label="Antena Cabeza", active_color=RED, on_change=handle_change),
            ft.Switch(label="Auto-Aimbot", active_color=RED, on_change=handle_change),
            ft.Switch(label="Anti-Ban Bypass", active_color=RED, value=True, on_change=handle_change),
            
            ft.Divider(height=20, color="transparent"),
            ft.Slider(min=0, max=100, label="Sensibilidad: {value}%", active_color=RED),
            
            ft.ElevatedButton(
                "INYECTAR AL JUEGO",
                bgcolor=RED,
                color="white",
                width=300,
                height=50,
                on_click=lambda _: print("Inyectando...")
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20,
        bgcolor=DARK_RED,
        border_radius=20,
        border=ft.border.all(1, RED)
    )

    # Limpiar y agregar (Evita errores de renderizado inicial)
    page.clean()
    page.add(
        ft.Center(
            ft.Column([
                menu_container,
                ft.Text("v4.7.3 Final - UPTYAB", size=10, color="grey")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )

# ESTA LÍNEA ES VITAL PARA EVITAR LA PANTALLA NEGRA EN ANDROID
if __name__ == "__main__":
    ft.app(target=main)