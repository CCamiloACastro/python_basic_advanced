"""
Guia de inicio
"""

import time
import flet as ft


def main(page: ft.Page):
    page.scroll = True # Añade un scroll a la pagina
    # add/update controls on Page
    t = ft.Text(value="Hola, bbsote!", color="blue", size=100)
    page.controls.append(t)  # loc controles son widgets

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    t = ft.Text()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        t.value = f"Step {i}"
        time.sleep(0.1)
        page.update()  # Envia cambios a la página

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    # botones con Controladores de eventos
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    # otro evento click
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # hint_text oculta texto el texto al escribir
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    first_name = ft.TextField(label="First name")
    last_name = ft.TextField(label="last name")
    first_name.disabled = False
    last_name.disabled = True
    page.add(first_name, last_name)

    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)


ft.app(target=main)  # ver en el escritorio
# ft.app(target=main, view=ft.WEB_BROWSER)  # ver en el navegador
