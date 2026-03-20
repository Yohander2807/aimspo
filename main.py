import flet as ft
import time

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE VENTANA (MODO OVERLAY) ---
    page.title = "SOPSoft V4.7 Final"
    page.window_width = 350
    page.window_height = 600
    page.window_always_on_top = True
    page.bgcolor = "#050505"  # Negro profundo
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_opacity = 0.9  # Transparencia para ver el juego detrás

    # Colores de la marca SOPSoft
    naranja_sop = "#FF8C00"
    gris_oscuro = "#121212"

    # --- LÓGICA DE FUNCIONES ---
    def on_change_switch(e):
        if e.control.label == "Aimbot Pro":
            status.value = "AIMBOT: ACTIVO" if e.control.value else "AIMBOT: OFF"
        elif e.control.label == "Antena Wire":
            status.value = "ANTENA: ACTIVA" if e.control.value else "ANTENA: OFF"
        
        status.color = "green" if e.control.value else naranja_sop
        page.update()

    # --- COMPONENTES DE LA UI ---
    
    # Header con Estilo Engineering
    header = ft.Container(
        content=ft.Column([
            ft.Text("SOPSoft", size=45, weight="bold", color=naranja_sop, font_family="Impact"),
            ft.Text("V4.7 FINAL | PAYPAL & PINTEREST FIX", size=10, color="grey"),
            ft.Text("UPTYAB - Yaracuy", size=9, italic=True, color="#444444"),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        margin=ft.margin.only(bottom=20)
    )

    # Monitor de Estado (PayPal Robusto Style)
    status = ft.Text("SISTEMA STANDBY", color=naranja_sop, weight="bold", size=12)
    status_box = ft.Container(
        content=status,
        padding=10,
        bgcolor=gris_oscuro,
        border_radius=10,
        border=ft.border.all(1, "#222222"),
        alignment=ft.alignment.center
    )

    # Panel de Control (Trucos)
    controls_card = ft.Container(
        content=ft.Column([
            ft.Text("MODS PRINCIPALES", size=14, weight="bold", color="grey"),
            ft.Divider(color="#222222"),
            
            # Switch Aimbot
            ft.Row([
                ft.Icon(ft.icons.TARGET, color=naranja_sop),
                ft.Switch(label="Aimbot Pro", active_color=naranja_sop, on_change=on_change_switch)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            # Switch Antena
            ft.Row([
                ft.Icon(ft.icons.SENSORS, color=naranja_sop),
                ft.Switch(label="Antena Wire", active_color=naranja_sop, on_change=on_change_switch)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            ft.Text("SENSIBILIDAD Y PINTEREST FIX", size=12, color="grey", margin=ft.margin.only(top=15)),
            ft.Slider(min=0, max=100, active_color=naranja_sop, divisions=10, label="Sens: {value}%"),
        ]),
        padding=20,
        bgcolor="#0d0d0d",
        border_radius=20,
        border=ft.border.all(1, "#1a1a1a")
    )

    # Botón de Inyección (PayPal Secure)
    btn_inject = ft.ElevatedButton(
        content=ft.Row([
            ft.Icon(ft.icons.BOLT),
            ft.Text("INICIAR INYECCIÓN", weight="bold")
        ], alignment=ft.MainAxisAlignment.CENTER),
        width=400,
        height=50,
        style=ft.ButtonStyle(
            color="white",
            bgcolor={"": naranja_sop, "hovered": "#e67e00"},
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
        on_click=lambda _: print("Injecting...")
    )

    # Créditos
    footer = ft.Text("Developer: Yohander - 2026", size=10, color="#333333", text_align="center")

    # Agregar a la página
    page.add(
        header,
        status_box,
        ft.Container(height=10),
        controls_card,
        ft.Container(height=20),
        btn_inject,
        ft.Container(height=10),
        ft.Divider(color="#111111"),
        footer
    )

ft.app(target=main)