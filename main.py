import flet as ft
import random
import time

def main(page: ft.Page):
    page.title = "SOPSoft - RED EDITION"
    page.window_width = 360
    page.window_height = 620
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_opacity = 0.85 # Transparencia para ver enemigos detrás

    # Colores SOP RED
    rojo_neon = "#FF0000"
    rojo_oscuro = "#4D0000"

    # Lógica Anti-Ban (Genera IDs falsos para camuflar el proceso)
    def antiban_log():
        logs = ["Limpiando registros...", "Bypass Activo", "ID Aleatorio: " + str(random.randint(1000, 9999))]
        for log in logs:
            status.value = log
            page.update()
            time.sleep(0.5)

    def on_toggle(e):
        if e.control.value:
            antiban_log()
            status.value = f"{e.control.label.upper()} ACTIVADO"
            status.color = "white"
        else:
            status.value = "SISTEMA STANDBY"
            status.color = rojo_neon
        page.update()

    # --- UI ---
    header = ft.Column([
        ft.Text("SOPSoft", size=50, weight="bold", color=rojo_neon, font_family="Impact"),
        ft.Text("RED APK - BYPASS V2", size=12, color="white", weight="bold"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    status = ft.Text("ESPERANDO INYECCIÓN", color=rojo_neon, weight="bold")
    
    # Panel Central
    menu = ft.Container(
        content=ft.Column([
            ft.Text("MODS VIP", size=14, color="white", weight="bold"),
            ft.Divider(color=rojo_neon),
            # Antena
            ft.Row([
                ft.Icon(ft.icons.SENSORS, color=rojo_neon),
                ft.Switch(label="Antena Cabeza 100%", active_color=rojo_neon, on_change=on_toggle)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            # Auto Apuntado
            ft.Row([
                ft.Icon(ft.icons.TARGET, color=rojo_neon),
                ft.Switch(label="Auto Apuntado (Head)", active_color=rojo_neon, on_change=on_toggle)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            # Anti-Ban
            ft.Row([
                ft.Icon(ft.icons.SECURITY, color=rojo_neon),
                ft.Switch(label="Anti-Ban (Bypass)", active_color=rojo_neon, on_change=on_toggle, value=True)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ]),
        padding=20,
        bgcolor=rojo_oscuro,
        border_radius=20,
        border=ft.border.all(2, rojo_neon)
    )

    btn_start = ft.ElevatedButton(
        "INYECTAR AHORA",
        icon=ft.icons.FLASH_ON,
        width=400,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=rojo_neon,
            color="white",
            shape=ft.RoundedRectangleBorder(radius=15),
        )
    )

    page.add(header, ft.Divider(height=20, color="transparent"), ft.Center(status), ft.Divider(height=10, color="transparent"), menu, ft.Divider(height=30, color="transparent"), btn_start)

ft.app(target=main)