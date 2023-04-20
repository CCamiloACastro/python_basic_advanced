import flet as ft

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    img = ft.Image(
        # src=f"/icons/icon-512.png",
        src=f"octofius.png",
        width=250,
        height=250,
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(10),
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.add(img, images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.app(target=main)