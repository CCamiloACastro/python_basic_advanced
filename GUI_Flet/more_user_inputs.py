import flet as ft


def main(page):
    # TextBox
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"  # Muestra texto en rojo
            page.update()
        else:
            name = txt_name.value
            page.clean()  # Quita todos los widgets
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

    # Checkbox

    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)  # la primera vez "ft.Text()" pero no se muestra porque está vacío

    def button_clicked(e):
        output_text2.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text2 = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text2)

    # Slider
    len_images = 100

    def slider_changed(e):
        t.value = f"Slider changed to {round(e.control.value)}"
        page.update()

    t = ft.Text()
    page.add(
        ft.Text("Slider with 'on_change' event:"),
        # ft.Slider(min=0, max=100, divisions=10, label="{value}%", on_change=slider_changed), t)
        ft.Slider(min=0, max=len_images, divisions=len_images, label="{value}", on_change=slider_changed), t)


ft.app(target=main)
